from __future__ import annotations

import ast
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"
NOTEBOOKS = ROOT / "notebooks"
READMES = ROOT / "docs" / "README"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash() -> str:
    en = load(LOCALES / "en.json")
    payload = json.dumps(
        {"placeholders": en["placeholders"], "readme_markdown": en["readme_markdown"]},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


class EnglishCanonicalMigration(unittest.TestCase):
    def test_authority_roles(self) -> None:
        set1 = load(ROOT / "localization" / "set1_languages.json")
        self.assertEqual(set1["canonical"], "en")

        en = load(LOCALES / "en.json")
        ja = load(LOCALES / "ja.json")
        self.assertTrue(en["canonical"])
        self.assertEqual(en["status"], "canonical")
        self.assertFalse(ja["canonical"])
        self.assertEqual(ja["status"], "reviewed")
        self.assertEqual(en["canonical_source_sha256"], canonical_hash())
        self.assertEqual(ja["canonical_source_sha256"], canonical_hash())
        self.assertIn("English", ja["translation_source"])

    def test_root_readme_is_japanese_presentation_only(self) -> None:
        en = load(LOCALES / "en.json")
        ja = load(LOCALES / "ja.json")
        self.assertEqual(
            (ROOT / "source" / "README.en.md").read_text(encoding="utf-8"),
            en["readme_markdown"],
        )
        self.assertEqual(
            (ROOT / "README.md").read_text(encoding="utf-8"),
            ja["readme_markdown"],
        )
        self.assertNotEqual(en["readme_markdown"], ja["readme_markdown"])

    def test_old_sync_is_removed(self) -> None:
        self.assertFalse((ROOT / "scripts" / "sync_from_japanese.py").exists())
        self.assertTrue((ROOT / "scripts" / "sync_from_english.py").exists())

    def test_noncanonical_payloads_match_current_progress_state(self) -> None:
        en_keys = set(load(LOCALES / "en.json")["placeholders"])
        current_hash = canonical_hash()
        allowed = {"pending", "machine-translated"}
        for path in sorted(LOCALES.glob("*.json")):
            code = path.stem
            if code in {"en", "ja"}:
                continue
            row = load(path)
            self.assertIn(row["status"], allowed, code)
            self.assertIn("English canonical", row["translation_source"], code)
            self.assertEqual(set(row["placeholders"]), en_keys, code)
            if row["status"] == "pending":
                self.assertEqual(row["canonical_source_sha256"], "", code)
                self.assertTrue(all(value == "" for value in row["placeholders"].values()), code)
                self.assertEqual(row["readme_markdown"], "", code)
            else:
                self.assertEqual(row["canonical_source_sha256"], current_hash, code)
                self.assertTrue(all(value.strip() for value in row["placeholders"].values()), code)
                self.assertTrue(row["readme_markdown"].strip(), code)

    def test_progress_build_contains_exactly_fresh_publishable_locales(self) -> None:
        current_hash = canonical_hash()
        expected = {"en"}
        for path in sorted(LOCALES.glob("*.json")):
            code = path.stem
            if code == "en":
                continue
            row = load(path)
            if row["status"] in {"reviewed", "machine-translated"} and row["canonical_source_sha256"] == current_hash:
                expected.add(code)

        notebooks = {
            p.stem.removeprefix("Haas_Japanese_Colab_")
            for p in NOTEBOOKS.glob("Haas_Japanese_Colab_*.ipynb")
        }
        readmes = {
            p.name[len("README."):-len(".md")]
            for p in READMES.glob("README.*.md")
        }
        self.assertEqual(notebooks, expected)
        self.assertEqual(readmes, expected - {"ja"})

    def test_all_generated_publishable_notebooks_have_valid_python(self) -> None:
        for path in sorted(NOTEBOOKS.glob("Haas_Japanese_Colab_*.ipynb")):
            code = path.stem.removeprefix("Haas_Japanese_Colab_")
            nb = load(path)
            for index, cell in enumerate(nb["cells"]):
                if cell.get("cell_type") != "code":
                    continue
                with self.subTest(code=code, cell=index):
                    ast.parse("".join(cell.get("source", [])))

    def test_runtime_invariants_survive_in_en_and_ja(self) -> None:
        for code in ("en", "ja"):
            nb = load(NOTEBOOKS / f"Haas_Japanese_Colab_{code}.ipynb")
            joined = []
            for cell in nb["cells"]:
                if cell.get("cell_type") != "code":
                    continue
                src = "".join(cell.get("source", []))
                ast.parse(src)
                joined.append(src)
                self.assertEqual(cell.get("metadata", {}).get("cellView"), "form")
                self.assertIsNone(cell.get("execution_count"))
                self.assertEqual(cell.get("outputs"), [])
            code_text = "\n".join(joined)
            self.assertIn("haas_asr.load_model(", code_text)
            self.assertIn("haas_asr.transcribe(", code_text)
            self.assertNotIn("torch.cuda.empty_cache()", code_text)
            self.assertIn("SAVE_OUTPUTS_TO_GOOGLE_DRIVE = False", code_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
