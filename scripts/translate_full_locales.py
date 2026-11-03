"""Refresh localized README/Notebook prose from the English canonical locale.

This is a maintainer-only helper. Ordinary CI is network-free and never calls
translation services. The committed locale JSON files are the distributable
source used by build_notebooks.py and build_readmes.py.

The maintenance model intentionally matches the other piccoripico Colab ASR
repositories: no API key or cloud account is required. The default path uses
``deep-translator``'s GoogleTranslator and falls back to the same unauthenticated
Google translation endpoint used by whisper-colab when the static language map
is missing a target or the primary path is rate-limited.

English is the only canonical translation source. Successful locales are checkpointed one
by one. A failed locale remains pending and does not abort unrelated locales.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


from languages import LANGUAGES, SET1_LANGUAGES, CANONICAL

ROOT = Path(__file__).resolve().parents[1]
LOC = ROOT / "locales"
LOCALIZATION = ROOT / "localization"
PLAN_PATH = LOCALIZATION / "translation_plan.json"
RUN_REPORT_PATH = LOCALIZATION / "translation_run_report.json"
DIRECT_URL = "https://translate.googleapis.com/translate_a/single"

# Google service target-code adapters. These are transport details only;
# repository/publication locale codes remain ISO 639 Set 1 codes.
GOOGLE_TARGET_CODES = {
    "he": "iw",
    "nb": "no",
    "zh": "zh-CN",
}

# Keep traffic deliberately conservative. The earlier all-at-once run hit 429,
# so this helper favors reliability over throughput.
DEFAULT_REQUEST_DELAY = 4.0
DEFAULT_COOLDOWN_429 = 90.0
DEFAULT_CHUNK_CHARS = 2800

PROTECT_PATTERNS = [
    re.compile(r"`[^`]+`"),
    re.compile(r"https?://[^\s)]+"),
    re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\}"),
    re.compile(r"\bGoogle Colab\b"),
    re.compile(r"\bGoogle Drive\b"),
    re.compile(r"\bHaas-ja-v1\.0\b"),
    re.compile(r"\bthird-intelligence/Haas-ja-v1\.0\b"),
    re.compile(r"\bNeMo\b"),
    re.compile(r"\bCUDA\b"),
    re.compile(r"\bGPU\b"),
    re.compile(r"\bJSON\b"),
    re.compile(r"\bTXT\b"),
    re.compile(r"\bCSV\b"),
    re.compile(r"\bXLSX\b"),
    re.compile(r"\bSRT\b"),
    re.compile(r"\bZIP\b"),
    re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b"),
    re.compile(r"\b[a-z]+_[a-z0-9_]+\b"),
]
PROTECT_RE = re.compile("|".join(f"(?:{p.pattern})" for p in PROTECT_PATTERNS))
COMMENT_PREFIX_PATTERNS = [
    re.compile(r"^(# @title \d+\. )(.*)$", re.S),
    re.compile(r"^(# \d+\. )(.*)$", re.S),
    re.compile(r"^(# @markdown #{2,3} )(.*)$", re.S),
    re.compile(r"^(# @markdown - )(.*)$", re.S),
    re.compile(r"^(# @markdown )(.*)$", re.S),
    re.compile(r"^(# )(.*)$", re.S),
]
MARKDOWN_PREFIX_RE = re.compile(r"^(\s*(?:#{1,6}\s+|[-*+]\s+|\d+[.)]\s+|>\s+))(.*)$", re.S)
ITEM_RE = re.compile(r"ZXQITEM(\d{3})QXZ\s*(.*?)(?=\n?ZXQITEM\d{3}QXZ|$)", re.S)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def canonical_source_sha256(canonical: dict) -> str:
    payload = json.dumps(
        {"placeholders": canonical["placeholders"], "readme_markdown": canonical["readme_markdown"]},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def protect(text: str) -> tuple[str, dict[str, str]]:
    tokens: dict[str, str] = {}
    def repl(match: re.Match[str]) -> str:
        token = f"ZXQPROTECT{len(tokens):04d}QXZ"
        tokens[token] = match.group(0)
        return token
    return PROTECT_RE.sub(repl, text), tokens


def restore(text: str, tokens: dict[str, str]) -> str:
    out = html.unescape(text)
    for token, value in tokens.items():
        # Exact token is expected; tolerate whitespace inserted between characters.
        if token in out:
            out = out.replace(token, value)
            continue
        loose = r"\s*".join(re.escape(ch) for ch in token)
        out, n = re.subn(loose, lambda _m, v=value: v, out, count=1, flags=re.I)
        if not n:
            raise RuntimeError(f"protected token was not preserved: {token}")
    return out


def split_comment_prefix(text: str) -> tuple[str, str]:
    for pattern in COMMENT_PREFIX_PATTERNS:
        m = pattern.match(text)
        if m:
            return m.group(1), m.group(2)
    return "", text


@dataclass
class Unit:
    key: str
    prefix: str
    protected: str
    tokens: dict[str, str]


def make_unit(key: str, prefix: str, body: str) -> Unit:
    protected, tokens = protect(body)
    return Unit(key, prefix, protected, tokens)


def prepare_placeholder_units(canonical: dict) -> list[Unit]:
    units: list[Unit] = []
    for key, value in canonical["placeholders"].items():
        prefix, body = split_comment_prefix(value)
        units.append(make_unit(f"ph::{key}", prefix, body))
    return units


def prepare_readme_units(markdown: str) -> tuple[list[Unit], list[tuple[str, str]]]:
    units: list[Unit] = []
    plan: list[tuple[str, str]] = []
    in_fence = False
    counter = 0
    for line in markdown.splitlines(keepends=True):
        raw = line[:-1] if line.endswith("\n") else line
        nl = "\n" if line.endswith("\n") else ""
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            plan.append(("literal", raw + nl))
            continue
        if in_fence or not raw.strip():
            plan.append(("literal", raw + nl))
            continue
        prefix, body = "", raw
        m = MARKDOWN_PREFIX_RE.match(raw)
        if m:
            prefix, body = m.group(1), m.group(2)
        key = f"readme::{counter:04d}"
        counter += 1
        units.append(make_unit(key, prefix, body))
        plan.append(("unit", key + ("\n" if nl else "")))
    return units, plan


def reconstruct_readme(plan: list[tuple[str, str]], translated: dict[str, str]) -> str:
    out: list[str] = []
    for kind, value in plan:
        if kind == "literal":
            out.append(value)
            continue
        has_nl = value.endswith("\n")
        key = value[:-1] if has_nl else value
        out.append(translated[key] + ("\n" if has_nl else ""))
    return "".join(out)


def chunks(units: list[Unit], limit: int) -> list[list[Unit]]:
    result: list[list[Unit]] = []
    current: list[Unit] = []
    size = 0
    for unit in units:
        n = len(unit.protected) + 24
        if current and size + n > limit:
            result.append(current)
            current, size = [], 0
        current.append(unit)
        size += n
    if current:
        result.append(current)
    return result


def is_rate_limit(exc: Exception) -> bool:
    text = f"{type(exc).__name__}: {exc}".lower()
    return type(exc).__name__ == "TooManyRequests" or "429" in text or "too many requests" in text or "rate limit" in text


@dataclass
class RequestPacer:
    delay: float
    last_request: float = 0.0

    def wait(self) -> None:
        elapsed = time.monotonic() - self.last_request
        if self.last_request and elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self.last_request = time.monotonic()


@dataclass
class AuthFreeTranslator:
    target: str
    session: Any
    pacer: RequestPacer
    cooldown_429: float
    backend: str = field(init=False)
    google: object | None = field(init=False, default=None)
    providers_used: set[str] = field(default_factory=set)

    def __post_init__(self) -> None:
        # Lazy import keeps --plan fully offline and dependency-free.
        try:
            from deep_translator import GoogleTranslator
            from deep_translator.exceptions import LanguageNotSupportedException
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "Translation execution requires requirements-localization.txt; "
                "--plan does not."
            ) from exc
        try:
            self.google = GoogleTranslator(source="en", target=self.target)
            self.backend = "deep-translator-google"
        except LanguageNotSupportedException:
            self.backend = "google-gtx"

    def _direct(self, text: str) -> str:
        self.pacer.wait()
        response = self.session.get(
            DIRECT_URL,
            params={"client": "gtx", "sl": "en", "tl": self.target, "dt": "t", "q": text},
            timeout=45,
        )
        if response.status_code == 429:
            raise RuntimeError("Google GTX HTTP 429")
        response.raise_for_status()
        payload = response.json()
        if not payload or not payload[0]:
            raise RuntimeError("Google GTX returned an empty payload")
        return "".join(part[0] for part in payload[0] if part and part[0])

    def _deep(self, text: str) -> str:
        assert self.google is not None
        self.pacer.wait()
        return self.google.translate(text)

    def translate(self, text: str, retries: int = 5) -> str:
        last: Exception | None = None
        for attempt in range(retries):
            try:
                if self.backend == "deep-translator-google":
                    result = self._deep(text)
                    self.providers_used.add("deep-translator-google")
                else:
                    result = self._direct(text)
                    self.providers_used.add("google-gtx")
                if not isinstance(result, str) or not result.strip():
                    raise RuntimeError("empty translation")
                return result
            except Exception as exc:
                last = exc
                # The primary deep-translator path may be rate-limited while the
                # endpoint used by whisper-colab still works. Switch once before
                # imposing a long cooldown.
                if self.backend == "deep-translator-google":
                    self.backend = "google-gtx"
                    time.sleep(max(self.pacer.delay, 2.0))
                    continue
                if is_rate_limit(exc):
                    time.sleep(self.cooldown_429 * (attempt + 1))
                else:
                    time.sleep(min(30.0, 3.0 * (attempt + 1)))
        assert last is not None
        raise last


def translate_chunk(translator: AuthFreeTranslator, batch: list[Unit]) -> dict[str, str]:
    if len(batch) == 1:
        unit = batch[0]
        text = translator.translate(unit.protected)
        return {unit.key: unit.prefix + restore(text, unit.tokens)}

    block = "\n".join(f"ZXQITEM{i:03d}QXZ\n{unit.protected}" for i, unit in enumerate(batch))
    translated = translator.translate(block)
    matches = list(ITEM_RE.finditer(translated))
    if len(matches) != len(batch):
        # Marker normalization occasionally occurs. Fall back to individual calls
        # rather than invalidating the entire locale.
        out: dict[str, str] = {}
        for unit in batch:
            one = translator.translate(unit.protected)
            out[unit.key] = unit.prefix + restore(one, unit.tokens)
        return out
    out: dict[str, str] = {}
    for m in matches:
        i = int(m.group(1))
        if i >= len(batch):
            raise RuntimeError("invalid translated item marker")
        unit = batch[i]
        out[unit.key] = unit.prefix + restore(m.group(2).strip(), unit.tokens)
    if len(out) != len(batch):
        raise RuntimeError("translated batch did not reconstruct all units")
    return out


def translate_locale(code: str, canonical: dict, session: Any, delay: float, cooldown: float, chunk_chars: int) -> tuple[dict[str, str], str, set[str]]:
    target = GOOGLE_TARGET_CODES.get(code, code)
    translator = AuthFreeTranslator(target, session, RequestPacer(delay), cooldown)
    ph_units = prepare_placeholder_units(canonical)
    readme_units, readme_plan = prepare_readme_units(canonical["readme_markdown"])
    translated: dict[str, str] = {}
    for batch in chunks(ph_units + readme_units, chunk_chars):
        translated.update(translate_chunk(translator, batch))
    placeholders = {u.key.removeprefix("ph::"): translated[u.key] for u in ph_units}
    readme = reconstruct_readme(readme_plan, translated)
    return placeholders, readme, set(translator.providers_used)


def build_plan(codes: list[str], canonical: dict) -> dict:
    rows=[]
    current_hash=canonical_source_sha256(canonical)
    for code in codes:
        d=load_json(LOC/f"{code}.json")
        rows.append({
            "code":code,
            "english_name":LANGUAGES[code]["english_name"],
            "current_status":d.get("status"),
            "target":GOOGLE_TARGET_CODES.get(code,code),
            "fresh":d.get("canonical_source_sha256")==current_hash,
        })
    pending=[r for r in rows if r["current_status"] not in {"canonical","reviewed","machine-translated"} or not r["fresh"]]
    return {
        "canonical":CANONICAL,
        "set1_reference_count":len(SET1_LANGUAGES),
        "publication_locale_count":len(LANGUAGES),
        "translation_target_count":len(LANGUAGES)-1,
        "requested_count":len(rows),
        "pending_or_stale_count":len(pending),
        "languages":rows,
    }


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--plan",action="store_true",help="write a local plan only; no network or credentials")
    ap.add_argument("--codes",nargs="*",help="optional publication-scope language codes")
    ap.add_argument("--overwrite",action="store_true",help="retranslate fresh machine-translated locales")
    ap.add_argument("--overwrite-reviewed",action="store_true",help="also overwrite reviewed locales (use deliberately)")
    ap.add_argument("--request-delay",type=float,default=DEFAULT_REQUEST_DELAY)
    ap.add_argument("--cooldown-429",type=float,default=DEFAULT_COOLDOWN_429)
    ap.add_argument("--chunk-chars",type=int,default=DEFAULT_CHUNK_CHARS)
    ap.add_argument("--max-locales",type=int,default=0,help="0=all selected; otherwise process at most N non-skipped locales")
    ap.add_argument("--fail-fast",action="store_true")
    args=ap.parse_args()

    canonical=load_json(LOC/f"{CANONICAL}.json")
    requested=args.codes or [c for c in LANGUAGES if c!=CANONICAL]
    invalid=[c for c in requested if c not in LANGUAGES or c==CANONICAL]
    if invalid:
        raise SystemExit("Codes outside the configured publication scope: "+", ".join(invalid))

    plan=build_plan(requested,canonical)
    write_json(PLAN_PATH,plan)
    print(f"Translation plan: requested={plan['requested_count']} pending-or-stale={plan['pending_or_stale_count']} publication-locales={plan['publication_locale_count']}")
    print("Plan:",PLAN_PATH.relative_to(ROOT))
    if args.plan:
        return

    try:
        import requests
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Translation execution requires requirements-localization.txt; "
            "run: python -m pip install -r requirements-localization.txt"
        ) from exc

    run={"requested_codes":requested,"success":[],"skipped":[],"failed":[],"request_delay":args.request_delay,"cooldown_429":args.cooldown_429}
    current_hash=canonical_source_sha256(canonical)
    session=requests.Session()
    processed=0
    for code in requested:
        path=LOC/f"{code}.json"
        d=load_json(path)
        status=d.get("status")
        fresh=d.get("canonical_source_sha256")==current_hash
        if status in {"reviewed","stale-reviewed"} and not args.overwrite_reviewed:
            print(f"skip {code}: {status}")
            run["skipped"].append({"code":code,"reason":status})
            continue
        if status=="machine-translated" and fresh and not args.overwrite:
            print(f"skip {code}: machine-translated fresh")
            run["skipped"].append({"code":code,"reason":"machine-translated fresh"})
            continue
        if args.max_locales and processed>=args.max_locales:
            break
        processed+=1
        target=GOOGLE_TARGET_CODES.get(code,code)
        print(f"translate {code} -> {target} [auth-free Google path]",flush=True)
        try:
            placeholders,readme,providers=translate_locale(code,canonical,session,args.request_delay,args.cooldown_429,args.chunk_chars)
            d["placeholders"]=placeholders
            d["readme_markdown"]=readme
            d["status"]="machine-translated"
            d["canonical_source_sha256"]=current_hash
            d["translation_source"]="Full translation machine-generated from English canonical source; review recommended."
            d.pop("stale_against_canonical_source_sha256",None)
            write_json(path,d)
            run["success"].append({"code":code,"target":target,"providers":sorted(providers)})
        except Exception as exc:
            # Preserve reviewed text. Other failures remain non-publishable and retryable.
            if status not in {"reviewed","stale-reviewed"}:
                d["status"]="pending"
            error=f"{type(exc).__name__}: {exc}"
            write_json(path,d)
            run["failed"].append({"code":code,"target":target,"error":error})
            print(f"FAILED {code}: {error}",flush=True)
            if args.fail_fast:
                write_json(RUN_REPORT_PATH,run)
                raise
    write_json(RUN_REPORT_PATH,run)
    print("SUMMARY:",f"success={len(run['success'])}",f"skipped={len(run['skipped'])}",f"failed={len(run['failed'])}")
    print("Run report:",RUN_REPORT_PATH.relative_to(ROOT))
    if run["failed"]:
        raise SystemExit(2)

if __name__=="__main__":
    main()
