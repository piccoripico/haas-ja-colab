# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** xoqoysima, Jappan audio kee video faylitte xaagu-gacsa kinni Google Colab notebook.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_aa.ipynb)

## Fayriitte

- **Qasri maleh:** Google Colab qasri maleh GPU runtime addal taamitta.
- **Jappan ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) xoqoysimta; tama Jappan raddi yaaxigeh 0.6B parameter takke model kinni.
- **Sissik:** Xaagu-gacsi sissikuk abam duuda.
- **Maqna-tamaat:** Model Jappan maqna-tamaat qiyaasak baysa.
- **Waqti tamgitte kee subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Dheer faylitte taamisiis:** Dheer audio kee video faylitte kaaduk taamisiisam duuda.
- **Google Drive cateena:** Faylitte beyak upload aba hinnay Google Drive kaak akri; output ZIP faxxi iyyaanah Drive addat dacrisam duuda.
- **Baxaabaxsa le output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kee ZIP.

## Xoqoysima

1. **1. Settings** addal `INPUT_MODE` doori, kaaduk faxxek kalah settings massos.
2. **Runtime → Run all** doori.
3. `INPUT_MODE = "upload"` tekkek **2. File selection / Google Drive mount** addal faylitte doori.
4. Taamisiis gaba kalteek output ZIP isih download takke.

## Timestamp mode

- `none`: waqti oyti mali.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Dheer faylitte

`CHUNK_SECONDS` dheer faylitteh xoqoysima internal chunk waqti xiqsisa. Kaxxa qadditte boundary dagnal xiqsisa kaaduk context dacrissa, kinnih immay inference inkih gibdi xiqsisa kaaduk GPU memory xoqoysima ossam duuda. Xiqqo qadditte inference salphisa kinnih immay boundary mango ginta, tah recognition xiqsima aracal ellecaboh duuda. Mango caalal default faxximta.

## Baaxô afat qindaa’ime UI

ASR model isih **Jappan qangara dubuk** kinni. README kee Colab UI localization **183 active ISO 639 Set 1 qangara** inkih (deprecated `sh` akkuk) xiqsisa.

Ingiliz (`en`) canonical translation source kinni. Jappan (`ja`) reviewed translation kinni kaaduk default `README.md` baxsa repository root fanah copy takke. Root Jappan README **translation source akkuk maxoqoysiminna**. Kalah 181 locale Ingilizik machine-translate takke.

## Qaddow

- GPU mageytimtek notebook transcription naharal soolissa.
- Processing waqti input dheerina, settings, kee Colab kee GPU duddah xiqsima. Naharsi run NeMo kee 1.23 GB model qiyaasak download abta.
- Dheer audio internal chunk addal taamitta, tohih chunk boundary aracal recognition ellecaboh duuda.

## Canonical source kee generation

Canonical translate takke sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot kinni. Jappan `locales/ja.json` addal reviewed translation akkuk dacrisan, isih README snapshot root `README.md` fanah copy takke.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI kaak baxa kinni. Ordinary users kee CI translation credentials faxximta mali.

## License

Notebook scaffolding kee build/check scripts MIT license le. Third Intelligence model tama aracal redistributem mali kaaduk **Apache-2.0** gubal geytima. Third-party dependencies isih license dacrissa.
