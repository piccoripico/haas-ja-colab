from __future__ import annotations

import ast
import copy
import json
from pathlib import Path

from languages import CANONICAL, LANGUAGES

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "notebook_template" / "Haas_Japanese_Colab.template.ipynb"
LOCALES = ROOT / "locales"
OUT = ROOT / "notebooks"
VERSION = (ROOT / "VERSION").read_text().strip()
CANONICAL_ROW = json.loads(
    (LOCALES / f"{CANONICAL}.json").read_text(encoding="utf-8")
)
CANONICAL_HASH = CANONICAL_ROW["canonical_source_sha256"]
PUBLISHABLE = {"reviewed", "machine-translated"}


def text(cell: dict) -> str:
    return "".join(cell.get("source", []))


def lines(value: str) -> list[str]:
    return value.splitlines(keepends=True)


def load(code: str) -> dict:
    return json.loads((LOCALES / f"{code}.json").read_text(encoding="utf-8"))


def render(code: str) -> dict | None:
    if code == CANONICAL:
        return None
    locale = load(code)
    if locale.get("status") not in PUBLISHABLE:
        return None
    if locale.get("canonical_source_sha256") != CANONICAL_HASH:
        return None

    nb = copy.deepcopy(json.loads(TEMPLATE.read_text(encoding="utf-8")))
    placeholders = locale["placeholders"]
    for cell in nb["cells"]:
        source = text(cell).replace("{{LANG}}", code)
        for key, value in placeholders.items():
            token = "{{" + key + "}}"
            source = source.replace(
                '"' + token + '"',
                json.dumps(str(value), ensure_ascii=False),
            )
            source = source.replace(token, str(value))
        cell["source"] = lines(source)
        if cell["cell_type"] == "code":
            ast.parse(source)
            cell.setdefault("metadata", {})["cellView"] = "form"
            cell["execution_count"] = None
            cell["outputs"] = []

    metadata = nb.setdefault("metadata", {})
    metadata["accelerator"] = "GPU"
    metadata.setdefault("colab", {})["name"] = (
        f"Haas_Japanese_Colab_{code}.ipynb"
    )
    project = metadata.setdefault("haas_ja_colab", {})
    project["version"] = VERSION
    project["language"] = code
    project["canonical_language"] = CANONICAL
    return nb


def main() -> None:
    OUT.mkdir(exist_ok=True)
    canonical_name = f"Haas_Japanese_Colab_{CANONICAL}.ipynb"
    if not (OUT / canonical_name).exists():
        raise RuntimeError("English canonical notebook is missing")

    for path in OUT.glob("Haas_Japanese_Colab_*.ipynb"):
        if path.name != canonical_name:
            path.unlink()

    count = 1
    for code in LANGUAGES:
        nb = render(code)
        if nb is None:
            continue
        path = OUT / f"Haas_Japanese_Colab_{code}.ipynb"
        path.write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        count += 1
        print(path.relative_to(ROOT))

    print(
        f"Published notebook artifacts: {count}/{len(LANGUAGES)} "
        f"(including canonical {CANONICAL})."
    )


if __name__ == "__main__":
    main()
