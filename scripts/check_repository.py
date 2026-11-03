from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from languages import CANONICAL, LANGUAGES, SET1_DATA

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"
NOTEBOOKS = ROOT / "notebooks"
READMES = ROOT / "docs" / "README"
SOURCE_README = ROOT / "source" / "README.en.md"
ROOT_README = ROOT / "README.md"
ROOT_PRESENTATION = "ja"

errors: list[str] = []
PUBLISHABLE = {"canonical", "reviewed", "machine-translated"}
EXPECTED_LOCALE_SCHEMA = {
    "language", "english_name", "native_name", "direction", "canonical",
    "status", "translation_source", "canonical_source_sha256",
    "placeholders", "readme_markdown"
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str) -> None:
    errors.append(message)


expected_codes = set(LANGUAGES)
if SET1_DATA.get("count") != 183 or len(expected_codes) != 183:
    fail("active ISO 639 Set 1 catalog must contain exactly 183 codes")
if SET1_DATA.get("excluded_deprecated") != ["sh"] or "sh" in expected_codes:
    fail("deprecated sh must be the sole excluded Set 1 code")
if CANONICAL != "en":
    fail("canonical language must be en")
if (ROOT / "localization" / "publication_targets.json").exists():
    fail("publication_targets.json is obsolete when publication scope equals Set 1")
old_sync_name = "sync_from_" + "japanese.py"
if (ROOT / "scripts" / old_sync_name).exists():
    fail(old_sync_name + " is obsolete under English canonical architecture")

locale_codes = {path.stem for path in LOCALES.glob("*.json")}
if locale_codes != expected_codes:
    fail(
        "locale set mismatch: "
        f"missing={sorted(expected_codes - locale_codes)}, "
        f"extra={sorted(locale_codes - expected_codes)}"
    )

en_path = LOCALES / "en.json"
ja_path = LOCALES / "ja.json"
if not en_path.exists():
    fail("locales/en.json is missing")
    en = {"placeholders": {}, "readme_markdown": ""}
else:
    en = load_json(en_path)
if not ja_path.exists():
    fail("locales/ja.json is missing")
    ja = {"placeholders": {}, "readme_markdown": ""}
else:
    ja = load_json(ja_path)

if en.get("status") != "canonical" or en.get("canonical") is not True:
    fail("en locale must be canonical")
if ja.get("status") != "reviewed" or ja.get("canonical") is not False:
    fail("ja locale must be reviewed and non-canonical")
if SOURCE_README.exists():
    if en.get("readme_markdown") != SOURCE_README.read_text(encoding="utf-8"):
        fail("en locale README snapshot differs from source/README.en.md; run sync_from_english.py")
else:
    fail("source/README.en.md is missing")
if ROOT_README.exists():
    if ja.get("readme_markdown") != ROOT_README.read_text(encoding="utf-8"):
        fail("root README.md must equal fresh reviewed ja locale README")
else:
    fail("README.md is missing")

