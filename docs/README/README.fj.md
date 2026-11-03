# Haas Japanese Colab

Na Google Colab notebook me vakadewataka na Japanese audio kei na video ki na text ena Third Intelligence **Haas-ja-v1.0**.

[![Dolava ena Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_fj.ipynb)

## Veika e rawa ni cakava

- **Sega ni saumi:** E cicivaki ena GPU runtime sega ni saumi ni Google Colab.
- **Japanese ASR:** E vakayagataka na [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), e dua na model rauta ni 0.6B-parameter me kilai kina na vosa vaka-Japani.
- **Totolo:** E rawa ni process vakatotolo na transcription.
- **Punctuation:** Na Model e vakarautaka na Japanese punctuation e nanuma ni dodonu.
- **Timestamp kei subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** E rawa talega ni process na audio kei na video file balavu.
- **Google Drive support:** Upload vakadodonu na file se wilika mai Google Drive; e rawa ni save na output ZIP ki Drive ke vinakati.
- **Output e vuqa:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kei ZIP.

## Vakayagataki

1. Digitaka na `INPUT_MODE` ena **1. Settings** ka veisautaka na setting tale eso ke gadrevi.
2. Digitaka na **Runtime → Run all**.
3. Kevaka `INPUT_MODE = "upload"`, digitaka na file ena **2. File selection / Google Drive mount**.
4. Ni sa oti na processing, ena download vakataki koya na output ZIP.

## Timestamp modes

- `none`: sega ni dua na timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File balavu

Na `CHUNK_SECONDS` e lewa na dede ni internal chunk e vakayagataki ena file balavu. Na value levu e vakalailaitaka na boundary ka maroroya e levu na context, ia e bibi cake na inference yadua ka rawa ni vakalevutaka na GPU memory. Na value lailai e vakarawarawataka na inference yadua ia e bulia e levu na boundary, ka rawa ni vakaleqa na recognition volekata na vanua oqori. Ena vuqa na gauna, e vakaturi me vakayagataki na default.

## UI vakavakadewa

Na ASR model vakataki koya e **Japanese-only**. Na README kei na Colab UI localization e kovuta kece na **183 active ISO 639 Set 1 languages** (e sega ni okati kina na deprecated `sh`).

Na English (`en`) na canonical translation source. Na Japanese (`ja`) e reviewed translation ka copy ki na repository root me default `README.md` presentation. Na root Japanese README e **sega ni vakayagataki** me translation source. Na 181 locale tale eso era machine-translated mai English.

## iVakamacala

- Ena cegu na notebook ni bera na transcription ke sega ni tiko na GPU.
- Na processing time e vakatau ena balavu ni input, setting, kei na GPU e solia na Colab. Ena imatai ni run, e download talega na NeMo kei na model rauta ni 1.23 GB.
- Na audio balavu e process ena internal chunks, o koya gona e rawa ni vakaleqai na recognition ena yasana ni chunk boundaries.

## Canonical source kei generation

iVurevure canonical e rawa ni vakadewataki:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Na `locales/en.json` na synchronized canonical snapshot. Na Japanese e maroroi me reviewed translation ena `locales/ja.json`, ka na kena README snapshot e copy ki na root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Na translation maintenance e duidui mai na ordinary CI. Era sega ni gadreva na ordinary users kei CI na translation credentials.

## License

Na notebook scaffolding kei na build/check scripts era MIT licensed. Na Third Intelligence model e sega ni redistributed eke ka muria na **Apache-2.0**. Na third-party dependencies era maroroya na nodra licenses.
