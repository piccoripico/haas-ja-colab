from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINALIZER = ROOT / "scripts" / "finalize_localization.py"


class LocalizationFinalizerContract(unittest.TestCase):
    def test_finalizer_exists_and_is_python(self) -> None:
        self.assertTrue(FINALIZER.exists(), "scripts/finalize_localization.py must exist")
        self.assertEqual(FINALIZER.suffix, ".py")

    def test_plan_is_offline_and_matches_current_repository_state(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(FINALIZER), "--plan", "--json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        data = json.loads(proc.stdout)
        self.assertEqual(data["canonical"], "en")
        self.assertEqual(data["root_presentation"], "ja")
        self.assertEqual(data["translation_targets"], 182)

        locale_dir = ROOT / "locales"
        current_hash = data["canonical_source_sha256"]
        publishable = {"canonical", "reviewed", "machine-translated"}
        expected_pending = []
        for path in sorted(locale_dir.glob("*.json")):
            row = json.loads(path.read_text(encoding="utf-8"))
            if path.stem == "en":
                continue
            if row.get("status") not in publishable or row.get("canonical_source_sha256") != current_hash:
                expected_pending.append(path.stem)
        self.assertEqual(data["pending_codes"], expected_pending)
        self.assertEqual(data["pending_or_stale"], len(expected_pending))
        self.assertEqual(data["publication_ready"], not expected_pending)

    def test_finalizer_has_no_legacy_japanese_canonical_path(self) -> None:
        text = FINALIZER.read_text(encoding="utf-8")
        forbidden = [
            "sync_from_japanese",
            "publication_targets.json",
            'source="ja"',
            'canonical = "ja"',
        ]
        for token in forbidden:
            self.assertNotIn(token, text)

    def test_module_import_does_not_require_translation_dependencies(self) -> None:
        spec = importlib.util.spec_from_file_location("finalizer", FINALIZER)
        self.assertIsNotNone(spec)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        self.assertEqual(
            module.FINAL_ARCHIVE_NAME,
            "haas-ja-colab-v1.0.0-set1-183-en-canonical-final.zip",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
