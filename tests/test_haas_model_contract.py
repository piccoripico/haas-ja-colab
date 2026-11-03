from __future__ import annotations

import ast
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NB_DIR = ROOT / "notebooks"


def notebook(code: str) -> dict:
    return json.loads((NB_DIR / f"Haas_Japanese_Colab_{code}.ipynb").read_text(encoding="utf-8"))


class HaasModelContract(unittest.TestCase):
    def test_version_fixed_and_source_repository_complete(self) -> None:
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "v1.0.0")
        self.assertTrue((ROOT / "scripts/build_notebooks.py").exists())
        self.assertTrue((ROOT / "scripts/build_readmes.py").exists())
        self.assertTrue((ROOT / "scripts/sync_from_english.py").exists())
        self.assertEqual(len(list((ROOT / "locales").glob("*.json"))), 183)
        self.assertEqual(len(list(NB_DIR.glob("Haas_Japanese_Colab_*.ipynb"))), 183)
        self.assertTrue((ROOT / "notebook_template/Haas_Japanese_Colab.template.ipynb").exists())
        self.assertFalse((ROOT / "notebook_template/Parakeet_Japanese_Colab.template.ipynb").exists())

    def test_metadata_and_structure(self) -> None:
        for code in ("en", "ja"):
            data = notebook(code)
            self.assertEqual(len(data["cells"]), 8)
            self.assertEqual(data["metadata"]["haas_ja_colab"]["version"], "v1.0.0")
            for cell in data["cells"][1:]:
                ast.parse("".join(cell["source"]))
                self.assertIsNone(cell.get("execution_count"))
                self.assertFalse(cell.get("outputs"))

    def test_official_model_and_no_unavailable_features(self) -> None:
        source = "\n".join("".join(c["source"]) for c in notebook("en")["cells"][1:])
        self.assertIn('MODEL_ID = "third-intelligence/Haas-ja-v1.0"', source)
        self.assertIn('TRANSFORMERS_VERSION = "4.57.6"', source)
        self.assertIn('os.environ["USE_TF"] = "0"', source)
        self.assertIn("haas_asr.load_model(", source)
        self.assertIn("haas_asr.transcribe(", source)
        self.assertIn("split_at_quiet_points(", source)
        self.assertIn('TIMESTAMP_MODE = "subtitle"  # @param ["subtitle", "none"]', source)
        self.assertNotIn('nvidia/parakeet-tdt_ctc-0.6b-ja', source)
        self.assertNotIn("nemo-toolkit[asr]==3.0.0", source)
        self.assertNotIn('DECODER = "CTC"', source)
        self.assertNotIn('"greedy.use_cuda_graph_decoder"', source)
        self.assertIn("approximate_chunk_bounds", source)
        self.assertNotIn("Parakeet_Japanese_ASR_outputs", source)

    def test_localized_readme_feature_markdown_is_well_formed(self) -> None:
        for path in (ROOT / "locales").glob("*.json"):
            row = json.loads(path.read_text(encoding="utf-8"))
            readme = row["readme_markdown"]
            self.assertNotIn("- ** `subtitle`", readme, path.stem)
            self.assertIn("Haas-ja-v1.0", readme, path.stem)

    def test_input_and_zip_cells_preserved(self) -> None:
        a = notebook("en")
        self.assertIn('INPUT_MODE = "upload"', "".join(a["cells"][1]["source"]))
        self.assertIn('google_drive', "".join(a["cells"][2]["source"]))
        self.assertIn('AUTO_DOWNLOAD_ZIP', "".join(a["cells"][7]["source"]))


if __name__ == "__main__":
    unittest.main()
