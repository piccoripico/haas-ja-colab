# Haas Japanese Colab

Google Colab ನೋಟ್‌ಬುಕ್, Third Intelligence **Haas-ja-v1.0** ಬಳಸಿ ಜಪಾನೀಸ್ ಆಡಿಯೋ ಮತ್ತು ವೀಡಿಯೊವನ್ನು ಪಠ್ಯಕ್ಕೆ ಪರಿವರ್ತಿಸಲು.

[![Colab ನಲ್ಲಿ ತೆರೆಯಿರಿ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kn.ipynb)

## ವೈಶಿಷ್ಟ್ಯಗಳು

- **ಉಚಿತ:** Google Colab ನ ಉಚಿತ GPU runtime ನಲ್ಲಿ ಚಾಲನೆಯಾಗುತ್ತದೆ.
- **ಜಪಾನೀಸ್ ASR:** ಜಪಾನೀಸ್ ಮಾತು ಗುರುತಿಸಲು ಸುಮಾರು 0.6B parameters ಇರುವ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ಮಾದರಿಯನ್ನು ಬಳಸುತ್ತದೆ.
- **ವೇಗ:** ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಷನ್ ಅನ್ನು ತ್ವರಿತವಾಗಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬಹುದು.
- **ವಿರಾಮಚಿಹ್ನೆಗಳು:** ಮಾದರಿ ಅಂದಾಜಿಸಿದ ಜಪಾನೀಸ್ ವಿರಾಮಚಿಹ್ನೆಗಳನ್ನು ಹೊರಹಾಕುತ್ತದೆ.
- **ಟೈಮ್‌ಸ್ಟ್ಯಾಂಪ್ ಮತ್ತು ಉಪಶೀರ್ಷಿಕೆಗಳು:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ದೀರ್ಘ ಫೈಲ್ ಪ್ರಕ್ರಿಯೆ:** ದೀರ್ಘ ಆಡಿಯೋ ಮತ್ತು ವೀಡಿಯೊ ಫೈಲ್‌ಗಳನ್ನೂ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬಹುದು.
- **Google Drive ಬೆಂಬಲ:** ಫೈಲ್‌ಗಳನ್ನು ನೇರವಾಗಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಅಥವಾ Google Drive ನಿಂದ ಓದಿ; output ZIP ಅನ್ನು ಆಯ್ಕೆಯಾಗಿ Drive ಗೆ ಉಳಿಸಬಹುದು.
- **ಬಹು output ಗಳು:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ಮತ್ತು ZIP.

## ಬಳಕೆ

1. **1. Settings** ನಲ್ಲಿ `INPUT_MODE` ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ಅಗತ್ಯವಿದ್ದರೆ ಇತರೆ settings ಸರಿಹೊಂದಿಸಿ.
2. **Runtime → Run all** ಆಯ್ಕೆ ಮಾಡಿ.
3. `INPUT_MODE = "upload"` ಇದ್ದರೆ **2. File selection / Google Drive mount** ನಲ್ಲಿ ಫೈಲ್‌ಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.
4. ಪ್ರಕ್ರಿಯೆಯ ನಂತರ output ZIP ಸ್ವಯಂಚಾಲಿತವಾಗಿ download ಆಗುತ್ತದೆ.

## Timestamp modes

- `none`: ಸಮಯದ ಮಾಹಿತಿ ಇಲ್ಲ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ದೀರ್ಘ ಫೈಲ್‌ಗಳು

`CHUNK_SECONDS` ದೀರ್ಘ ಫೈಲ್‌ಗಳಿಗೆ ಬಳಸುವ internal chunk ಅವಧಿಯನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ದೊಡ್ಡ values boundaries ಕಡಿಮೆ ಮಾಡಿ ಹೆಚ್ಚು context ಉಳಿಸಿಕೊಳ್ಳುತ್ತವೆ, ಆದರೆ ಪ್ರತಿಯೊಂದು inference ಭಾರವಾಗುತ್ತದೆ ಮತ್ತು ಹೆಚ್ಚು GPU memory ಬಳಸಬಹುದು. ಸಣ್ಣ values ಪ್ರತಿಯೊಂದು inference ಅನ್ನು ಹಗುರಗೊಳಿಸುತ್ತವೆ ಆದರೆ ಹೆಚ್ಚು boundaries ರಚಿಸುತ್ತವೆ, ಇದರಿಂದ ಆ ಬಿಂದುಗಳ ಸುತ್ತ recognition ಪ್ರಭಾವಿತರಾಗಬಹುದು. ಹೆಚ್ಚಿನ ಸಂದರ್ಭಗಳಲ್ಲಿ default value ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ.

## ಸ್ಥಳೀಕರಿಸಿದ UI

ASR model ಸ್ವತಃ **ಜಪಾನೀಸ್‌ಗೆ ಮಾತ್ರ**. README ಮತ್ತು Colab UI localization **ISO 639 Set 1 ರ ಎಲ್ಲಾ 183 ಸಕ್ರಿಯ ಭಾಷೆಗಳನ್ನು** ಒಳಗೊಂಡಿದೆ (deprecated `sh` ಹೊರತುಪಡಿಸಿ).

ಇಂಗ್ಲಿಷ್ (`en`) canonical translation source. ಜಪಾನೀಸ್ (`ja`) reviewed translation ಆಗಿದ್ದು default `README.md` presentation ಆಗಿ repository root ಗೆ copy ಆಗುತ್ತದೆ. root ನ ಜಪಾನೀಸ್ README **translation source ಆಗಿ ಬಳಸಲಾಗುವುದಿಲ್ಲ**. ಇತರೆ 181 locales ಇಂಗ್ಲಿಷ್‌ನಿಂದ machine-translated ಆಗುತ್ತವೆ.

## ಟಿಪ್ಪಣಿಗಳು

- GPU ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ notebook transcription ಗಿಂತ ಮೊದಲು ನಿಲ್ಲುತ್ತದೆ.
- Processing time input length, settings ಮತ್ತು Colab ನೀಡಿದ GPU ಮೇಲೆ ಅವಲಂಬಿತ. ಮೊದಲ run ನಲ್ಲಿ NeMo ಮತ್ತು ಸುಮಾರು 1.23 GB model ಕೂಡ download ಆಗುತ್ತದೆ.
- ದೀರ್ಘ audio ಅನ್ನು internal chunks ನಲ್ಲಿ process ಮಾಡಲಾಗುತ್ತದೆ, ಆದ್ದರಿಂದ chunk boundaries ಸುತ್ತ recognition ಪ್ರಭಾವಿತರಾಗಬಹುದು.

## Canonical source ಮತ್ತು generation

ಅನುವಾದಿಸಬಹುದಾದ ಅಧಿಕೃತ ಮೂಲಗಳು:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot ಆಗಿದೆ. ಜಪಾನೀಸ್ `locales/ja.json` ನಲ್ಲಿ reviewed translation ಆಗಿ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಅದರ README snapshot ಅನ್ನು root `README.md` ಗೆ copy ಮಾಡಲಾಗುತ್ತದೆ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ಸಾಮಾನ್ಯ CI ಯಿಂದ ಪ್ರತ್ಯೇಕವಾಗಿದೆ. ಸಾಮಾನ್ಯ users ಮತ್ತು CI ಗೆ translation credentials ಅಗತ್ಯವಿಲ್ಲ.

## ಪರವಾನಗಿ

Notebook scaffolding ಮತ್ತು build/check scripts MIT ಪರವಾನಗಿಯಲ್ಲಿವೆ. Third Intelligence model ಅನ್ನು ಇಲ್ಲಿ ಮರುಹಂಚಿಕೆ ಮಾಡಲಾಗುವುದಿಲ್ಲ ಮತ್ತು ಇದು **Apache-2.0** ಅಡಿಯಲ್ಲಿ ಇದೆ. Third-party dependencies ತಮ್ಮದೇ ಪರವಾನಗಿಗಳನ್ನು ಉಳಿಸಿಕೊಳ್ಳುತ್ತವೆ.
