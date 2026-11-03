from __future__ import annotations

import json
from pathlib import Path

from languages import CANONICAL, LANGUAGES

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"
OUT = ROOT / "docs" / "README"
ROOT_PRESENTATION = "ja"
PUBLISHABLE = {"canonical", "reviewed", "machine-translated"}

CANONICAL_ROW = json.loads(
    (LOCALES / f"{CANONICAL}.json").read_text(encoding="utf-8")
)
CANONICAL_HASH = CANONICAL_ROW["canonical_source_sha256"]


def load(code: str) -> dict:
    return json.loads((LOCALES / f"{code}.json").read_text(encoding="utf-8"))


def is_fresh_publishable(row: dict) -> bool:
    return (
        row.get("status") in PUBLISHABLE
        and row.get("canonical_source_sha256") == CANONICAL_HASH
    )



def expected_colab_link(code: str) -> str:
    return (
        "https://colab.research.google.com/github/piccoripico/"
        "haas-ja-colab/blob/main/notebooks/"
        f"Haas_Japanese_Colab_{code}.ipynb"
    )


def readme_for(code: str, row: dict) -> str:
    text = row["readme_markdown"]
    expected = expected_colab_link(code)
    if expected not in text:
        raise RuntimeError(f"{code} locale README has a wrong Colab notebook link")
    return text


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for path in OUT.glob("README.*.md"):
        path.unlink()

    ja = load(ROOT_PRESENTATION)
    if not is_fresh_publishable(ja) or ja.get("status") != "reviewed":
        raise RuntimeError(
            "Japanese root presentation must be a fresh reviewed translation"
        )
    (ROOT / "README.md").write_text(
        readme_for(ROOT_PRESENTATION, ja),
        encoding="utf-8",
        newline="\n",
    )

    count = 1  # root Japanese README
    for code in LANGUAGES:
        if code == ROOT_PRESENTATION:
            continue
        row = load(code)
        if not is_fresh_publishable(row):
            continue
        text = readme_for(code, row)
        (OUT / f"README.{code}.md").write_text(text, encoding="utf-8", newline="\n")
        count += 1

    print(
        f"Published README artifacts: {count}/{len(LANGUAGES)} "
        "(including root Japanese presentation)."
    )


if __name__ == "__main__":
    main()
