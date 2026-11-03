# Haas Japanese Colab

Google Colab notebook ꋋꂷ Third Intelligence **Haas-ja-v1.0** ꌌ ꏣꀯꉙꑵꌠ ꌋꆀ ꃅꇭꁱꂷꄻꊿ ꄻꌠꉬ。

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ii.ipynb)

## ꐨꌠ

- **ꎆꃀꀋꐥ:** Google Colab ꆹꎆꃀꀋꐥꌠ GPU runtime ꇬꄻꉆ。
- **ꏣꀯꉙ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ꌌꄻ，ꋋꆹ ꏣꀯꉙꑵꌠ ꁱꂷꄻꊿꂷꄻꌠ 0.6B-parameter ꈎꏅ model ꉬ。
- **ꏦꄻꀘ:** transcription ꆹꃅꈎꃅꄻꉆ。
- **ꁱꂷꏦꌠ:** model ꆹꏣꀯꉙꁱꂷꇬꏦꌠꌌ ꄻꐛꅹ ꄻꎼꌠꄉꅐ。
- **Timestamps ꌋꆀ subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ꅉꀕꃅꀕꌠ ꄻꊿ:** ꉙꑵꌠ ꌋꆀ ꃅꇭꅉꀕꃅꀕꌠꑌ ꄻꉆ。
- **Google Drive ꐨꌠ:** ꅉꀕꌠꆹꋍꄷꅐꄉ upload ꄻꉆ，ꄷꀋꁧ Google Drive ꇬꐥꌠ ꊭꏓꄻꉆ；output ZIP ꑌ Drive ꇬꃅꄉ save ꄻꉆ。
- **Output ꈎꏅ:** TXT、Markdown、JSON、CSV、XLSX、SRT、manifest ꌋꆀ ZIP。

## ꄻꊿꎭꌠ

1. **1. Settings** ꇬ `INPUT_MODE` ꎹ，ꀋꄻꀋꉆꌠ setting ꑌꏦꌠꄻ。
2. **Runtime → Run all** ꎹ。
3. `INPUT_MODE = "upload"` ꄻꄉ，**2. File selection / Google Drive mount** ꇬꅉꀕꎹ。
4. ꄻꊿꆏ output ZIP ꆹꋍꄷꅐꄉ download ꄻ。

## Timestamp mode

- `none`: timing information ꀋꐥ。
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ꅉꀕꃅꀕꌠ

`CHUNK_SECONDS` ꆹ ꅉꀕꃅꀕꌠ internal chunk ꍈꇬꈎꏅꌠ control ꄻ。Value ꃅꀕꌠꆹ boundary ꀋꇈꃅꄻꄉ context ꈎꏅꃅꃅꄻ，ꀋꁧ inference ꋍꂷꆹ ꃅꀕꄉ GPU memory ꑌꈎꏅꃅꄻꉆ。Value ꇬꀋꇈꌠꆹ inference ꉬꇮꃅꄻ，ꀋꁧ boundary ꈎꏅꃅꄻꅹ ꄷꀋꁧ recognition ꌠꇬꐛꀋꉆꐨꐥ。ꈎꏅꌠꇬ default ꌌꄻꌠꃅꐥ。

## ꉙꑵ UI

ASR model ꋍꂷꆹ **ꏣꀯꉙꑵꌠꌌꄻꌠ** ꉬ。README ꌋꆀ Colab UI localization ꆹ **183 active ISO 639 Set 1 languages** ꐯꇯꄻ (`sh` deprecated ꌠ ꀋꐥ)。

English (`en`) ꆹ canonical translation source ꉬ。Japanese (`ja`) ꆹ reviewed translation ꉬ，repository root ꇬ default `README.md` ꃅꄉ copy ꄻ。Root Japanese README ꆹ translation source **ꀋꉬ**。ꉙꑵꆏꁏ 181 locale ꆹ English ꄉ machine-translated ꄻ。

## ꃅꄷꌠ

- GPU ꀋꐥꄉ notebook ꆹ transcription ꄻꀋꇁꌠꇬ stop ꄻ。
- Processing time ꆹ input ꃅꀕꌠ、settings ꌋꆀ Colab GPU ꐨꅿꄉꁏꀕ。ꄻꊿꋍꑍꁢ NeMo ꌋꆀ 1.23 GB ꈎꏅ model ꆹ download ꄻ。
- ꉙꑵꃅꀕꌠꆹ internal chunk ꌌꄻꅹ chunk boundaries ꄷꀋꁧ recognition ꐛꀋꉆꐨꐥ。

## Canonical source ꌋꆀ generation

ꁱꂷꄻꐨꌠꌋꆀꊭꏦꄻꉆꌠꄉꇬ:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ꆹ synchronized canonical snapshot ꉬ。Japanese ꆹ `locales/ja.json` ꇬ reviewed translation ꃅꄉꃅꐥ，ꋌꅿ README snapshot ꆹ root `README.md` ꇬ copy ꄻ。

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ꆹ ordinary CI ꌋꆀꏭꏮꀋꌠꉬ。Ordinary user ꌋꆀ CI ꆹ translation credentials ꀋꑌꌠꑴꌦ。

## License

Notebook scaffolding ꌋꆀ build/check scripts ꆹ MIT licensed ꉬ。Third Intelligence model ꆹ ꅉꋋꇬ redistributed ꀋꄻ，**Apache-2.0** ꌌꄻ。Third-party dependencies ꆹ ꋍꍂꋍꍂꅿ license ꌌꄻ。
