# Haas Japanese Colab

Notebook ya Google Colab ya kulemba audio ne video ya Japonais mu text ku di Third Intelligence **Haas-ja-v1.0**.

[![Jula mu Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_lu.ipynb)

## Bintu bikalenga

- **Bwa bulelela:** Isala pa GPU runtime ya bulelela ya Google Colab.
- **ASR ya Japonais:** Isadila [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model wa pene ne 0.6B parameters wa kumanya mulaka wa Japonais.
- **Lubilobilo:** Transcription ikalenga kusalwa lubilo.
- **Bilembo bya kulemba:** Model ipeta bilembo bya Japonais byadi ikana.
- **Timestamps ne subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Kusala ne file bile:** Audio ne video file bile bikalenga kusalwa mpe.
- **Google Drive:** Upload file kudi straight nansha bala ku Google Drive; output ZIP ikalenga kusungibwa ku Drive biwikala ukeba.
- **Output mishindu mingi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ne ZIP.

## Muswelo wa kusadila

1. Sangula `INPUT_MODE` mu **1. Settings** ne shintulula settings ikwabo biwikala idi ya mushinga.
2. Sangula **Runtime → Run all**.
3. Bi `INPUT_MODE = "upload"`, sangula file mu **2. File selection / Google Drive mount**.
4. Output ZIP ikadownload yoyo moko panyima pa processing.

## Timestamp modes

- `none`: kakuena nsangu ya diba.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File bile

`CHUNK_SECONDS` ulombola bule bwa internal chunk busadilwa pa file bile. Value bikole bishasha boundaries ne bisunga context mingi, kadi inference yonso ikala buzitu ne ikalenga kusadila GPU memory mingi. Value bikese bipanga inference yonso iikale pete kadi bipanga boundaries mingi, byakalenga kusambila recognition pa pene ne bikalenge. Default idi ya mushinga mu bilele bingi.

## UI ya milaka

ASR model yoyo moko idi **ya Japonais nkayayo**. Localization ya README ne Colab UI ikwata **milaka 183 ya active ISO 639 Set 1** yonso (`sh` wa kale kawena mu kati to).

Anglais (`en`) idi canonical translation source. Japonais (`ja`) idi translation itangilwe ne ikopibwa ku root ya repository bu default `README.md`. Root Japanese README **kaisadilu** bu translation source. Locale ikwabo 181 idi machine-translated ku Anglais.

## Mambu a kumanya

- Notebook iyemena kumpala kwa transcription bi GPU kayena to.
- Processing time ishingamana ne bule bwa input, settings, ne GPU Google Colab udi wapa. Mu run wa kumpala, NeMo ne model wa pene ne 1.23 GB idownloadiwa mpe.
- Audio bile isalwa mu internal chunks, nanku recognition ikalenga kusambila pa pene ne chunk boundaries.

## Canonical source ne generation

Mishimi mikulu idi ya kukudimuna:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` idi synchronized canonical snapshot. Japonais usungibwa bu reviewed translation mu `locales/ja.json`, ne README snapshot wayo ukopibwa ku root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance idi ya pa nkayayo ne ordinary CI. Ordinary users ne CI kabadi dijinga ne translation credentials to.

## License

Notebook scaffolding ne build/check scripts idi MIT licensed. Third Intelligence model kaibadilui apa to ne ilombolwa ne **Apache-2.0**. Third-party dependencies bisunga licenses byabo.
