# Haas Japanese Colab

Notebook ya Google Colab sambu na kusonika na texte audio mpi video ya Kiyapani na Third Intelligence **Haas-ja-v1.0**.

[![Kangula na Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kg.ipynb)

## Mambu yina yo lenda sala

- **Mpamba:** Ke salaka na GPU runtime ya mpamba ya Google Colab.
- **ASR ya Kiyapani:** Ke sadilaka [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ya pene-pene 0.6B parameters sambu na kuzaba ndinga ya Kiyapani.
- **Nswalu:** Transcription lenda kusalama nswalu.
- **Bilembo ya kusonika:** Model ke pesaka bilembo ya kusonika ya Kiyapani yina yo me banza.
- **Timestamps mpi subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Kusala na bafile ya nda:** Audio mpi video file ya nda lenda mpi kusalama.
- **Lusadisu ya Google Drive:** Upload bafile mbala mosi to tanga yo na Google Drive; output ZIP lenda kubumbama na Drive kana nge me zola.
- **Baoutput mingi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, mpi ZIP.

## Mutindu ya kusadila

1. Pona `INPUT_MODE` na **1. Settings** mpi soba settings ya nkaka kana yo kele mfunu.
2. Pona **Runtime → Run all**.
3. Kana `INPUT_MODE = "upload"`, pona bafile na **2. File selection / Google Drive mount**.
4. Output ZIP ke download na yo mosi na nima ya processing.

## Bamode ya timestamp

- `none`: ata information ya ntangu ve.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Bafile ya nda

`CHUNK_SECONDS` ke kontrolaka ntangu ya internal chunk yina ke sadilama sambu na bafile ya nda. Ba value ya nene ke kitisaka boundaries mpi ke bumbaka context mingi, kansi inference konso ke kuma kilo mpi lenda kusadila GPU memory mingi. Ba value ya fioti ke salaka inference konso petepete kansi ke salaka boundaries mingi, yina lenda kubebisa recognition na pene ya bisika yina. Default kele mbote na ba kaso mingi.

## UI ya kubalula

ASR model yo mosi kele **kaka ya Kiyapani**. Kubalula ya README mpi Colab UI ke fukaka **183 active ISO 639 Set 1 languages** yonso (`sh` ya ntama kele ve).

Kizungu (`en`) kele canonical translation source. Kiyapani (`ja`) kele translation yina bo me tala mpi bo ke kopia yo na root ya repository bonso default `README.md`. README ya Kiyapani na root **ke sadilama ve** bonso source ya translation. Ba locale 181 ya nkaka ke balulama na machine na Kizungu.

## Mambu ya kuyibuka

- Notebook ke telema na ntwala ya transcription kana GPU kele ve.
- Processing time ke landaka nda ya input, settings, mpi GPU yina Colab me pesa. Na run ya ntete, NeMo mpi model ya pene-pene 1.23 GB ke download mpi.
- Audio ya nda ke salama na internal chunks, yo yina recognition lenda kubebisama na pene ya chunk boundaries.

## Canonical source mpi generation

Ba canonical source yina lenda kubalulama:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` kele synchronized canonical snapshot. Kiyapani ke bumbama bonso reviewed translation na `locales/ja.json`, mpi snapshot ya README na yo ke kopiama na root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Maintenance ya translation kele ya kukabwana na CI ya kawaida. Ba user ya kawaida mpi CI ke lombaka translation credentials ve.

## License

Notebook scaffolding mpi build/check scripts kele na license ya MIT. Third Intelligence model ke redistribuer ve awa mpi yo kele na nsi ya **Apache-2.0**. Ba dependency ya bantu ya nkaka ke bumbaka ba license na bo.
