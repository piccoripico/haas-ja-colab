# Haas Japanese Colab

Notebook Google Colab an etingida audio me video dorerin Japan an Third Intelligence **Haas-ja-v1.0**.

[![Ekamawida Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_na.ipynb)

## Omo irou

- **Eab danga:** Eiy jerab mu free GPU runtime an Google Colab.
- **ASR dorerin Japan:** Eiy angow [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model 0.6B parameter ekaramwen an edorer dorerin Japan.
- **Ekamam:** Transcription eiy jerab ekamam.
- **Omo tanda edorer:** Model eiy ongida omo tanda dorerin Japan an eiy etamak.
- **Timestamps me subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File eatamo:** Audio me video file eatamo eiy jerab.
- **Google Drive:** Upload file ewak me read imwin Google Drive; output ZIP eiy rowa mu Drive ngage amwant.
- **Output eoñ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, me ZIP.

## Omo angow

1. Ruwom `INPUT_MODE` mu **1. Settings** me ura settings eoñ ngage eiy aek.
2. Ruwom **Runtime → Run all**.
3. Ngage `INPUT_MODE = "upload"`, ruwom file mu **2. File selection / Google Drive mount**.
4. Output ZIP eiy download ewak engame processing.

## Timestamp modes

- `none`: eab omo information an time.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File eatamo

`CHUNK_SECONDS` eiy idorer durasin internal chunk an file eatamo. Value eñame eiy ekidanga boundaries me rowa context eoñ, wo inference juon eiy adau me eiy angow GPU memory eoñ. Value edik eiy arama inference emam, wo eiy arama boundaries eoñ, me eiy wanga recognition iturin omo jikin. Default eiy emam mu omo case eoñ.

## UI an dorer eoñ

ASR model ewam eiy **dorerin Japan atsin**. Localization an README me Colab UI eiy riñin **183 active ISO 639 Set 1 languages** (`sh` an old eab riñin).

Dorerin Englis (`en`) eiy canonical translation source. Dorerin Japan (`ja`) eiy reviewed translation me copy imwin repository root an default `README.md`. Root Japanese README **eab angow** an translation source. Omo locale 181 eoñ eiy machine-translate imwin Englis.

## Omo note

- Notebook eiy stop mwan transcription ngage GPU eab available.
- Processing time eiy depende an etamo input, settings, me GPU an Colab eiy ongida. Mu first run, NeMo me model 1.23 GB ngang eiy download.
- Audio eatamo eiy jerab mu internal chunks, bwe recognition eiy wanga iturin chunk boundaries.

## Canonical source me generation

Source canonical an dorerin:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` eiy synchronized canonical snapshot. Dorerin Japan eiy rowa an reviewed translation mu `locales/ja.json`, me README snapshot eiy copy an root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance eiy separate imwin ordinary CI. Ordinary users me CI eab aek translation credentials.

## License

Notebook scaffolding me build/check scripts eiy MIT licensed. Third Intelligence model eab redistribute iya me eiy ian **Apache-2.0**. Third-party dependencies eiy rowa omo license irowa.
