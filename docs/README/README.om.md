# Haas Japanese Colab

Google Colab notebook sagalee fi viidiyoo Jaappaanii Third Intelligence **Haas-ja-v1.0** fayyadamuun barruutti jijjiiruuf.

[![Colab keessatti bani](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_om.ipynb)

## Amaloota

- **Bilisa:** Google Colab GPU runtime bilisaa irratti hojjeta.
- **Japanese ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model parameters tilmaamaan 0.6B qabu kan Japanese speech recognition tiif fayyadama.
- **Saffisaa:** Transcription saffisaan adeemsifamuu danda'a.
- **Mallattoolee barreeffamaa:** Model Japanese punctuation tilmaamame baasa.
- **Timestamps fi subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Faayilota dheeraa:** Audio fi video files dheeraan illee adeemsifamuu danda'u.
- **Google Drive support:** Files kallattiin upload godhi ykn Google Drive irraa dubbisi; output ZIP fedhii irratti Drive keessatti kuusamuu danda'a.
- **Outputs hedduu:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, fi ZIP.

## Itti fayyadama

1. `INPUT_MODE` **1. Settings** keessaa filadhu, settings biroo barbaachisaa ta'e sirreessi.
2. **Runtime → Run all** filadhu.
3. Yeroo `INPUT_MODE = "upload"`, files **2. File selection / Google Drive mount** keessaa filadhu.
4. Processing erga xumuramee output ZIP ofumaan download ta'a.

## Timestamp modes

- `none`: timing information hin jiru.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Faayilota dheeraa

`CHUNK_SECONDS` internal chunk duration faayilota dheeraaf fayyadamu to'ata. Values guddaan boundaries hir'isu, context dabalataa eegu, garuu inference tokko tokko ulfaataa godhu, GPU memory usage dabalu danda'a. Values xiqqaan inference salphisu garuu boundaries baay'isu, kunis recognition naannoo sanaa irratti dhiibbaa qabaachuu danda'a. Yeroo baay'ee default gorfama.

## UI naannoome

ASR model mataan isaa **Japanese-only** dha. Localization README fi Colab UI **183 active ISO 639 Set 1 languages** hunda hammata (deprecated `sh` keessaa baafame).

English (`en`) canonical translation source dha. Japanese (`ja`) reviewed translation dha, repository root keessatti default `README.md` presentation ta'ee copy ta'a. Root Japanese README translation source ta'ee **hin fayyadamu**. Locales 181 hafan English irraa machine-translated ta'u.

## Hubachiisa

- GPU yoo hin jirre notebook transcription dura dhaabbata.
- Processing time dheerina input, settings, fi GPU Colab ramade irratti hundaa'a. Run jalqabaa irratti NeMo fi model tilmaamaan 1.23 GB ta'e illee download ta'u.
- Long audio internal chunks keessatti adeemsifama, kanaaf recognition chunk boundaries naannoo irratti dhiibbaa qabaachuu danda'a.

## Canonical source fi generation

Madda kaanoonikaa hiikamu:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot dha. Japanese `locales/ja.json` keessatti reviewed translation ta'ee eegama, README snapshot isaa root `README.md` tti copy ta'a.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI irraa adda dha. Ordinary users fi CI translation credentials hin barbaadan.

## Hayyama

Notebook scaffolding fi build/check scripts MIT licensed dha. Third Intelligence model as keessatti redistribute hin ta'u, **Apache-2.0** jalatti bulmaata. Third-party dependencies licenses isaanii eegu.
