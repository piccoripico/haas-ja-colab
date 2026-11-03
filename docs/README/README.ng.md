# Haas Japanese Colab

Google Colab notebook yokunyola mo text audio novideo yOshiJapani pa Third Intelligence **Haas-ja-v1.0**.

[![Patulula mu Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ng.ipynb)

## Omauliko

- **Nayi li free:** Yi longekidha mo free GPU runtime ya Google Colab.
- **ASR yOshiJapani:** Yi longitha [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model yi na parameters dhaa li popepi 0.6B yokumona omapopyo gOshiJapani.
- **Ondjanga:** Transcription oyi vulika okulongeka neendelelo.
- **Omatomelo gonyolo:** Model oyi gandja omatomelo gOshiJapani ga tengenekwa.
- **Timestamps nosubtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Okulongeka omafile malekele:** Audio novideo file malekele oga vulika okulongeka.
- **Google Drive:** Upload omafile pethimbo limwe nenge u ga leshe mo Google Drive; output ZIP oyi vulika okupungulwa mu Drive ngoka wa hala.
- **Output dha yooloka:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Omukalo gwokulongitha

1. Hogolola `INPUT_MODE` mu **1. Settings** nokulundulula settings dhilwe ngele sha pumbiwa.
2. Hogolola **Runtime → Run all**.
3. Ngele `INPUT_MODE = "upload"`, hogolola omafile mu **2. File selection / Google Drive mount**.
4. Output ZIP oyi download-elwa yoye mwene konima yokulongeka.

## Timestamp modes

- `none`: kapu na timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Omafile malekele

`CHUNK_SECONDS` oyi pangela ethimbo lyointernal chunk ya longithwa koma file malekele. Ovalue oinene oyi shona boundaries nokukaleka context oyindji, ihe inference kehe oyi ningi idhigu nokayi vulika okulongitha GPU memory oyindji. Ovalue onshona oyi ningi inference yi pupile ihe oyi ningi boundaries oyindji, naasho osha vulika okukonga recognition popepi naashoka. Default oye ya yambidhidhwa melandulathano lya vulu.

## UI ya tulwa momalaka

ASR model yoyo mwene oye **yOshiJapani ashike**. README na Colab UI localization oyi kwata **omalaka 183 ga active ISO 639 Set 1** agehe (`sh` ya kala ya tegwa po).

Oshiingilisa (`en`) osho canonical translation source. OshiJapani (`ja`) osho reviewed translation nokukopiwa koot root ya repository nga default `README.md`. Root Japanese README **kayi longithwa** nga translation source. Omalocale 181 galwe oga machine-translate okuza mOshiingilisa.

## Omapopyo

- Notebook oyi yima manga transcription ina tameka ngele GPU kayi li po.
- Processing time oyi ya pefimbo lya input, settings, na GPU ya gandjwa ku Colab. Mu run yotango, NeMo na model ya popepi 1.23 GB oyi download-elwa wo.
- Audio ile oyi longekwa mointernal chunks, naasho recognition oyi vulika okukongwa popepi nachunk boundaries.

## Canonical source negeneration

Omithombo dhopamutemo dhi li mokutolokwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` oye synchronized canonical snapshot. OshiJapani oshi pungulwa nga reviewed translation mu `locales/ja.json`, na README snapshot yasho oyi kopiwa ku root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance oyi li ya yooloka noordinary CI. Ordinary users na CI kava pumbi translation credentials.

## License

Notebook scaffolding nabuild/check scripts odhi na MIT license. Third Intelligence model kayi redistributewa mpano nokayi pangelwa ku **Apache-2.0**. Third-party dependencies odhi kaleka licenses dhadho.
