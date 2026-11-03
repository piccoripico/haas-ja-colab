# Haas Japanese Colab

I-Google Colab notebook yokuguqula iaudio nevidiyo yesiJapan ibe ngumbhalo kusetyenziswa i-Third Intelligence **Haas-ja-v1.0**.

[![Vula kwi-Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_xh.ipynb)

## Iimpawu

- **Simahla:** Isebenza kwi-GPU runtime yasimahla ye-Google Colab.
- **Japanese ASR:** Isebenzisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), imodeli ene-parameters ezimalunga ne-0.6B yokuqonda intetho yesiJapan.
- **Iyakhawuleza:** I-transcription ingalungiswa ngokukhawuleza.
- **Iimpawu zokubhala:** Imodeli ikhupha Japanese punctuation eqikelelweyo.
- **Timestamps kunye subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ukulungisa iifayile ezinde:** Iifayile zeaudio nevidiyo ezinde nazo zinokulungiswa.
- **Inkxaso ye-Google Drive:** Upload iifayile ngqo okanye uzifunde kwi-Google Drive; i-output ZIP inokugcinwa kwi-Drive ngokuzikhethela.
- **Iziphumo ezininzi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kunye ZIP.

## Ukusetyenziswa

1. Khetha `INPUT_MODE` kwi-**1. Settings** uze ulungise ezinye settings xa kufuneka.
2. Khetha **Runtime → Run all**.
3. Xa `INPUT_MODE = "upload"`, khetha iifayile kwi-**2. File selection / Google Drive mount**.
4. I-output ZIP ikhutshelwa ngokuzenzekelayo emva kokuba processing igqityiwe.

## Iindlela ze-timestamp

- `none`: akukho timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Iifayile ezinde

`CHUNK_SECONDS` ilawula internal chunk duration esetyenziswa kwiifayile ezinde. Values ezinkulu zinciphisa boundaries kwaye zigcina context eninzi, kodwa zenza inference nganye ibe nzima kwaye zinokwandisa ukusetyenziswa kwe-GPU memory. Values ezincinci zenza inference nganye ibe lula kodwa zenza boundaries ezininzi, nto leyo enokuchaphazela recognition kufuphi naloo ndawo. I-default iyacetyiswa kwiimeko ezininzi.

## UI eyenziwe yasekuhlaleni

Imodeli ye-ASR ngokwayo **yeyesiJapan kuphela**. I-localization ye-README kunye ne-Colab UI igubungela zonke **183 active ISO 639 Set 1 languages** (i-deprecated `sh` ayiqukwanga).

English (`en`) yi-canonical translation source. Japanese (`ja`) yi-reviewed translation kwaye ikopishwa kwi-repository root njenge-default `README.md` presentation. I-root Japanese README **ayisetyenziswa** njenge-translation source. Ezinye ii-locale eziyi-181 zi-machine-translated zisuka kwi-English.

## Amanqaku

- I-notebook iyema ngaphambi kwe-transcription ukuba i-GPU ayifumaneki.
- Processing time ixhomekeke kubude be-input, settings, kunye ne-GPU eyabelwe yi-Colab. Kwi-run yokuqala, i-NeMo kunye nemodeli emalunga ne-1.23 GB nazo ziyakhutshelwa.
- Long audio ilungiswa kwi-internal chunks, ngoko recognition inokuchaphazeleka kufuphi ne-chunk boundaries.

## Canonical source kunye generation

Imithombo esisiseko enokuguqulelwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yi-synchronized canonical snapshot. Japanese igcinwa njenge-reviewed translation kwi-`locales/ja.json`, kwaye i-README snapshot yayo ikopishwa kwi-root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yahlukile kwi-ordinary CI. Ordinary users kunye CI azidingi translation credentials.

## Ilayisensi

Notebook scaffolding kunye build/check scripts zi-MIT licensed. Imodeli ye-Third Intelligence ayisasazwa kwakhona apha kwaye ilawulwa yi-**Apache-2.0**. Third-party dependencies zigcina iilayisensi zazo.
