# Haas Japanese Colab

Google Colab notebook ᔭᐸᓃᓯᑐᑦ ᓂᐱᒥᒃ ᐊᔾᔨᓕᐅᕈᑎᒥᓪᓗ ᑎᑎᕋᖅᑕᐅᑎᑦᑎᓂᕐᒧᑦ Third Intelligence **Haas-ja-v1.0** ᐊᑐᖅᖢᒍ.

[![Colab-ᒥ ᒪᑐᐃᕐᓗᒍ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_iu.ipynb)

## ᐱᔪᓐᓇᖅᑕᖏᑦ

- **ᐊᑭᖃᙱᑦᑐᖅ:** Google Colab free GPU runtime-ᒥ ᐊᐅᓚᓲᖅ.
- **ᔭᐸᓃᓯᑐᑦ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ᐊᑐᖅᑐᖅ, 0.6B parameter model ᔭᐸᓃᓯᑐᑦ ᓂᐱᒥᒃ ᑎᑎᕋᖅᑕᐅᑎᑦᑎᓂᕐᒧᑦ.
- **ᓱᒃᑲᔪᖅ:** ᑎᑎᕋᖅᑕᐅᑎᑦᑎᓂᖅ ᓱᒃᑲᔪᒥᒃ ᐱᔭᕇᖅᑕᐅᔪᓐᓇᖅᑐᖅ.
- **ᑎᑎᕋᐅᓯᐅᑉ ᓇᓗᓇᐃᒃᑯᑕᖏᑦ:** Model ᔭᐸᓃᓯᑐᑦ punctuation-ᓂᒃ ᓇᓚᐅᑦᑖᖅᖢᓂ ᓴᖅᑭᑎᑦᑎᓲᖅ.
- **Timestamps ᐊᒻᒪ subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ᐊᑯᓂ files:** ᐊᑯᓂᐅᔪᑦ audio ᐊᒻᒪ video files ᐱᓕᕆᐊᕆᔭᐅᔪᓐᓇᖅᑐᑦ.
- **Google Drive:** Files ᑕᐃᑯᖓ upload-ᒋᓗᒋᑦ ᐅᕝᕙᓘᓐᓃᑦ Google Drive-ᒦᑦᑐᑦ ᐊᑐᕐᓗᒋᑦ; output ZIP ᐱᔪᒪᒍᕕᑦ Drive-ᒧᑦ ᑐᖅᑯᖅᑕᐅᔪᓐᓇᖅᑐᖅ.
- **ᐊᔾᔨᒌᙱᑦᑐᑦ output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ᐊᒻᒪ ZIP.

## ᖃᓄᖅ ᐊᑐᕐᓂᖅ

1. `INPUT_MODE` ᓂᕈᐊᕐᓗᒍ **1. Settings**-ᒥ, ᐊᓯᖏᓪᓗ settings ᐱᔪᒪᔭᕐᓄᑦ ᐋᖅᑭᒋᐊᕐᓗᒋᑦ.
2. **Runtime → Run all** ᓂᕈᐊᕐᓗᒍ.
3. `INPUT_MODE = "upload"`-ᖑᑉᐸᑦ, files ᓂᕈᐊᕐᓗᒋᑦ **2. File selection / Google Drive mount**-ᒥ.
4. ᐱᓕᕆᐊᖅ ᐱᔭᕇᖅᐸᑦ output ZIP ᐃᒻᒥᓂᒃ download-ᒋᔭᐅᓲᖅ.

## Timestamp modes

- `none`: ᐱᕕᒃᓴᒧᑦ timing information-ᖃᙱᑦᑐᖅ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ᐊᑯᓂ files

`CHUNK_SECONDS` ᐊᑯᓂ file internal chunk-ᒥ ᖃᔅᓯᓂᒃ seconds-ᓂᒃ ᐱᓕᕆᔭᐅᓂᖓᓂᒃ ᐋᖅᑭᒃᓱᐃᓲᖅ. Value ᐊᖏᓂᖅᓴᖅ boundaries-ᓂᒃ ᐃᑭᓪᓕᑎᑦᑎᓲᖅ context-ᒥᓪᓗ ᐊᒥᓱᓂᒃ ᑐᖅᑯᐃᓪᓗᓂ, ᑭᓯᐊᓂ inference ᐊᑕᐅᓯᖅ ᐅᖁᒪᐃᓐᓂᖅᓴᐅᓲᖅ GPU memory-ᒥᓪᓗ ᐊᒥᓱᓂᒃ ᐊᑐᕈᓐᓇᖅᖢᓂ. Value ᒥᑭᓂᖅᓴᖅ inference-ᒥᒃ ᐅᖓᓯᙱᑎᑦᑎᓲᖅ, ᑭᓯᐊᓂ boundaries-ᓂᒃ ᐊᒥᓱᓂᒃ ᓴᖅᑭᑎᑦᑎᓲᖅ, recognition-ᓗ ᑕᐃᒃᑯᓇᓂ ᐊᓯᔾᔨᕈᓐᓇᖅᖢᓂ. Default ᐊᒥᓱᓂ ᐱᐅᓂᖅᐹᖑᓲᖅ.

## ᐅᖃᐅᓯᕐᓄᑦ UI

ASR model **ᔭᐸᓃᓯᑐᑦ ᐅᖃᐅᓯᕐᒧᑦ ᑭᓯᐊᓂ** ᐊᑐᖅᑕᐅᔪᖅ. README ᐊᒻᒪ Colab UI localization **183 active ISO 639 Set 1 languages** ᑕᒪᖏᓐᓂᒃ ᐃᓚᖃᖅᑐᖅ (`sh` deprecated-ᖑᒻᒪᑦ ᐃᓚᐅᙱᑦᑐᖅ).

English (`en`) canonical translation source-ᖑᔪᖅ. Japanese (`ja`) reviewed translation-ᖑᔪᖅ, repository root-ᒧᑦ default `README.md`-ᑎᑐᑦ copy-ᒋᔭᐅᓪᓗᓂ. Root Japanese README **translation source-ᖑᙱᑦᑐᖅ**. 181 locales ᐊᓯᖏᑦ English-ᒥᑦ machine-translated-ᖑᔪᑦ.

## ᓇᓗᓇᐃᒃᑯᑕᐃᑦ

- GPU ᐊᑐᐃᓐᓇᐅᙱᑉᐸᑦ notebook transcription ᐱᒋᐊᙱᓐᓂᖓᓂ ᓄᖅᑲᓲᖅ.
- Processing time input-ᐅᑉ ᐊᑯᓂᐅᓂᖓᓂᒃ, settings-ᓂᒃ, Google Colab-ᒥᓗ GPU-ᒥᒃ ᑐᓂᔭᐅᓂᕐᒥᒃ ᐱᔾᔪᑎᖃᖅᑐᖅ. ᓯᕗᓪᓕᕐᒥ run-ᒥ NeMo ᐊᒻᒪ 1.23 GB model download-ᒋᔭᐅᓲᑦ.
- ᐊᑯᓂ audio internal chunks-ᓂ ᐱᓕᕆᔭᐅᓲᖅ, ᑕᐃᒪᐃᒻᒪᑦ chunk boundaries ᖃᓂᒋᔮᓂ recognition ᐊᓯᔾᔨᕈᓐᓇᖅᑐᖅ.

## Canonical source ᐊᒻᒪ generation

ᑐᙵᕕᐅᔪᑦ ᐅᖃᐅᓰᑦ ᐊᓯᔾᔨᖅᑕᐅᔪᓐᓇᖅᑐᑦ:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot-ᖑᔪᖅ. Japanese reviewed translation `locales/ja.json`-ᒥ ᑐᖅᑯᖅᑕᐅᔪᖅ, README snapshot-ᓗ root `README.md`-ᒧᑦ copy-ᒋᔭᐅᓪᓗᓂ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI-ᒥᑦ ᐊᔾᔨᐅᙱᑦᑐᒥᒃ ᐱᓕᕆᐊᖑᔪᖅ. Ordinary users ᐊᒻᒪ CI translation credentials-ᓂᒃ ᐱᔭᕆᐊᖃᙱᑦᑐᑦ.

## License

Notebook scaffolding ᐊᒻᒪ build/check scripts MIT licensed-ᖑᔪᑦ. Third Intelligence model ᐅᕙᓂ redistribute-ᒋᔭᐅᙱᑦᑐᖅ, **Apache-2.0**-ᒧᓪᓗ ᒪᓕᒃᑐᖅ. Third-party dependencies ᐃᒻᒥᓄᑦ licenses-ᓂᒃ ᐱᖃᖅᑐᑦ.
