# Haas Japanese Colab

Google Colab notebook ya u ṅwala Japanese audio na video sa text nga Third Intelligence **Haas-ja-v1.0**.

[![Vula kha Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ve.ipynb)

## Zwine ya kona

- **Mahala:** I shuma kha GPU runtime ya mahala ya Google Colab.
- **Japanese ASR:** I shumisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ya 0.6B-parameter u ṱoḓou ṱalusa Japanese speech.
- **Nga u ṱavhanya:** Transcription i nga processiwa nga u ṱavhanya.
- **Punctuation:** Model i bvisa Japanese punctuation ye ya humbulela.
- **Timestamp na subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio na video file ndapfu dzi nga processiwa na dzone.
- **Google Drive support:** Upload file nga u livha kana ni dzi vhale kha Google Drive; output ZIP i nga savedzwa kha Drive arali ni tshi funa.
- **Output nnzhi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Kushumisele

1. Nangani `INPUT_MODE` kha **1. Settings** ni shandukise setting dziṅwe arali zwi tshi ṱoḓea.
2. Nangani **Runtime → Run all**.
3. Arali `INPUT_MODE = "upload"`, nangani file kha **2. File selection / Google Drive mount**.
4. Processing musi yo fhela, output ZIP i downloadiwa nga yoṱhe.

## Timestamp modes

- `none`: a hu na timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File ndapfu

`CHUNK_SECONDS` i langa vhulapfu ha internal chunk ine ya shumiswa kha file ndapfu. Value khulwane dzi fhungudza boundary nahone dzi vhulunga context nnzhi, fhedzi inference iṅwe na iṅwe i a lemea nahone i nga shumisa GPU memory nnzhi. Value ṱhukhu dzi ita inference iṅwe na iṅwe i leluwe fhedzi dzi sika boundary nnzhi, zwine zwa nga kwama recognition tsini na fhethu honoho. Kha zwiimo zwinzhi, default i a eletshedzwa.

## UI yo ṱalutshedzwaho

ASR model yone i **Japanese-only**. README na Colab UI localization zwi katela **183 active ISO 639 Set 1 languages** dzoṱhe (deprecated `sh` a i katelwi).

English (`en`) ndi canonical translation source. Japanese (`ja`) ndi reviewed translation nahone i copyiwa kha repository root sa default `README.md` presentation. Root Japanese README **a i shumiswi** sa translation source. Locale dziṅwe 181 ndi machine-translated u bva kha English.

## Notsi

- Notebook i ima transcription i sa athu u thoma arali GPU i siho.
- Processing time i ḓitika nga vhulapfu ha input, setting, na GPU yo ṋewaho nga Colab. Kha run ya u thoma, NeMo na model ya 1.23 GB dzi downloadiwa na dzone.
- Audio ndapfu i processiwa nga internal chunks, ngauralo recognition i nga kwamea tsini na chunk boundaries.

## Canonical source na generation

Zwiko zwa ndeme zwine zwa nga ṱalutshedzwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ndi synchronized canonical snapshot. Japanese i vhulungwa sa reviewed translation kha `locales/ja.json`, nahone README snapshot yayo i copyiwa kha root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yo fhambana na ordinary CI. Ordinary users na CI a vha ṱoḓi translation credentials.

## License

Notebook scaffolding na build/check scripts ndi MIT licensed. Third Intelligence model a i redistributed hafha nahone i langiwa nga **Apache-2.0**. Third-party dependencies dzi vhulunga licenses dzadzo.
