# Haas Japanese Colab

Google Colab notebook ya go fetolela audio le video ya Sejapane go nna mokwalo ka Third Intelligence **Haas-ja-v1.0**.

[![Bula mo Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_tn.ipynb)

## Dikarolo

- **Mahala:** E dira mo GPU runtime ya mahala ya Google Colab.
- **Japanese ASR:** E dirisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model e e nang le parameters tse di ka nnang 0.6B ya Japanese speech recognition.
- **Ka bonako:** Transcription e ka dirwa ka bonako.
- **Punctuation:** Model e ntsha Japanese punctuation e e fopholeditsweng.
- **Timestamps le subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Go dira ka files tse ditelele:** Audio le video files tse ditelele le tsone di ka dirwa.
- **Google Drive support:** Upload files ka tlhamalalo kgotsa di bale mo Google Drive; output ZIP e ka bolokwa mo Drive fa o batla.
- **Outputs tse dintsi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, le ZIP.

## Tiriso

1. Tlhopha `INPUT_MODE` mo **1. Settings** mme o fetole settings tse dingwe fa go tlhokega.
2. Tlhopha **Runtime → Run all**.
3. Fa `INPUT_MODE = "upload"`, tlhopha files mo **2. File selection / Google Drive mount**.
4. Output ZIP e download ka boyona fa processing e sena go fela.

## Timestamp modes

- `none`: ga go timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files tse ditelele

`CHUNK_SECONDS` e laola internal chunk duration e e dirisiwang mo files tse ditelele. Values tse dikgolo di fokotsa boundaries mme di boloka context e ntsi, mme inference nngwe le nngwe e nna boima e bile e ka dirisa GPU memory e ntsi. Values tse dinnye di dira inference nngwe le nngwe e nne motlhofo mme di dira boundaries tse dintsi, tse di ka amang recognition gaufi le mafelo ao. Default e a eletsiwa mo mabakeng a le mantsi.

## UI e e fetoletsweng

ASR model ka boyona ke **Japanese-only**. Localization ya README le Colab UI e akaretsa **183 active ISO 639 Set 1 languages** tsotlhe (deprecated `sh` e tlositswe).

English (`en`) ke canonical translation source. Japanese (`ja`) ke reviewed translation mme e kopololelwa kwa repository root jaaka default `README.md` presentation. Root Japanese README **ga e dirisiwe** jaaka translation source. Locales tse dingwe tse 181 ke machine-translated go tswa mo English.

## Dintlha

- Notebook e ema pele ga transcription fa GPU e sa bonale.
- Processing time e ikaegile ka boleele jwa input, settings, le GPU e e neilweng ke Colab. Run ya ntlha gape e download NeMo le model ya mo e ka nnang 1.23 GB.
- Long audio e dirwa ka internal chunks, ka jalo recognition e ka amega gaufi le chunk boundaries.

## Canonical source le generation

Metswedi ya konokono e e ka ranolwang:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ke synchronized canonical snapshot. Japanese e tlhokomelwa jaaka reviewed translation mo `locales/ja.json`, mme README snapshot ya yone e kopololelwa kwa root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance e farologane le ordinary CI. Ordinary users le CI ga ba tlhoke translation credentials.

## License

Notebook scaffolding le build/check scripts di na le MIT license. Third Intelligence model ga e redistributed fano mme e laolwa ke **Apache-2.0**. Third-party dependencies di boloka licenses tsa tsone.
