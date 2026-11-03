# Haas Japanese Colab

Google Colab notebook a wɔde Third Intelligence **Haas-ja-v1.0** di dwuma de kyerɛw Japan kasa audio ne video ase.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ak.ipynb)

## Nneɛma a ɛwom

- **Kwa:** Ɛyɛ adwuma wɔ Google Colab free GPU runtime so.
- **Japan ASR:** Ɛde [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) di dwuma, model a ɛwɔ bɛyɛ 0.6B parameter a wɔayɛ ama Japan kasa ahyɛnsode.
- **Ntɛm:** Wobetumi ayɛ transcription no ntɛm.
- **Punctuation:** Model no de Japan punctuation a wɔabu ho akontaa ba.
- **Timestamp ne subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File tenten ho adwuma:** Wobetumi ayɛ audio ne video file tenten nso.
- **Google Drive mmoa:** Upload file tẽẽ anaa kenkan fi Google Drive; wubetumi de output ZIP akɔsie Drive mu.
- **Output ahorow pii:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ne ZIP.

## Sɛnea wɔde di dwuma

1. Paw `INPUT_MODE` wɔ **1. Settings** mu na sesa settings foforo sɛ ɛho hia.
2. Paw **Runtime → Run all**.
3. Sɛ `INPUT_MODE = "upload"` a, paw file wɔ **2. File selection / Google Drive mount** mu.
4. Sɛ processing no wie a, output ZIP no bɛdownload ne ho ara.

## Timestamp mode

- `none`: bere ho nsɛm biara nni hɔ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File tenten

`CHUNK_SECONDS` hwɛ internal chunk bere a wɔde yɛ file tenten. Value kɛse ma boundary no so tew na ɛkora context pii so, nanso ɛma inference biara yɛ den na ebetumi de GPU memory pii adi dwuma. Value ketewa ma inference yɛ hare nanso ɛyɛ boundary pii, a ebetumi aka recognition wɔ saa mmeae no. Mpɛn pii no, default no yɛ nea wɔkamfo kyerɛ.

## UI a wɔayɛ no kasa mu

ASR model no ankasa yɛ **Japan kasa nko ara**. README ne Colab UI localization no kata **ISO 639 Set 1 kasa 183 a ɛreyɛ adwuma nyinaa** so (`sh` a wɔagyae no nka ho).

Borɔfo (`en`) ne canonical translation source. Japan kasa (`ja`) yɛ reviewed translation, na wɔcopy kɔ repository root sɛ default `README.md` presentation. Root Japan README no **wɔmfa nyɛ translation source**. Locale 181 a aka no yɛ machine-translate fi Borɔfo mu.

## Nhyɛso

- Sɛ GPU nni hɔ a, notebook no gyina ansa na transcription afi ase.
- Processing bere gyina input tenten, settings, ne GPU a Colab de ama no so. Run a edi kan no nso download NeMo ne model a ne kɛse bɛyɛ 1.23 GB.
- Wɔyɛ audio tenten wɔ internal chunk mu, enti recognition betumi anya nsunsuanso wɔ chunk boundary ho.

## Canonical source ne generation

Canonical source a wobetumi akyerɛ ase:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yɛ synchronized canonical snapshot. Wɔhwɛ Japan kasa so sɛ reviewed translation wɔ `locales/ja.json` mu, na wɔcopy ne README snapshot kɔ root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yɛ soronko fi ordinary CI ho. Ordinary users ne CI nhia translation credentials.

## Tumi krataa

Notebook scaffolding ne build/check scripts wɔ MIT license ase. Wɔmfa Third Intelligence model no nkyekyɛ bio wɔ ha, na ɛwɔ **Apache-2.0** ase. Third-party dependencies kora wɔn ankasa license so.
