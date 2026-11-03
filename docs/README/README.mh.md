# Haas Japanese Colab

Google Colab notebook ñan jejeik audio im video ilo kajin Japan kin Third Intelligence **Haas-ja-v1.0**.

[![Kwalok ilo Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_mh.ipynb)

## Men ko ej maroñ kōmmane

- **Ejjeļok wonen:** Ej jerbal ilo free GPU runtime an Google Colab.
- **ASR an kajin Japan:** Ej kōjerbal [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), juon model eo ewōr ippān 0.6B parameter ñan kile kajin Japan.
- **Mōkaj:** Transcription emaroñ jerbal mōkaj.
- **Kōjjelā in jeje:** Model eo ej kwalok kōjjelā in jeje an kajin Japan ko ej lemnak rejimwe.
- **Timestamps im subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Jerbal file ko aetok:** Audio im video file ko aetok emaroñ bar jerbal.
- **Google Drive:** Upload file ko kajjojo ak riiti jen Google Drive; output ZIP emaroñ save ilo Drive ñe kwōj kōnaan.
- **Output ko jiluḷu:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, im ZIP.

## Wāween kōjerbal

1. Kelet `INPUT_MODE` ilo **1. Settings** im ukot settings ko jet ñe aikuj.
2. Kelet **Runtime → Run all**.
3. Ñe `INPUT_MODE = "upload"`, kelet file ko ilo **2. File selection / Google Drive mount**.
4. Output ZIP ej download make ilo kōjota in jerbal.

## Timestamp modes

- `none`: ejjeļok melele in ien.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File ko aetok

`CHUNK_SECONDS` ej tōl aetok in internal chunk eo rej kōjerbale ñan file ko aetok. Value ko elap rej kōmman boundary ko dikļọk im kejbarok context lapļọk, ak kajjojo inference ej eddoļọk im emaroñ kōjerbal GPU memory lapļọk. Value ko edik rej kōmman inference ejjab eddo, ak rej kōmman boundary ko lapļọk, im men in emaroñ jelet recognition iturin jikin kein. Default eo ej emman ilo elōñ case.

## UI eo emōj ukote

ASR model eo make ej **kajin Japan wōt**. README im Colab UI localization ej koba aolep **183 active ISO 639 Set 1 languages** (`sh` eo etto ejjab koba).

Kajin Pālle (`en`) ej canonical translation source. Kajin Japan (`ja`) ej reviewed translation im rej copy e ñan root in repository einwōt default `README.md`. Root Japanese README **ejjab kōjerbal** einwōt translation source. Locale ko jet 181 rej machine-translate jen kajin Pālle.

## Kōjjelā ko

- Notebook eo ej bōjrak mokta jen transcription ñe GPU ejjab bellok.
- Processing time ej ekkar ñan aetok in input, settings, im GPU eo Colab ej leļọk. Ilo run eo jinoin, NeMo im model eo 1.23 GB tōrerein rej download bar juon.
- Audio eo aetok rej jerbal kake ilo internal chunks, kōn men in recognition emaroñ jelet iturin chunk boundaries.

## Canonical source im generation

Jikin jān eo emool im emaroñ ukote:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ej synchronized canonical snapshot. Kajin Japan ej save einwōt reviewed translation ilo `locales/ja.json`, im README snapshot eo an ej copy ñan root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ej oktak jen ordinary CI. Ordinary users im CI rejjab aikuj translation credentials.

## License

Notebook scaffolding im build/check scripts rej MIT licensed. Third Intelligence model eo rejjab redistribute e ijin im ej idaapdikdik iumin **Apache-2.0**. Third-party dependencies rej kejbarok license ko aer make.
