# Haas Japanese Colab

Google Colab notebook yokunyola mo text audio novideo yOshiJapani tashi longifa Third Intelligence **Haas-ja-v1.0**.

[![Patulula mu Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kj.ipynb)

## Oinima tai dulu

- **Free:** Oi longekida mu free GPU runtime ya Google Colab.
- **ASR yOshiJapani:** Oi longifa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ina parameters di li popepi 0.6B yokudidilika omapopyo OshiJapani.
- **Tashi ende nawa:** Transcription oya dulu okulongekwa nombili.
- **Oimanyifo yokunyola:** Model oya pita oimanyifo yOshiJapani ya tengenekwa.
- **Timestamps nosubtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Okulonga omafile male:** Audio novideo file male oga dulu okulongekwa.
- **Google Drive:** Upload omafile pethimbo limwe ile u ga lese mo Google Drive; output ZIP oya dulu okupungulwa mu Drive nge wa hala.
- **Output di lili:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Omukalo wokulongifa

1. Hoolola `INPUT_MODE` mu **1. Settings** nohendulula settings dikwao nge sha pumbiwa.
2. Hoolola **Runtime → Run all**.
3. Nge `INPUT_MODE = "upload"`, hoolola omafile mu **2. File selection / Google Drive mount**.
4. Output ZIP oya downloadwa yoyo vene konima yokulongeka.

## Timestamp modes

- `none`: kape na timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Omafile male

`CHUNK_SECONDS` oya pangela efimbo lointerna chunk la longifwa koma file male. Ovalue inene oya shuna boundaries noya kaleka context inji, ndele inference keshe oya ninga idjuu noya dulu okulongifa GPU memory inji. Ovalue ishona oya ninga inference i dule, ndele oya ninga boundaries inji, oyo ya dulu okuponga recognition popepi naayo. Default oya yambididwa moinima inji.

## UI ya tulwa momalaka

ASR model yoyo vene **yOshiJapani ashike**. README na Colab UI localization oya kwata **omalaka 183 ga active ISO 639 Set 1** agehe (`sh` ya kulupa kaya kwatwa).

Oshiingilisa (`en`) osho canonical translation source. OshiJapani (`ja`) osho reviewed translation nokukopiwa ku root ya repository nga default `README.md`. Root Japanese README **kayi longifwa** nga translation source. Omalocale 181 makwao oga machine-translate okuza mOshiingilisa.

## Omapopyo

- Notebook oya yema manga transcription ina tameka nge GPU kayi li po.
- Processing time oya dependeka koure woinput, settings, na GPU ya gandjwa ku Colab. Mu run yotete, NeMo na model ya popepi 1.23 GB oya downloadwa wo.
- Audio ile oya longekwa mointernal chunks, naasho recognition oya dulu okupongwa popepi nachunk boundaries.

## Canonical source negeneration

Omithombo dhopamutemo dhi li mokutolokwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` oye synchronized canonical snapshot. OshiJapani osha pungulwa nga reviewed translation mu `locales/ja.json`, na README snapshot yasho oya kopiwa ku root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance oya yooloka noordinary CI. Ordinary users na CI kava pumbi translation credentials.

## License

Notebook scaffolding nabuild/check scripts odi na MIT license. Third Intelligence model kai redistributewa apa noya pangelwa ku **Apache-2.0**. Third-party dependencies oda kaleka licenses dado.
