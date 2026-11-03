# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** භාවිතයෙන් ජපන් audio සහ video පිටපත් කිරීමට Google Colab notebook එකක්.

[![Colab හි විවෘත කරන්න](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_si.ipynb)

## විශේෂාංග

- **නොමිලේ:** Google Colab හි නොමිලේ GPU runtime එක මත ධාවනය වේ.
- **ජපන් ASR:** ජපන් කථනය හඳුනාගැනීමට පරාමිතීන් 0.6B පමණ ඇති [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) model එක භාවිතා කරයි.
- **වේගවත්:** Transcription ඉක්මනින් process කළ හැක.
- **විරාම ලකුණු:** Model එක අනුමාන කළ ජපන් punctuation output කරයි.
- **Timestamps සහ subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **දිගු file processing:** දිගු audio සහ video files ද process කළ හැක.
- **Google Drive සහාය:** Files සෘජුව upload කරන්න හෝ Google Drive වෙතින් කියවන්න; output ZIP එක කැමති නම් Drive හි save කළ හැක.
- **Output කිහිපයක්:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, සහ ZIP.

## භාවිතය

1. **1. Settings** තුළ `INPUT_MODE` තෝරා අවශ්‍ය නම් වෙනත් settings සකස් කරන්න.
2. **Runtime → Run all** තෝරන්න.
3. `INPUT_MODE = "upload"` නම් **2. File selection / Google Drive mount** තුළ files තෝරන්න.
4. Processing අවසන් වූ පසු output ZIP එක ස්වයංක්‍රීයව download වේ.

## Timestamp modes

- `none`: කාල තොරතුරු නැත.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## දිගු files

`CHUNK_SECONDS` දිගු files සඳහා භාවිතා වන internal chunk කාලය පාලනය කරයි. විශාල values boundaries අඩු කර වැඩි context තබන නමුත් එක් එක් inference එක බර වැඩි වී වැඩි GPU memory භාවිතා කළ හැක. කුඩා values inference එක පහසු කරයි නමුත් වැඩි boundaries ඇති කරයි; ඒවා අසල recognition බලපෑමට ලක් විය හැක. බොහෝ අවස්ථාවල default value එක නිර්දේශිතය.

## දේශීයකරණය කළ UI

ASR model එක **ජපන් පමණි**. README සහ Colab UI localization සියලු **183 active ISO 639 Set 1 languages** ආවරණය කරයි (deprecated `sh` හැර).

English (`en`) canonical translation source එකයි. Japanese (`ja`) reviewed translation එකක් වන අතර repository root හි default `README.md` presentation ලෙස copy වේ. Root Japanese README එක **translation source එකක් ලෙස භාවිත නොවේ**. ඉතිරි 181 locales English වෙතින් machine-translated වේ.

## සටහන්

- GPU නොමැති නම් notebook එක transcription ට පෙර නවතී.
- Processing time input length, settings සහ Colab මඟින් ලබා දෙන GPU අනුව වෙනස් වේ. පළමු run එකේ NeMo සහ 1.23 GB පමණ model එකද download වේ.
- දිගු audio internal chunks ලෙස process වන නිසා chunk boundaries අසල recognition බලපෑමට ලක් විය හැක.

## Canonical source සහ generation

පරිවර්තනය කළ හැකි canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot එකයි. Japanese `locales/ja.json` තුළ reviewed translation ලෙස පවත්වාගෙන යන අතර එහි README snapshot එක root `README.md` වෙත copy කරයි.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance සාමාන්‍ය CI වෙතින් වෙනමයි. සාමාන්‍ය users සහ CI සඳහා translation credentials අවශ්‍ය නැත.

## License

Notebook scaffolding සහ build/check scripts MIT licensed වේ. Third Intelligence model එක මෙහි redistribute නොකරන අතර **Apache-2.0** යටතේ පාලනය වේ. Third-party dependencies තමන්ගේ licenses පවත්වා ගනී.
