# Haas Japanese Colab

Google Colab notebook ngam transkribude audio e video Japonais e binndol huutoraade Third Intelligence **Haas-ja-v1.0**.

[![Uddit e Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ff.ipynb)

## Fannuji

- **Dokkal:** Ina dogga e GPU runtime dokkal Google Colab.
- **Japanese ASR:** Ina huutora [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model 0.6B-parameter ɗo ɓuri ɓadude ngam Japanese speech recognition.
- **Jaawɗe:** Transcription ina waawi process-de jaawɗe.
- **Punctuation:** Model ɗum ina yaltina Japanese punctuation ɗum waɗi miijooji.
- **Timestamp e subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio e video file juutɗe ina mbaawi process-de.
- **Google Drive support:** Upload file tigi walla jang ɗe e Google Drive; output ZIP ina waawi save-de e Drive so a yiɗi.
- **Outputji keewɗi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, e ZIP.

## Huutoraade

1. Suɓo `INPUT_MODE` e **1. Settings** tee waylu setting goɗɗi so ina sokli.
2. Suɓo **Runtime → Run all**.
3. So `INPUT_MODE = "upload"`, suɓo file e **2. File selection / Google Drive mount**.
4. Caggal processing timmude, output ZIP ina download-a hoore mum.

## Timestamp modes

- `none`: alaa timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File juutɗe

`CHUNK_SECONDS` ina laamu juuteendi internal chunk ɗi huutoraa e file juutɗe. Value mawɗe ina ustina boundary tee joga context ɓurɗo, kono inference kala ina ɓeyda teddugol tee ina waawi huutoraade GPU memory ɓurɗo. Value pamɗe ina hoyna inference kala kono waɗa boundary keewɗe, ɗum ina waawi tampinde recognition e nokkuuji ɗiin. E ko ɓuri heewde, default ɗum ko ko ɓuri moƴƴude.

## UI firotaaɗo

ASR model ɗum tigi ko **Japanese-only**. README e Colab UI localization ina waɗa **183 active ISO 639 Set 1 languages** fof (deprecated `sh` alaa e mum).

English (`en`) ko canonical translation source. Japanese (`ja`) ko reviewed translation tee ina copy-aa to repository root no default `README.md` presentation. Root Japanese README **huwataako** no translation source. Locale 181 goɗɗe ko machine-translated ummoraade e English.

## Tintinooje

- Notebook dartoto hade transcription fuɗɗaade so GPU alaa.
- Processing time ina fawii e juuteendi input, setting, e GPU mo Colab hokkata. E run arande, NeMo e model 1.23 GB ɗo ɓadi ina download-aa kadi.
- Audio juutɗo ina process-aa e internal chunks, ɗum waɗi recognition ina waawi waylude e chunk boundaries.

## Canonical source e generation

Iwdiiji ɗi foti firteede:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ko synchronized canonical snapshot. Japanese ina jogii no reviewed translation e `locales/ja.json`, tee README snapshot mum ina copy-aa to root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ko ko seerti e ordinary CI. Ordinary users e CI soklaa translation credentials.

## License

Notebook scaffolding e build/check scripts ko MIT licensed. Third Intelligence model redistribute-aaka ɗoo tee ko **Apache-2.0** laamii ɗum. Third-party dependencies ina joga licenses mum'en.
