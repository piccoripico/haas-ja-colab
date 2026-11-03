# Haas Japanese Colab

Google Colab notebook for transcribing Japanese audio and video with Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_en.ipynb)

## Features

- **Free:** Runs on Google Colab's free GPU runtime.
- **Japanese ASR:** Uses [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), an approximately 0.6B-parameter model for Japanese speech recognition.
- **Fast:** Transcription can be processed quickly.
- **Punctuation:** The model outputs estimated Japanese punctuation.
- **Timestamps and subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Long audio and video files can also be processed.
- **Google Drive support:** Upload files directly or read them from Google Drive; the output ZIP can optionally be saved to Drive.
- **Multiple outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, and ZIP.

## Usage

1. Choose `INPUT_MODE` in **1. Settings** and adjust other settings if needed.
2. Select **Runtime → Run all**.
3. With `INPUT_MODE = "upload"`, choose files in **2. File selection / Google Drive mount**.
4. The output ZIP is downloaded automatically after processing.

## Timestamp modes

- `none`: no timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Long files

`CHUNK_SECONDS` controls the internal chunk duration used for long files. Larger values reduce boundaries and preserve more context, but make each inference heavier and may increase GPU memory use. Smaller values make each inference lighter but create more boundaries, which can affect recognition around those points. The default is recommended in most cases.

## Localized UI

The ASR model itself is **Japanese-only**. README and Colab UI localization covers all **183 active ISO 639 Set 1 languages** (deprecated `sh` excluded).

English (`en`) is the canonical translation source. Japanese (`ja`) is a reviewed translation and is copied to the repository root as the default `README.md` presentation. The root Japanese README is **not** used as a translation source. The other 181 locales are machine-translated from English.

## Notes

- The notebook stops before transcription if a GPU is unavailable.
- Processing time depends on input length, settings, and the GPU assigned by Colab. The first run also downloads NeMo and the approximately 1.23 GB model.
- Long audio is processed in internal chunks, so recognition can be affected around chunk boundaries.

## Canonical source and generation

Canonical translatable sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` is the synchronized canonical snapshot. Japanese is maintained as a reviewed translation in `locales/ja.json`, and its README snapshot is copied to root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance is separate from ordinary CI. Ordinary users and CI do not need translation credentials.

## License

Notebook scaffolding and build/check scripts are MIT licensed. The Third Intelligence model is not redistributed here and is governed by **Apache-2.0**. Third-party dependencies retain their own licenses.
