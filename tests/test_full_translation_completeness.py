from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"

NATURAL_LANGUAGE_PLACEHOLDER_KEYS = {
    "messages.bf16",
    "cell1.section", "cell1.title",
    "settings.filename_contains",
    "cell4.section", "cell4.title",
    "cell5.section", "cell5.title",
    "cell2.section", "cell2.title",
    "settings.input_heading",
    "cell7.section", "cell7.title",
    "settings.subtitle_internal",
    "settings.long_heading",
    "messages.model_loaded", "messages.settings_loaded",
    "messages.model_loading", "messages.selected_files",
}

NATURAL_README_EXACT_LINES = {
    "Canonical translatable sources:",
    "## Localized UI",
    "## Notes",
    "## Usage",
    "## Long files",
}


def load(code: str) -> dict:
    return json.loads((LOCALES / f"{code}.json").read_text(encoding="utf-8"))


def structure_signature(text: str) -> list[str]:
    sig: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            sig.append("blank")
        elif line.startswith("```"):
            sig.append("fence")
        elif line.startswith("#"):
            sig.append("heading:" + str(len(line) - len(line.lstrip("#"))))
        elif re.match(r"^- ", line):
            sig.append("bullet")
        elif re.match(r"^\d+\. ", line):
            sig.append("numbered")
        else:
            sig.append("text")
    return sig




def comment_prefix(value: str) -> str | None:
    if value.startswith("# @markdown"):
        return "# @markdown"
    if value.startswith("# @title"):
        return "# @title"
    if value.startswith("#"):
        return "#"
    return None

def protected_tokens(text: str) -> set[str]:
    tokens = set(re.findall(r"`([^`\n]+)`", text))
    # Colab notebook URLs are intentionally locale-specific and are validated separately.
    for url in re.findall(r"https?://[^)\s]+", text):
        if "colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_" not in url:
            tokens.add(url)
    # Stable file/model/format identifiers that may occur outside backticks.
    for token in [
        "Haas", "Third Intelligence", "Google Colab", "NeMo", "TDT", "CTC",
        "TIMESTAMP_MODE", "CHUNK_SECONDS", "INPUT_MODE", "JSON", "CSV",
        "XLSX", "SRT", "TXT", "ZIP", "Apache-2.0",
    ]:
        if token in text:
            tokens.add(token)
    return tokens


class FullTranslationCompleteness(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.en = load("en")
        cls.codes = sorted(p.stem for p in LOCALES.glob("*.json") if p.stem not in {"en", "ja"})
        cls.en_readme_sig = structure_signature(cls.en["readme_markdown"])
        cls.en_intro_sig = structure_signature(cls.en["placeholders"]["intro_markdown"])
        cls.en_readme_tokens = protected_tokens(cls.en["readme_markdown"])
        cls.en_intro_tokens = protected_tokens(cls.en["placeholders"]["intro_markdown"])

    def test_completed_locales_preserve_code_comments_and_locale_link(self) -> None:
        for code in self.codes:
            row = load(code)
            if row["status"] != "machine-translated":
                continue
            with self.subTest(code=code):
                for key, en_value in self.en["placeholders"].items():
                    prefix = comment_prefix(en_value)
                    if prefix is not None:
                        self.assertTrue(
                            row["placeholders"][key].startswith(prefix),
                            f"{code}:{key} must preserve {prefix!r}",
                        )
                expected_colab = (
                    "https://colab.research.google.com/github/piccoripico/haas-ja-colab/"
                    f"blob/main/notebooks/Haas_Japanese_Colab_{code}.ipynb"
                )
                self.assertIn(expected_colab, row["readme_markdown"])

    def test_all_181_locales_are_full_translations(self) -> None:
        self.assertEqual(len(self.codes), 181)
        for code in self.codes:
            with self.subTest(code=code):
                row = load(code)
                self.assertEqual(row["status"], "machine-translated")
                self.assertIn("English canonical", row["translation_source"])
                self.assertIn("full translation", row["translation_source"].lower())
                self.assertNotIn("memory", row["translation_source"].lower())
                self.assertNotIn("rebase", row["translation_source"].lower())
                self.assertTrue(row["readme_markdown"].strip())
                self.assertEqual(
                    structure_signature(row["readme_markdown"]), self.en_readme_sig,
                    f"README structure differs for {code}",
                )
                self.assertEqual(
                    structure_signature(row["placeholders"]["intro_markdown"]), self.en_intro_sig,
                    f"intro structure differs for {code}",
                )
                self.assertEqual(set(row["placeholders"]), set(self.en["placeholders"]))
                self.assertTrue(all(v.strip() for v in row["placeholders"].values()))
                self.assertTrue(self.en_readme_tokens <= protected_tokens(row["readme_markdown"]))
                self.assertTrue(self.en_intro_tokens <= protected_tokens(row["placeholders"]["intro_markdown"]))
                expected_colab = (
                    "https://colab.research.google.com/github/piccoripico/haas-ja-colab/"
                    f"blob/main/notebooks/Haas_Japanese_Colab_{code}.ipynb"
                )
                self.assertIn(expected_colab, row["readme_markdown"])
                self.assertIn("https://colab.research.google.com/assets/colab-badge.svg", row["readme_markdown"])

    def test_no_locale_reuses_complete_english_natural_language_payload(self) -> None:
        en_readme = self.en["readme_markdown"]
        en_intro = self.en["placeholders"]["intro_markdown"]
        for code in self.codes:
            row = load(code)
            with self.subTest(code=code):
                self.assertNotEqual(row["readme_markdown"], en_readme)
                self.assertNotEqual(row["placeholders"]["intro_markdown"], en_intro)
                for key in NATURAL_LANGUAGE_PLACEHOLDER_KEYS:
                    self.assertNotEqual(
                        row["placeholders"][key],
                        self.en["placeholders"][key],
                        f"{code}:{key} retains English UI natural language",
                    )
                localized_lines = {line.strip() for line in row["readme_markdown"].splitlines()}
                self.assertTrue(
                    NATURAL_README_EXACT_LINES.isdisjoint(localized_lines),
                    f"{code}:README retains English natural-language line(s): "
                    f"{sorted(NATURAL_README_EXACT_LINES & localized_lines)}",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
