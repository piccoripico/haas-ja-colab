# Haas Japanese Colab

Google Colab notebook yo guhindura amajwi n'amavidewo y'Ikiyapani mu nyandiko hakoreshejwe Third Intelligence **Haas-ja-v1.0**.

[![Fungura muri Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_rn.ipynb)

## Ibiranga

- **Ku buntu:** Ikorera kuri GPU runtime y'ubuntu ya Google Colab.
- **Japanese ASR:** Ikoresha [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ifise parameters hafi 0.6B yo kumenya imvugo y'Ikiyapani.
- **Iragenda vuba:** Transcription irashobora gukorwa ningoga.
- **Utumenyetso tw'inyandiko:** Model isohora Japanese punctuation yagereranijwe.
- **Timestamps na subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Gutunganya files ndende:** Audio na video files ndende na zo zirashobora gutunganywa.
- **Google Drive support:** Upload files ako kanya canke uzisome muri Google Drive; output ZIP irashobora kubikwa muri Drive iyo ubishatse.
- **Outputs nyinshi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Uko ikoreshwa

1. Hitamwo `INPUT_MODE` muri **1. Settings** hanyuma uhindure izindi settings iyo bikenewe.
2. Hitamwo **Runtime → Run all**.
3. Iyo `INPUT_MODE = "upload"`, hitamwo files muri **2. File selection / Google Drive mount**.
4. Output ZIP ihita download iyo processing irangiye.

## Timestamp modes

- `none`: nta timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files ndende

`CHUNK_SECONDS` igenzura internal chunk duration ikoreshwa kuri files ndende. Values nini zigabanya boundaries kandi zigumana context nyinshi, ariko inference imwe iba iremereye kandi ishobora gukoresha GPU memory nyinshi. Values nto zoroshya inference imwe ariko zigakora boundaries nyinshi, ivyo bikagira ingaruka kuri recognition hafi yaho. Default irasabwa mu bihe vyinshi.

## UI yahinduwe mu ndimi

ASR model ubwayo ni **iy'Ikiyapani gusa**. Localization ya README na Colab UI ikubiyemo **183 active ISO 639 Set 1 languages** zose (deprecated `sh` yakuweho).

English (`en`) ni canonical translation source. Japanese (`ja`) ni reviewed translation kandi ikopororwa kuri repository root nka default `README.md` presentation. Root Japanese README **ntikoreshwa** nka translation source. Izindi locales 181 ni machine-translated zivuye muri English.

## Ibyitonderwa

- Notebook ihagarara imbere ya transcription iyo GPU itabonetse.
- Processing time iterwa n'uburebure bwa input, settings, na GPU Colab yatanze. Ku run ya mbere, NeMo na model hafi 1.23 GB na vyo biradownloadwa.
- Long audio itunganywa mu internal chunks, rero recognition irashobora kugira ikibazo hafi ya chunk boundaries.

## Canonical source na generation

Inkomoko nyamukuru zishobora guhindurwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ni synchronized canonical snapshot. Japanese ibikwa nka reviewed translation muri `locales/ja.json`, kandi README snapshot yayo ikopororwa kuri root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance itandukanye na ordinary CI. Ordinary users na CI ntibakeneye translation credentials.

## Uruhusha

Notebook scaffolding na build/check scripts biri MIT licensed. Third Intelligence model ntisubirwamwo hano kandi igenzurwa na **Apache-2.0**. Third-party dependencies zigumana licenses zazo.
