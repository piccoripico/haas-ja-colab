from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NB = ROOT / "notebooks" / "Haas_Japanese_Colab_en.ipynb"
README = ROOT / "source" / "README.en.md"
LOCALE = ROOT / "locales" / "en.json"
TEMPLATE = ROOT / "notebook_template" / "Haas_Japanese_Colab.template.ipynb"


def cell_text(cell: dict) -> str:
    return "".join(cell.get("source", []))


def source_lines(text: str) -> list[str]:
    return text.splitlines(keepends=True)


data = json.loads(LOCALE.read_text(encoding="utf-8"))
nb = json.loads(NB.read_text(encoding="utf-8"))
units = data["placeholders"]

# The English notebook and source README are the human-editable canonical sources.
intro = cell_text(nb["cells"][0])
if intro.rstrip("\n") != str(units["intro_markdown"]).rstrip("\n"):
    units["intro_markdown"] = intro

joined = "\n".join(cell_text(cell) for cell in nb["cells"][1:])
missing = [
    key
    for key, value in units.items()
    if key != "intro_markdown" and str(value) not in joined
]
if missing:
    raise RuntimeError(
        "English canonical notebook changed translatable units; "
        "update locales/en.json deliberately: " + ", ".join(missing)
    )

# Derive a language-neutral template from the English canonical notebook.
tpl = json.loads(json.dumps(nb))
tpl["cells"][0]["source"] = ["{{intro_markdown}}"]
for cell in tpl["cells"][1:]:
    text = cell_text(cell)
    for key, value in sorted(
        ((key, value) for key, value in units.items() if key != "intro_markdown"),
        key=lambda item: len(str(item[1])),
        reverse=True,
    ):
        text = text.replace(str(value), "{{" + key + "}}")
    cell["source"] = source_lines(text)

tpl.setdefault("metadata", {}).setdefault("colab", {})["name"] = (
    "Haas_Japanese_Colab_{{LANG}}.ipynb"
)
meta = tpl["metadata"].setdefault("haas_ja_colab", {})
meta["language"] = "{{LANG}}"
meta["canonical_language"] = "en"
TEMPLATE.write_text(
    json.dumps(tpl, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8",
    newline="\n",
)

data["canonical"] = True
data["status"] = "canonical"
data["translation_source"] = "canonical English source"
data["readme_markdown"] = README.read_text(encoding="utf-8")
payload = json.dumps(
    {
        "placeholders": data["placeholders"],
        "readme_markdown": data["readme_markdown"],
    },
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")
new_hash = hashlib.sha256(payload).hexdigest()
old_hash = data.get("canonical_source_sha256")
data["canonical_source_sha256"] = new_hash
LOCALE.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

# Fail closed after English-source changes.
if old_hash != new_hash:
    for path in sorted((ROOT / "locales").glob("*.json")):
        if path.name == "en.json":
            continue
        row = json.loads(path.read_text(encoding="utf-8"))
        row["canonical"] = False
        if row.get("canonical_source_sha256") == new_hash:
            continue
        status = row.get("status")
        if status == "reviewed":
            row["status"] = "stale-reviewed"
        elif status == "machine-translated":
            row["status"] = "stale-machine-translated"
        elif status == "canonical":
            row["status"] = "stale-reviewed"
        path.write_text(
            json.dumps(row, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

print(
    "Synchronized English canonical -> template + en locale snapshot. "
    "canonical_source_sha256=" + new_hash
)
