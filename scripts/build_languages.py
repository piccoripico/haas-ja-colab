from __future__ import annotations

import json
from pathlib import Path

from languages import LANGUAGES

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"
OUT = ROOT / "docs" / "LANGUAGES.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    lines = [
        "# ローカライズ対応状況",
        "",
        "翻訳正本言語: **英語 (`en`)**。",
        "root README表示: **日本語 (`ja`, reviewed)**。",
        "選定基準: **廃止済み `sh` を除くactive ISO 639 Set 1全183言語**。",
        "完成時の公開対象: **183言語 = 英語正本1 + 日本語レビュー済み1 + その他181言語の英語source機械翻訳**。",
        "",
        "> 音声認識モデル自体は日本語専用です。ここに示す言語はREADMEとColab操作UIの表示をローカライズするもので、文字起こし対象言語を変更するものではありません。",
        "",
        "| コード | 言語名 | 現地語名 | 方向 | 状態 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for code, meta in LANGUAGES.items():
        path = LOCALES / f"{code}.json"
        status = load(path).get("status", "missing") if path.exists() else "missing"
        values = [
            f"`{code}`",
            meta["english_name"],
            meta["native_name"],
            meta["direction"],
            status,
        ]
        values = [str(value).replace("|", "\\|") for value in values]
        lines.append("| " + " | ".join(values) + " |")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Updated docs/LANGUAGES.md ({len(LANGUAGES)} Set1 locales)")


if __name__ == "__main__":
    main()
