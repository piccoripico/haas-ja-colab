# Haas Japanese Colab

Google Colab notebook para i-transcribe ang Japanese audio at video gamit ang Third Intelligence **Haas-ja-v1.0**.

[![Buksan sa Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_tl.ipynb)

## Mga tampok

- **Libre:** Tumatakbo sa libreng GPU runtime ng Google Colab.
- **Japanese ASR:** Gumagamit ng [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), isang model na may humigit-kumulang 0.6B parameters para sa Japanese speech recognition.
- **Mabilis:** Mabilis na mapoproseso ang transcription.
- **Bantas:** Naglalabas ang model ng tinatayang Japanese punctuation.
- **Mga timestamp at subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pagproseso ng mahahabang file:** Maaari ring iproseso ang mahahabang audio at video file.
- **Suporta sa Google Drive:** Direktang mag-upload ng files o basahin ang mga ito mula sa Google Drive; maaaring i-save sa Drive ang output ZIP kung gusto.
- **Maraming output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, at ZIP.

## Paggamit

1. Piliin ang `INPUT_MODE` sa **1. Settings** at ayusin ang iba pang settings kung kailangan.
2. Piliin ang **Runtime → Run all**.
3. Kapag `INPUT_MODE = "upload"`, pumili ng files sa **2. File selection / Google Drive mount**.
4. Awtomatikong mada-download ang output ZIP pagkatapos ng processing.

## Mga mode ng timestamp

- `none`: walang timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Mahahabang file

Kinokontrol ng `CHUNK_SECONDS` ang internal chunk duration na ginagamit sa mahahabang file. Binabawasan ng mas malalaking value ang boundaries at mas maraming context ang napapanatili, ngunit mas mabigat ang bawat inference at maaaring mas gumamit ng GPU memory. Pinapagaan ng mas maliliit na value ang bawat inference ngunit lumilikha ng mas maraming boundaries, na maaaring makaapekto sa recognition sa paligid ng mga puntong iyon. Inirerekomenda ang default sa karamihan ng kaso.

## Nakalokalisang UI

Ang ASR model mismo ay **para lamang sa Japanese**. Saklaw ng localization ng README at Colab UI ang lahat ng **183 active ISO 639 Set 1 languages** (hindi kasama ang deprecated na `sh`).

English (`en`) ang canonical translation source. Ang Japanese (`ja`) ay reviewed translation at kinokopya sa repository root bilang default na `README.md` presentation. Ang root Japanese README ay **hindi** ginagamit bilang translation source. Ang iba pang 181 locales ay machine-translated mula sa English.

## Mga tala

- Hihinto ang notebook bago ang transcription kung walang available na GPU.
- Nakadepende ang processing time sa haba ng input, settings, at GPU na inilaan ng Colab. Sa unang run, dina-download din ang NeMo at ang humigit-kumulang 1.23 GB model.
- Pinoproseso ang mahabang audio sa internal chunks, kaya maaaring maapektuhan ang recognition sa paligid ng chunk boundaries.

## Canonical source at generation

Mga canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Ang `locales/en.json` ang synchronized canonical snapshot. Ang Japanese ay pinananatili bilang reviewed translation sa `locales/ja.json`, at ang README snapshot nito ay kinokopya sa root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Hiwalay ang translation maintenance sa ordinaryong CI. Hindi kailangan ng ordinaryong users at CI ang translation credentials.

## Lisensya

MIT licensed ang Notebook scaffolding at build/check scripts. Hindi muling ipinamamahagi rito ang Third Intelligence model at saklaw ito ng **Apache-2.0**. Pinananatili ng third-party dependencies ang sarili nilang licenses.
