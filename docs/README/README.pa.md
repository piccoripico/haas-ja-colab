# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ਨਾਲ ਜਪਾਨੀ ਆਡੀਓ ਅਤੇ ਵੀਡੀਓ ਨੂੰ ਟ੍ਰਾਂਸਕ੍ਰਾਈਬ ਕਰਨ ਲਈ Google Colab notebook.

[![Colab ਵਿੱਚ ਖੋਲ੍ਹੋ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_pa.ipynb)

## ਖਾਸੀਅਤਾਂ

- **ਮੁਫ਼ਤ:** Google Colab ਦੇ ਮੁਫ਼ਤ GPU runtime ਉੱਤੇ ਚੱਲਦਾ ਹੈ.
- **ਜਪਾਨੀ ASR:** ਜਪਾਨੀ ਬੋਲੀ ਦੀ ਪਛਾਣ ਲਈ ਲਗਭਗ 0.6B parameters ਵਾਲਾ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ਮਾਡਲ ਵਰਤਦਾ ਹੈ.
- **ਤੇਜ਼:** ਟ੍ਰਾਂਸਕ੍ਰਿਪਸ਼ਨ ਤੇਜ਼ੀ ਨਾਲ process ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ.
- **ਵਿਰਾਮ ਚਿੰਨ੍ਹ:** ਮਾਡਲ ਅੰਦਾਜ਼ੇ ਵਾਲੇ ਜਪਾਨੀ ਵਿਰਾਮ ਚਿੰਨ੍ਹ output ਕਰਦਾ ਹੈ.
- **ਟਾਈਮਸਟੈਂਪ ਅਤੇ ਸਬਟਾਈਟਲ:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ਲੰਬੀਆਂ ਫਾਈਲਾਂ ਦੀ processing:** ਲੰਬੀਆਂ audio ਅਤੇ video ਫਾਈਲਾਂ ਨੂੰ ਵੀ process ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ.
- **Google Drive ਸਹਾਇਤਾ:** ਫਾਈਲਾਂ ਸਿੱਧੇ upload ਕਰੋ ਜਾਂ Google Drive ਤੋਂ ਪੜ੍ਹੋ; output ZIP ਨੂੰ ਚੋਣਵਾਂ ਤੌਰ ਤੇ Drive ਵਿੱਚ save ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ.
- **ਕਈ output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ਅਤੇ ZIP.

## ਵਰਤੋਂ

1. **1. Settings** ਵਿੱਚ `INPUT_MODE` ਚੁਣੋ ਅਤੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਹੋਰ settings ਬਦਲੋ.
2. **Runtime → Run all** ਚੁਣੋ.
3. `INPUT_MODE = "upload"` ਨਾਲ **2. File selection / Google Drive mount** ਵਿੱਚ ਫਾਈਲਾਂ ਚੁਣੋ.
4. Processing ਮੁਕਣ ਤੋਂ ਬਾਅਦ output ZIP ਆਪਣੇ ਆਪ download ਹੁੰਦੀ ਹੈ.

## Timestamp ਮੋਡ

- `none`: ਕੋਈ timing ਜਾਣਕਾਰੀ ਨਹੀਂ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ਲੰਬੀਆਂ ਫਾਈਲਾਂ

`CHUNK_SECONDS` ਲੰਬੀਆਂ ਫਾਈਲਾਂ ਲਈ ਵਰਤੇ internal chunk ਦੀ ਮਿਆਦ ਨੂੰ ਕਾਬੂ ਕਰਦਾ ਹੈ. ਵੱਡੀਆਂ values boundaries ਘਟਾ ਕੇ ਹੋਰ context ਰੱਖਦੀਆਂ ਹਨ, ਪਰ ਹਰ inference ਭਾਰੀ ਹੁੰਦੀ ਹੈ ਅਤੇ ਹੋਰ GPU memory ਲੈ ਸਕਦੀ ਹੈ. ਛੋਟੀਆਂ values inference ਹਲਕੀ ਕਰਦੀਆਂ ਹਨ ਪਰ ਹੋਰ boundaries ਬਣਾਉਂਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਉਹਨਾਂ ਥਾਵਾਂ ਨੇੜੇ recognition ਪ੍ਰਭਾਵਿਤ ਹੋ ਸਕਦੀ ਹੈ. ਜ਼ਿਆਦਾਤਰ ਮਾਮਲਿਆਂ ਵਿੱਚ default value ਦੀ ਸਿਫ਼ਾਰਸ਼ ਹੈ.

## ਸਥਾਨਕੀਕ੍ਰਿਤ UI

ASR ਮਾਡਲ ਆਪ **ਸਿਰਫ਼ ਜਪਾਨੀ** ਹੈ. README ਅਤੇ Colab UI localization ਸਾਰੀਆਂ **183 active ISO 639 Set 1 languages** ਨੂੰ cover ਕਰਦਾ ਹੈ (deprecated `sh` ਤੋਂ ਬਿਨਾਂ).

English (`en`) canonical translation source ਹੈ. Japanese (`ja`) reviewed translation ਹੈ ਅਤੇ repository root ਵਿੱਚ default `README.md` presentation ਵਜੋਂ copy ਹੁੰਦੀ ਹੈ. Root Japanese README **translation source ਵਜੋਂ ਨਹੀਂ ਵਰਤੀ ਜਾਂਦੀ**. ਬਾਕੀ 181 locales English ਤੋਂ machine-translated ਹਨ.

## ਨੋਟ

- ਜੇ GPU ਉਪਲਬਧ ਨਾ ਹੋਵੇ ਤਾਂ notebook transcription ਤੋਂ ਪਹਿਲਾਂ ਰੁਕਦੀ ਹੈ.
- Processing time input length, settings, ਅਤੇ Colab ਵੱਲੋਂ ਮਿਲੀ GPU ਉੱਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ. ਪਹਿਲੇ run ਵਿੱਚ NeMo ਅਤੇ ਲਗਭਗ 1.23 GB ਮਾਡਲ ਵੀ download ਹੁੰਦਾ ਹੈ.
- ਲੰਬੀ audio internal chunks ਵਿੱਚ process ਹੁੰਦੀ ਹੈ, ਇਸ ਕਰਕੇ chunk boundaries ਨੇੜੇ recognition ਪ੍ਰਭਾਵਿਤ ਹੋ ਸਕਦੀ ਹੈ.

## Canonical source ਅਤੇ generation

ਅਨੁਵਾਦਯੋਗ canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot ਹੈ. Japanese ਨੂੰ `locales/ja.json` ਵਿੱਚ reviewed translation ਵਜੋਂ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਸਦਾ README snapshot root `README.md` ਵਿੱਚ copy ਹੁੰਦਾ ਹੈ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ਆਮ CI ਤੋਂ ਵੱਖ ਹੈ. ਆਮ users ਅਤੇ CI ਨੂੰ translation credentials ਦੀ ਲੋੜ ਨਹੀਂ.

## ਲਾਇਸੈਂਸ

Notebook scaffolding ਅਤੇ build/check scripts MIT licensed ਹਨ. Third Intelligence ਮਾਡਲ ਇੱਥੇ redistribute ਨਹੀਂ ਕੀਤਾ ਜਾਂਦਾ ਅਤੇ **Apache-2.0** ਅਧੀਨ ਹੈ. Third-party dependencies ਆਪਣੇ licenses ਰੱਖਦੀਆਂ ਹਨ.