canonical_payload = json.dumps(
    {
        "placeholders": en.get("placeholders", {}),
        "readme_markdown": en.get("readme_markdown", ""),
    },
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")
canonical_hash = hashlib.sha256(canonical_payload).hexdigest()
if en.get("canonical_source_sha256") != canonical_hash:
    fail("en canonical source hash is stale")

placeholder_keys = set(en.get("placeholders", {}))
status_counts: Counter[str] = Counter()
for code in sorted(expected_codes & locale_codes):
    row = load_json(LOCALES / f"{code}.json")
    status_counts[row.get("status", "<missing>")] += 1

    if row.get("language") != code:
        fail(f"{code}: language field mismatch")
    if set(row.get("placeholders", {})) != placeholder_keys:
        fail(f"{code}: placeholder key mismatch")
    if set(row) != EXPECTED_LOCALE_SCHEMA:
        fail(f"{code}: locale schema mismatch: {sorted(set(row) ^ EXPECTED_LOCALE_SCHEMA)}")
    if row.get("canonical_source_sha256") != canonical_hash:
        fail(f"{code}: stale relative to English canonical source")
    if code == CANONICAL:
        if row.get("canonical") is not True:
            fail("en: canonical must be true")
    elif row.get("canonical") is not False:
        fail(f"{code}: canonical must be false")

if status_counts.get("canonical") != 1:
    fail(f"status distribution requires canonical=1, got {status_counts.get('canonical', 0)}")
if status_counts.get("reviewed") != 1:
    fail(f"status distribution requires reviewed=1, got {status_counts.get('reviewed', 0)}")
if status_counts.get("machine-translated") != 181:
    fail(
        "status distribution requires machine-translated=181, "
        f"got {status_counts.get('machine-translated', 0)}"
    )
for status, count in sorted(status_counts.items()):
    if status not in PUBLISHABLE:
        fail(f"non-publishable locale status remains: {status}={count}")

# English canonical notebook is the editable notebook source.
canonical_nb_path = NOTEBOOKS / "Haas_Japanese_Colab_en.ipynb"
if not canonical_nb_path.exists():
    fail("English canonical notebook is missing")
    canonical_nb = {"cells": []}
else:
    canonical_nb = load_json(canonical_nb_path)
meta = canonical_nb.get("metadata", {}).get("haas_ja_colab", {})
if meta.get("canonical_language") != "en":
    fail("English canonical notebook metadata must declare canonical_language=en")
if canonical_nb.get("cells"):
    intro = "".join(canonical_nb["cells"][0].get("source", []))
    if intro.rstrip("\n") != str(en.get("placeholders", {}).get("intro_markdown", "")).rstrip("\n"):
        fail("en intro snapshot differs from canonical notebook")

# Runtime invariants must hold for the canonical notebook.
canonical_code = "\n".join(
    "".join(cell.get("source", []))
    for cell in canonical_nb.get("cells", [])
    if cell.get("cell_type") == "code"
)
for token in (
    'MODEL_ID = "third-intelligence/Haas-ja-v1.0"',
    'TRANSFORMERS_VERSION = "4.57.6"',
    'os.environ["USE_TF"] = "0"',
    'haas_asr.load_model(',
    'haas_asr.transcribe(',
    'split_at_quiet_points(',
    'TIMESTAMP_MODE = "subtitle"',
    'SAVE_OUTPUTS_TO_GOOGLE_DRIVE = False',
    'approximate_chunk_bounds',
):
    if token not in canonical_code:
        fail("canonical notebook missing runtime invariant: " + token)
if "torch.cuda.empty_cache()" in canonical_code:
    fail("canonical notebook must not call torch.cuda.empty_cache() between chunks")

# Final publication requires all 183 notebooks.
notebook_paths = sorted(NOTEBOOKS.glob("Haas_Japanese_Colab_*.ipynb"))
notebook_codes = {
    path.stem.removeprefix("Haas_Japanese_Colab_")
    for path in notebook_paths
}
if notebook_codes != expected_codes:
    fail(
        "notebook set mismatch: "
        f"missing={sorted(expected_codes - notebook_codes)}, "
        f"extra={sorted(notebook_codes - expected_codes)}"
    )
for path in notebook_paths:
    code = path.stem.removeprefix("Haas_Japanese_Colab_")
    if code not in expected_codes:
        continue
    row = load_json(LOCALES / f"{code}.json")
    if row.get("status") not in PUBLISHABLE:
        fail(f"{code}: generated notebook is not publishable")
    if row.get("canonical_source_sha256") != canonical_hash:
        fail(f"{code}: generated notebook locale is stale")
    nb = load_json(path)
    for index, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        try:
            ast.parse(source)
        except SyntaxError as exc:
            fail(f"{code} cell {index}: Python syntax error: {exc}")
        if cell.get("metadata", {}).get("cellView") != "form":
            fail(f"{code} cell {index}: cellView=form required")
        if cell.get("outputs"):
            fail(f"{code} cell {index}: saved output present")
        if cell.get("execution_count") is not None:
            fail(f"{code} cell {index}: execution_count must be null")

# Root README is ja presentation; docs/README contains all other 182 locales.
readme_paths = sorted(READMES.glob("README.*.md"))
readme_codes = {path.name[len("README.") : -len(".md")] for path in readme_paths}
expected_readmes = expected_codes - {ROOT_PRESENTATION}
if readme_codes != expected_readmes:
    fail(
        "localized README set mismatch: "
        f"missing={sorted(expected_readmes - readme_codes)}, "
        f"extra={sorted(readme_codes - expected_readmes)}"
    )
for code in sorted(readme_codes):
    text = (READMES / f"README.{code}.md").read_text(encoding="utf-8")
    expected_link = f"notebooks/Haas_Japanese_Colab_{code}.ipynb"
    if expected_link not in text:
        fail(f"{code}: localized README does not link to its localized notebook")

# Documentation remains Japanese, while its policy must describe English source.
expected_doc_headings = {
    "ARCHITECTURE.md": "# アーキテクチャ",
    "LOCALIZATION_SCOPE.md": "# ローカライズ対象範囲",
    "LOCALIZATION.md": "# ローカライズ保守",
    "LANGUAGES.md": "# ローカライズ対応状況",
}
for name, heading in expected_doc_headings.items():
    path = ROOT / "docs" / name
    if not path.exists():
        fail("missing Japanese documentation: docs/" + name)
        continue
    text = path.read_text(encoding="utf-8")
    if not text.startswith(heading):
        fail(f"docs/{name} must use Japanese policy documentation")
    if not re.search(r"[ぁ-んァ-ヶ一-龯]", text):
        fail(f"docs/{name} must contain Japanese documentation")

active_contract_files = [
    ROOT / "README.md",
    SOURCE_README,
    *sorted((ROOT / "docs").glob("*.md")),
    *sorted((ROOT / "scripts").glob("*.py")),
]
for path in active_contract_files:
    text = path.read_text(encoding="utf-8")
    for token in ("固定" + "109", "110" + "言語", "scope_" + "frozen"):
        if token in text:
            fail(f"obsolete subset contract {token!r} in {path.relative_to(ROOT)}")
    if path.name != "check_repository.py" and "publication_targets.json" in text:
        fail(f"obsolete publication target catalog reference in {path.relative_to(ROOT)}")
    old_sync_token = "sync_from_" + "japanese.py"
    if path.name != "check_repository.py" and old_sync_token in text:
        fail(f"obsolete Japanese canonical sync reference in {path.relative_to(ROOT)}")

translation_helper = (ROOT / "scripts" / "translate_full_locales.py").read_text(encoding="utf-8")
if 'source="ja"' in translation_helper or '"sl": "ja"' in translation_helper:
    fail("translation helper must translate from English canonical source")
if "AZURE_" + "TRANSLATOR_KEY" in translation_helper or "Ocp-Apim-" + "Subscription-Key" in translation_helper:
    fail("translation helper must not require cloud credentials")

# Privacy/secret scan.
secret_patterns = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"[A-Za-z]:" + r"\\Users\\" + r"[^\\\s]+", re.I),
    re.compile("/" + "Users" + r"/[^/\s]+/"),
    re.compile("/" + "home" + r"/[^/\s]+/"),
    re.compile("/" + "mnt" + "/" + "data" + r"(?:/|\\b)"),
    re.compile("/" + "Transcript_projects" + r"(?:/|\\b)"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
]
email_pattern = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
allowed_email_domains = {"example.com"}
text_suffixes = {".py", ".json", ".md", ".yml", ".yaml", ".txt", ".ipynb"}
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    if ".git" in rel.parts or "tests" in rel.parts:
        continue
    if path.suffix not in text_suffixes and path.name not in {".gitignore", ".gitattributes"}:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for pattern in secret_patterns:
        if pattern.search(text):
            fail(f"possible private/secret/local-path data in {rel}")
    for match in email_pattern.finditer(text):
        domain = match.group(0).rsplit("@", 1)[1].lower()
        if domain not in allowed_email_domains:
            fail(f"email address in {rel}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)

print(
    "PASS: Set1=183; canonical=en; root-presentation=ja; locales=183; statuses="
    + json.dumps(dict(sorted(status_counts.items())), ensure_ascii=False)
    + "; notebooks=183; localized READMEs=182; privacy/secret scan=PASS"
)
