from __future__ import annotations

import ast
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SET1 = ROOT / "localization" / "set1_languages.json"
LOCALES = ROOT / "locales"
NOTEBOOKS = ROOT / "notebooks"
READMES = ROOT / "docs" / "README"
EN_SOURCE_README = ROOT / "source" / "README.en.md"
ROOT_README = ROOT / "README.md"
PUBLISHABLE = {"canonical", "reviewed", "machine-translated"}
EXPECTED_LOCALE_SCHEMA = {
    "language", "english_name", "native_name", "direction", "canonical",
    "status", "translation_source", "canonical_source_sha256",
    "placeholders", "readme_markdown"
}
TEXT_SUFFIXES = {".py", ".json", ".md", ".yml", ".yaml", ".txt", ".ipynb", ".gitignore", ".gitattributes"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def set1_codes() -> list[str]:
    data = load_json(SET1)
    return [row["code"] for row in data["languages"]]


def canonical_hash() -> str:
    en = load_json(LOCALES / "en.json")
    payload = json.dumps(
        {"placeholders": en["placeholders"], "readme_markdown": en["readme_markdown"]},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


class FullSet1Contract(unittest.TestCase):
    def test_active_set1_is_exactly_183_and_english_canonical(self) -> None:
        data = load_json(SET1)
        codes = set1_codes()
        self.assertEqual(data["count"], 183)
        self.assertEqual(len(codes), 183)
        self.assertEqual(len(set(codes)), 183)
        self.assertNotIn("sh", codes)
        self.assertEqual(data["excluded_deprecated"], ["sh"])
        self.assertEqual(data["canonical"], "en")

    def test_publication_universe_is_set1_itself(self) -> None:
        self.assertFalse((ROOT / "localization" / "publication_targets.json").exists())
        expected = set(set1_codes())
        actual = {p.stem for p in LOCALES.glob("*.json")}
        self.assertEqual(actual, expected)

    def test_final_status_distribution(self) -> None:
        rows = {code: load_json(LOCALES / f"{code}.json") for code in set1_codes()}
        self.assertTrue(rows["en"]["canonical"])
        self.assertEqual(rows["en"]["status"], "canonical")
        self.assertFalse(rows["ja"]["canonical"])
        self.assertEqual(rows["ja"]["status"], "reviewed")
        machine = [code for code, row in rows.items() if row.get("status") == "machine-translated"]
        pending_or_stale = [code for code, row in rows.items() if row.get("status") not in PUBLISHABLE]
        self.assertEqual(len(machine), 181)
        self.assertEqual(pending_or_stale, [])

    def test_english_source_and_japanese_root_presentation(self) -> None:
        en = load_json(LOCALES / "en.json")
        ja = load_json(LOCALES / "ja.json")
        self.assertEqual(EN_SOURCE_README.read_text(encoding="utf-8"), en["readme_markdown"])
        self.assertEqual(ROOT_README.read_text(encoding="utf-8"), ja["readme_markdown"])
        self.assertNotEqual(ROOT_README.read_text(encoding="utf-8"), EN_SOURCE_README.read_text(encoding="utf-8"))
        self.assertEqual(en["status"], "canonical")
        self.assertEqual(ja["status"], "reviewed")
        self.assertIn("English", en["translation_source"])
        self.assertIn("English", ja["translation_source"])

    def test_all_locales_are_fresh_and_schema_aligned(self) -> None:
        expected_hash = canonical_hash()
        en = load_json(LOCALES / "en.json")
        expected_keys = set(en["placeholders"])
        for code in set1_codes():
            row = load_json(LOCALES / f"{code}.json")
            self.assertEqual(set(row), EXPECTED_LOCALE_SCHEMA, code)
            self.assertEqual(row["language"], code)
            self.assertEqual(set(row["placeholders"]), expected_keys, code)
            self.assertEqual(row["canonical_source_sha256"], expected_hash, code)

    def test_generated_artifact_counts_and_links(self) -> None:
        codes = set1_codes()
        notebooks = {p.stem.removeprefix("Haas_Japanese_Colab_") for p in NOTEBOOKS.glob("Haas_Japanese_Colab_*.ipynb")}
        readmes = {p.name[len("README."):-len(".md")] for p in READMES.glob("README.*.md")}
        self.assertEqual(notebooks, set(codes))
        self.assertEqual(readmes, set(codes) - {"ja"})
        self.assertEqual(len(notebooks), 183)
        self.assertEqual(len(readmes), 182)
        for code in readmes:
            text = (READMES / f"README.{code}.md").read_text(encoding="utf-8")
            expected = f"notebooks/Haas_Japanese_Colab_{code}.ipynb"
            self.assertIn(expected, text, code)

    def test_notebook_runtime_invariants(self) -> None:
        for path in sorted(NOTEBOOKS.glob("Haas_Japanese_Colab_*.ipynb")):
            nb = load_json(path)
            code_text = []
            for cell in nb["cells"]:
                if cell.get("cell_type") != "code":
                    continue
                source = "".join(cell.get("source", []))
                ast.parse(source)
                code_text.append(source)
                self.assertEqual(cell.get("metadata", {}).get("cellView"), "form", path.name)
                self.assertIsNone(cell.get("execution_count"), path.name)
                self.assertEqual(cell.get("outputs"), [], path.name)
            joined = "\n".join(code_text)
            self.assertIn("haas_asr.load_model(", joined, path.name)
            self.assertIn("haas_asr.transcribe(", joined, path.name)
            self.assertIn('TRANSFORMERS_VERSION = "4.57.6"', joined, path.name)
            self.assertIn('os.environ["USE_TF"] = "0"', joined, path.name)
            self.assertIn("approximate_chunk_bounds", joined, path.name)
            self.assertNotIn("torch.cuda.empty_cache()", joined, path.name)
            self.assertIn("SAVE_OUTPUTS_TO_GOOGLE_DRIVE = False", joined, path.name)

    def test_active_docs_have_no_old_canonical_contract(self) -> None:
        targets = [ROOT / "README.md", EN_SOURCE_README, *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "scripts").glob("*.py"))]
        forbidden = ["Japanese is the canonical source", "日本語正本", "sync_from_japanese.py", "canonical language must be ja"]
        for path in targets:
            text = path.read_text(encoding="utf-8")
            for token in forbidden:
                self.assertNotIn(token, text, f"{token} in {path.relative_to(ROOT)}")

    def test_docs_outside_localized_readmes_are_japanese_policy_docs(self) -> None:
        for path in sorted((ROOT / "docs").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            self.assertRegex(text, r"[ぁ-んァ-ヶ一-龯]", path.name)

    def test_locale_schema_has_no_legacy_metadata_or_fake_translation(self) -> None:
        self.assertFalse((ROOT / "localization" / "publication_targets.json").exists())
        en = load_json(LOCALES / "en.json")
        ja = load_json(LOCALES / "ja.json")
        for code in set1_codes():
            row = load_json(LOCALES / f"{code}.json")
            self.assertEqual(set(row), EXPECTED_LOCALE_SCHEMA, code)
            if code in {"ja", "en"}:
                continue
            self.assertNotEqual(row["placeholders"]["intro_markdown"], en["placeholders"]["intro_markdown"], code)
            self.assertNotEqual(row["placeholders"]["intro_markdown"], ja["placeholders"]["intro_markdown"], code)
            self.assertNotEqual(row["readme_markdown"], en["readme_markdown"], code)
            self.assertNotEqual(row["readme_markdown"], ja["readme_markdown"], code)
            self.assertIn("English", row["translation_source"], code)
            self.assertIn("review recommended", row["translation_source"].lower(), code)

    def test_privacy_and_secret_scan(self) -> None:
        secret_patterns = [
            re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
            re.compile(r"AKIA[0-9A-Z]{16}"),
            re.compile(r"ghp_[A-Za-z0-9]{30,}"),
            re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
            re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.I),
            re.compile(r"/Users/[^/\s]+/"),
            re.compile(r"/home/[^/\s]+/"),
            re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
        ]
        email = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
        allowed_email_suffixes = {"example.com"}
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT)
            if ".git" in rel.parts or "tests" in rel.parts:
                continue
            if path.suffix not in TEXT_SUFFIXES and path.name not in {".gitignore", ".gitattributes"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for pattern in secret_patterns:
                self.assertIsNone(pattern.search(text), f"possible private/secret data in {path.relative_to(ROOT)}")
            for match in email.finditer(text):
                domain = match.group(0).rsplit("@", 1)[1].lower()
                self.assertIn(domain, allowed_email_suffixes, f"email in {path.relative_to(ROOT)}")

    def test_generators_explicitly_write_lf(self) -> None:
        # Windows translates newlines in Path.write_text unless newline is set.
        for script in (
            "build_languages.py",
            "build_notebooks.py",
            "build_readmes.py",
            "sync_from_english.py",
        ):
            tree = ast.parse((ROOT / "scripts" / script).read_text(encoding="utf-8"))
            writes = [
                node for node in ast.walk(tree)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "write_text"
            ]
            self.assertTrue(writes, script)
            for call in writes:
                newline = next(
                    (item.value for item in call.keywords if item.arg == "newline"),
                    None,
                )
                self.assertIsInstance(newline, ast.Constant, f"{script}:{call.lineno}")
                self.assertEqual(newline.value, "\n", f"{script}:{call.lineno}")

    def test_generated_artifacts_use_lf(self) -> None:
        generated = [
            *NOTEBOOKS.glob("Haas_Japanese_Colab_*.ipynb"),
            *READMES.glob("README.*.md"),
            ROOT / "README.md",
            ROOT / "docs" / "LANGUAGES.md",
        ]
        for path in generated:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertNotIn(b"\r\n", path.read_bytes())

    def test_clean_rebuild_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            copy = Path(td) / "repo"
            shutil.copytree(ROOT, copy)
            before = {
                p.relative_to(copy).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for base in (copy / "notebooks", copy / "docs" / "README")
                for p in base.glob("*") if p.is_file()
            }
            before["README.md"] = hashlib.sha256((copy / "README.md").read_bytes()).hexdigest()
            before["docs/LANGUAGES.md"] = hashlib.sha256((copy / "docs" / "LANGUAGES.md").read_bytes()).hexdigest()
            for script in ("build_languages.py", "build_notebooks.py", "build_readmes.py"):
                subprocess.run([sys.executable, str(copy / "scripts" / script)], cwd=copy, check=True, capture_output=True, text=True)
            after = {
                p.relative_to(copy).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for base in (copy / "notebooks", copy / "docs" / "README")
                for p in base.glob("*") if p.is_file()
            }
            after["README.md"] = hashlib.sha256((copy / "README.md").read_bytes()).hexdigest()
            after["docs/LANGUAGES.md"] = hashlib.sha256((copy / "docs" / "LANGUAGES.md").read_bytes()).hexdigest()
            self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
