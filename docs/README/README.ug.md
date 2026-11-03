# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ئارقىلىق ياپونچە ئاۋاز ۋە ۋىدىيونى تېكىستكە ئايلاندۇرۇش ئۈچۈن Google Colab notebook.

[![Colab دا ئېچىڭ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ug.ipynb)

## ئىقتىدارلار

- **ھەقسىز:** Google Colab نىڭ ھەقسىز GPU runtime ىدا ئىشلەيدۇ.
- **ياپونچە ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) نى ئىشلىتىدۇ؛ بۇ ياپونچە سۆزلەشنى تونۇش ئۈچۈن تەخمىنەن 0.6B-parameter model.
- **تېز:** Transcription نى تېز بىر تەرەپ قىلغىلى بولىدۇ.
- **تىنىش بەلگىلىرى:** Model مۆلچەرلەنگەن ياپونچە punctuation نى چىقىرىدۇ.
- **Timestamp ۋە subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ئۇزۇن file بىر تەرەپ قىلىش:** ئۇزۇن audio ۋە video file لارنىمۇ بىر تەرەپ قىلغىلى بولىدۇ.
- **Google Drive قوللاش:** File نى بىۋاسىتە upload قىلىڭ ياكى Google Drive دىن ئوقۇڭ؛ output ZIP نى خالىسا Drive غا save قىلغىلى بولىدۇ.
- **كۆپ خىل output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ۋە ZIP.

## ئىشلىتىش

1. **1. Settings** ئىچىدە `INPUT_MODE` نى تاللاپ، زۆرۈر بولسا باشقا setting لارنى تەڭشەڭ.
2. **Runtime → Run all** نى تاللاڭ.
3. `INPUT_MODE = "upload"` بولسا **2. File selection / Google Drive mount** ئىچىدە file تاللاڭ.
4. Processing تاماملانغاندىن كېيىن output ZIP ئاپتوماتىك download بولىدۇ.

## Timestamp mode لىرى

- `none`: timing information يوق.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ئۇزۇن file لار

`CHUNK_SECONDS` ئۇزۇن file ئۈچۈن ئىشلىتىلىدىغان internal chunk نىڭ داۋاملىشىش ۋاقتىنى كونترول قىلىدۇ. چوڭ value boundary نى ئازايتىپ تېخىمۇ كۆپ context نى ساقلايدۇ، بىراق ھەر بىر inference ئېغىرلىشىپ GPU memory ئىشلىتىشنى ئاشۇرۇشى مۇمكىن. كىچىك value ھەر بىر inference نى يېنىكلىتىدۇ، بىراق تېخىمۇ كۆپ boundary ھاسىل قىلىپ شۇ جايلار ئەتراپىدىكى recognition غا تەسىر قىلىشى مۇمكىن. كۆپىنچە ئەھۋالدا default تەۋسىيە قىلىنىدۇ.

## يەرلىكلەشتۈرۈلگەن UI

ASR model ئۆزى **Japanese-only**. README ۋە Colab UI localization بارلىق **183 active ISO 639 Set 1 languages** نى قاپلايدۇ (deprecated `sh` چىقىرىۋېتىلگەن).

English (`en`) canonical translation source. Japanese (`ja`) reviewed translation بولۇپ، default `README.md` presentation سۈپىتىدە repository root قا copy قىلىنىدۇ. Root Japanese README translation source سۈپىتىدە **ئىشلىتىلمەيدۇ**. قالغان 181 locale English تىن machine-translated قىلىنغان.

## ئىزاھات

- GPU بولمىسا notebook transcription دىن بۇرۇن توختايدۇ.
- Processing time input ئۇزۇنلۇقى، setting ۋە Colab تەقسىملىگەن GPU غا باغلىق. بىرىنچى run دا NeMo ۋە تەخمىنەن 1.23 GB model مۇ download بولىدۇ.
- ئۇزۇن audio internal chunk لاردا بىر تەرەپ قىلىنىدۇ، شۇڭا chunk boundary ئەتراپىدا recognition تەسىرگە ئۇچرىشى مۇمكىن.

## Canonical source ۋە generation

Canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot. Japanese `locales/ja.json` ئىچىدە reviewed translation سۈپىتىدە ساقلىنىدۇ، ئۇنىڭ README snapshot ى root `README.md` غا copy قىلىنىدۇ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ئادەتتىكى CI دىن ئايرىم. ئادەتتىكى user ۋە CI غا translation credential لازىم ئەمەس.

## License

Notebook scaffolding ۋە build/check script MIT licensed. Third Intelligence model بۇ يەردە قايتا تارقىتىلمايدۇ ۋە **Apache-2.0** بويىچە باشقۇرۇلىدۇ. Third-party dependency ئۆز license لىرىنى ساقلايدۇ.
