"""Finalize the English-canonical 183-locale localization set.

This is a maintainer entry point, not part of normal CI.  It never treats stale
legacy translations as fresh.  `--plan` is offline and stdlib-only.  With
`--translate`, the translation helper checkpoints each successful locale, then
this script rebuilds deterministic artifacts and runs the full publication gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"
SET1 = ROOT / "localization" / "set1_languages.json"
CANONICAL = "en"
ROOT_PRESENTATION = "ja"
PUBLISHABLE = {"canonical", "reviewed", "machine-translated"}
FINAL_ARCHIVE_NAME = "haas-ja-colab-v1.0.0-set1-183-en-canonical-final.zip"
TRANSIENT_RELATIVE_PATHS = {
    "localization/translation_plan.json",
    "localization/translation_run_report.json",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash() -> str:
    row = load_json(LOCALES / f"{CANONICAL}.json")
    payload = json.dumps(
        {"placeholders": row["placeholders"], "readme_markdown": row["readme_markdown"]},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def set1_codes() -> list[str]:
    data = load_json(SET1)
    return [row["code"] for row in data["languages"]]


def plan() -> dict:
    codes = set1_codes()
    current_hash = canonical_hash()
    rows = {code: load_json(LOCALES / f"{code}.json") for code in codes}
    pending = [
        code
        for code, row in rows.items()
        if code != CANONICAL
        and (row.get("status") not in PUBLISHABLE or row.get("canonical_source_sha256") != current_hash)
    ]
    statuses = Counter(row.get("status", "missing") for row in rows.values())
    return {
        "canonical": CANONICAL,
        "root_presentation": ROOT_PRESENTATION,
        "set1_locales": len(codes),
        "translation_targets": len(codes) - 1,
        "pending_or_stale": len(pending),
        "pending_codes": pending,
        "statuses": dict(sorted(statuses.items())),
        "canonical_source_sha256": current_hash,
        "publication_ready": len(pending) == 0,
    }


def run_checked(args: list[str]) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def translate() -> int:
    args = [sys.executable, str(ROOT / "scripts" / "translate_full_locales.py")]
    print("+", " ".join(args), flush=True)
    return subprocess.run(args, cwd=ROOT, check=False).returncode


def build_and_verify() -> None:
    for name in ("build_languages.py", "build_notebooks.py", "build_readmes.py"):
        run_checked([sys.executable, str(ROOT / "scripts" / name)])
    run_checked([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
    run_checked([sys.executable, str(ROOT / "scripts" / "check_repository.py")])


def package_final() -> tuple[Path, str]:
    output = ROOT.parent / FINAL_ARCHIVE_NAME
    if output.exists():
        output.unlink()
    root_name = ROOT.name
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in {".git", ".venv", "__pycache__"} for part in rel.parts):
            continue
        if path.suffix == ".pyc" or rel.as_posix() in TRANSIENT_RELATIVE_PATHS:
            continue
        files.append(path)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda p: p.relative_to(ROOT).as_posix()):
            rel = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"{root_name}/{rel}", date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return output, digest


def emit(data: dict, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, ensure_ascii=False, sort_keys=True))
        return
    print(
        "Localization state:",
        f"canonical={data['canonical']}",
        f"Set1={data['set1_locales']}",
        f"targets={data['translation_targets']}",
        f"pending-or-stale={data['pending_or_stale']}",
    )
    if data["pending_codes"]:
        print("Pending/stale:", " ".join(data["pending_codes"]))
    print("Statuses:", json.dumps(data["statuses"], ensure_ascii=False, sort_keys=True))
    print("Publication ready:", "yes" if data["publication_ready"] else "no")


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--plan", action="store_true", help="offline state inspection only")
    action.add_argument("--translate", action="store_true", help="translate stale locales, then build and verify")
    action.add_argument("--verify", action="store_true", help="build and verify without network translation")
    parser.add_argument("--json", action="store_true", help="machine-readable output for --plan")
    args = parser.parse_args()

    before = plan()
    if args.plan:
        emit(before, args.json)
        return

    translation_rc = 0
    if args.translate and before["pending_or_stale"]:
        translation_rc = translate()

    after_translation = plan()
    if after_translation["pending_or_stale"]:
        emit(after_translation, False)
        suffix = f" Translation helper exit code: {translation_rc}." if args.translate else ""
        raise SystemExit(
            "Finalization stopped: untranslated/stale locales remain. "
            "Successful locales were checkpointed; rerun --translate after resolving failures." + suffix
        )

    if args.translate and translation_rc != 0:
        raise SystemExit(f"Translation helper exited with {translation_rc} despite no pending locale; inspect the run report.")

    build_and_verify()
    final = plan()
    if not final["publication_ready"]:
        raise SystemExit("Finalization stopped: publication gate is not green after verification.")
    emit(final, False)
    archive, digest = package_final()
    print("FINAL LOCALIZATION VERIFICATION PASSED")
    print("Final archive:", archive)
    print("SHA-256:", digest)


if __name__ == "__main__":
    main()
