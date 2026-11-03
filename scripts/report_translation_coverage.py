from __future__ import annotations
import json
from pathlib import Path
from languages import LANGUAGES, CANONICAL
ROOT=Path(__file__).resolve().parents[1]
statuses={}
for code in LANGUAGES:
    d=json.loads((ROOT/'locales'/f'{code}.json').read_text(encoding='utf-8'))
    st=d.get('status','unknown'); statuses[st]=statuses.get(st,0)+1
print(f'Set1 reference=183; publication locales={len(LANGUAGES)}; translation targets={len(LANGUAGES)-1}; canonical={CANONICAL}')
print(json.dumps(statuses,ensure_ascii=False,sort_keys=True))
