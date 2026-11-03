from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SET1_DATA = json.loads(
    (ROOT / "localization" / "set1_languages.json").read_text(encoding="utf-8")
)
SET1_LANGUAGES = {row["code"]: row for row in SET1_DATA["languages"]}
CANONICAL = SET1_DATA["canonical"]

# The publication universe is exactly active ISO 639 Set 1.
LANGUAGES = SET1_LANGUAGES

assert SET1_DATA["count"] == 183
assert len(LANGUAGES) == 183
assert len(set(LANGUAGES)) == 183
assert SET1_DATA.get("excluded_deprecated") == ["sh"]
assert "sh" not in LANGUAGES
assert CANONICAL == "en"
