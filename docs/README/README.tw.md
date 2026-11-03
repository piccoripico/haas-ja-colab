# Haas Japanese Colab

Google Colab notebook a ɛde Third Intelligence **Haas-ja-v1.0** kyerɛw Japan audio ne video ma ɛdan text.

[![Bue wɔ Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_tw.ipynb)

## Ne dwumadi

- **Kwa:** Ɛyɛ adwuma wɔ Google Colab GPU runtime a ɛyɛ kwa no so.
- **Japanese ASR:** Ɛde [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) di dwuma, model a ɛwɔ bɛyɛ 0.6B-parameter a ɛde Japanese speech recognition yɛ adwuma.
- **Ntɛm:** Wobetumi aprocess transcription ntɛm.
- **Punctuation:** Model no yi Japanese punctuation a ɛsusuw sɛ ɛfata no adi.
- **Timestamp ne subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio ne video file tenten nso betumi aprocess.
- **Google Drive support:** Upload file tee anaa kenkan fi Google Drive; wubetumi asave output ZIP wɔ Drive sɛ wopɛ.
- **Output pii:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ne ZIP.

## Sɛnea wɔde di dwuma

1. Paw `INPUT_MODE` wɔ **1. Settings** na sesa setting foforo sɛ ɛho hia.
2. Paw **Runtime → Run all**.
3. Sɛ `INPUT_MODE = "upload"` a, paw file wɔ **2. File selection / Google Drive mount**.
4. Processing wie a, output ZIP no download ne ho ara.

## Timestamp modes

- `none`: timing information biara nni hɔ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File tenten

`CHUNK_SECONDS` hwɛ internal chunk tenten a wɔde di dwuma ma file tenten. Value akɛse tew boundary so na ɛkora context pii, nanso inference biara yɛ den na ebetumi de GPU memory pii adi dwuma. Value nketewa ma inference biara yɛ hare nanso ɛyɛ boundary pii, na ɛno betumi aka recognition wɔ mmeae no ho. Mpɛn pii no, default no na ɛyɛ papa.

## UI a wɔakyerɛ ase

ASR model no ara yɛ **Japanese-only**. README ne Colab UI localization ka **183 active ISO 639 Set 1 languages** no nyinaa ho (deprecated `sh` nka ho).

English (`en`) ne canonical translation source. Japanese (`ja`) yɛ reviewed translation na wɔcopy kɔ repository root sɛ default `README.md` presentation. Root Japanese README **wɔmfa nni dwuma** sɛ translation source. Locale 181 a aka no yɛ machine-translated fi English.

## Nhyɛnsode

- Notebook no gyina ansa na transcription ahyɛ ase sɛ GPU nni hɔ.
- Processing time gyina input tenten, setting, ne GPU a Colab de ma no so. Wɔ run a edi kan mu no, NeMo ne model a ɛyɛ bɛyɛ 1.23 GB no nso download.
- Audio tenten process wɔ internal chunks mu, enti recognition betumi asesa wɔ chunk boundaries ho.

## Canonical source ne generation

Fibea titiriw a wobetumi akyerɛ ase:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yɛ synchronized canonical snapshot. Wɔkora Japanese sɛ reviewed translation wɔ `locales/ja.json`, na wɔcopy ne README snapshot kɔ root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yɛ soronko fi ordinary CI. Ordinary users ne CI nhia translation credentials.

## License

Notebook scaffolding ne build/check scripts yɛ MIT licensed. Wɔmmfa Third Intelligence model no nkyɛ ha na **Apache-2.0** na ɛhwɛ so. Third-party dependencies kora wɔn licenses.
