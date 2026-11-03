# Haas Japanese Colab

Google Colab notebook yo tsala Japanese audio na video yi va text hi Third Intelligence **Haas-ja-v1.0**.

[![Pfula eka Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ts.ipynb)

## Swihlawulekisi

- **Mahala:** Yi tirha eka GPU runtime ya mahala ya Google Colab.
- **Japanese ASR:** Yi tirhisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ya kwalomu ka 0.6B-parameter ya Japanese speech recognition.
- **Hi ku hatlisa:** Transcription yi nga processiwa hi ku hatlisa.
- **Punctuation:** Model yi humesa Japanese punctuation leyi yi ringanyeteke.
- **Timestamp na subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio na video file to leha ti nga processiwa na tona.
- **Google Drive support:** Upload file hi ku kongoma kumbe u yi hlaya eka Google Drive; output ZIP yi nga savedziwa eka Drive loko u swi lava.
- **Output to tala:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Matirhiselo

1. Hlawula `INPUT_MODE` eka **1. Settings** kutani u cinca setting yin'wana loko swi laveka.
2. Hlawula **Runtime → Run all**.
3. Loko `INPUT_MODE = "upload"`, hlawula file eka **2. File selection / Google Drive mount**.
4. Loko processing yi herile, output ZIP yi downloadeka hi yoxe.

## Timestamp modes

- `none`: a ku na timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File to leha

`CHUNK_SECONDS` yi lawula nkarhi wa internal chunk lowu tirhisiwaka eka file to leha. Value letikulu ti hunguta boundary naswona ti hlayisa context yo tala, kambe inference yin'wana na yin'wana yi tika naswona yi nga tirhisa GPU memory yo tala. Value letitsongo ti endla inference yi olova kambe ti endla boundary to tala, leswi nga khumbaka recognition ekusuhi na tindhawu teto. Eka swiyimo swo tala, default yi bumabumeriwa.

## UI leyi hundzuluxiweke

ASR model hi yoxe i **Japanese-only**. README na Colab UI localization yi katsa hinkwato **183 active ISO 639 Set 1 languages** (deprecated `sh` a yi katsiwanga).

English (`en`) i canonical translation source. Japanese (`ja`) i reviewed translation naswona yi copyiwa eka repository root tani hi default `README.md` presentation. Root Japanese README **a yi tirhisiwi** tani hi translation source. Locale tin'wana ta 181 i machine-translated ku suka eka English.

## Tinotsi

- Notebook yi yima transcription yi nga si sungula loko GPU yi nga ri kona.
- Processing time yi ya hi ku leha ka input, setting, na GPU leyi nyikiweke hi Colab. Eka run yo sungula, NeMo na model ya kwalomu ka 1.23 GB swi downloadiwa na swona.
- Audio yo leha yi processiwa hi internal chunks, kutani recognition yi nga khumbeka ekusuhi na chunk boundaries.

## Canonical source na generation

Swihlovo swa nkoka leswi hundzuluxekaka:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` i synchronized canonical snapshot. Japanese yi hlayisiwa tani hi reviewed translation eka `locales/ja.json`, naswona README snapshot ya yona yi copyiwa eka root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yi hambanile na ordinary CI. Ordinary users na CI a va lavi translation credentials.

## License

Notebook scaffolding na build/check scripts i MIT licensed. Third Intelligence model a yi redistributed laha naswona yi lawuriwa hi **Apache-2.0**. Third-party dependencies ti hlayisa licenses ta tona.
