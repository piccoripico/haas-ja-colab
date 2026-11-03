# Haas Japanese Colab

I-Google Colab notebook yokuguqula amafayela omsindo nevidiyo yesiJapane abe umbhalo kusetshenziswa i-Third Intelligence **Haas-ja-v1.0**.

[![Vula ku-Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_zu.ipynb)

## Izici

- **Mahhala:** Isebenza ku-GPU runtime yamahhala ye-Google Colab.
- **Japanese ASR:** Isebenzisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), imodeli enama-parameter acishe abe ngu-0.6B yokuqaphela inkulumo yesiJapane.
- **Iyashesha:** I-transcription ingacutshungulwa ngokushesha.
- **Izimpawu zokubhala:** Imodeli ikhipha Japanese punctuation elinganiselwe.
- **Timestamps nama-subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ukucubungula amafayela amade:** Amafayela omsindo nevidiyo amade nawo angacutshungulwa.
- **Ukusekelwa kwe-Google Drive:** Upload amafayela ngqo noma uwafunde ku-Google Drive; i-output ZIP ingagcinwa ku-Drive uma kudingeka.
- **Outputs eziningi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kanye ZIP.

## Ukusetshenziswa

1. Khetha `INPUT_MODE` ku-**1. Settings** bese ulungisa ezinye settings uma kudingeka.
2. Khetha **Runtime → Run all**.
3. Uma `INPUT_MODE = "upload"`, khetha amafayela ku-**2. File selection / Google Drive mount**.
4. I-output ZIP ilandwa ngokuzenzakalelayo ngemva kokuphela kwe-processing.

## Izindlela ze-timestamp

- `none`: akukho timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Amafayela amade

`CHUNK_SECONDS` ilawula internal chunk duration esetshenziswa emafayeleni amade. Values ezinkulu zehlisa boundaries futhi zigcina context eningi, kodwa zenza inference ngayinye ibe nzima futhi zingandisa ukusetshenziswa kwe-GPU memory. Values ezincane zenza inference ngayinye ibe lula kodwa zakha boundaries eziningi, okungathinta recognition eduze kwalezo zindawo. I-default inconywa ezimweni eziningi.

## UI eyenziwe yasendaweni

Imodeli ye-ASR uqobo **ingeyesiJapane kuphela**. I-localization ye-README ne-Colab UI ihlanganisa zonke **183 active ISO 639 Set 1 languages** (i-deprecated `sh` ayifakiwe).

English (`en`) yi-canonical translation source. Japanese (`ja`) yi-reviewed translation futhi ikopishwa ku-repository root njenge-default `README.md` presentation. I-root Japanese README **ayisetshenziswa** njenge-translation source. Amanye ama-locale ayi-181 a-machine-translated kusuka ku-English.

## Amanothi

- I-notebook iyama ngaphambi kwe-transcription uma i-GPU ingatholakali.
- Processing time incike kubude be-input, settings, kanye ne-GPU enikezwe yi-Colab. Ku-run yokuqala, i-NeMo kanye nemodeli ecishe ibe ngu-1.23 GB nazo ziyalandwa.
- Long audio icutshungulwa ngama-internal chunks, ngakho recognition ingathinteka eduze kwe-chunk boundaries.

## Canonical source kanye generation

Imithombo eyinhloko engahunyushwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yi-synchronized canonical snapshot. Japanese igcinwa njenge-reviewed translation ku-`locales/ja.json`, futhi i-README snapshot yayo ikopishwa ku-root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yehlukile ku-ordinary CI. Ordinary users ne-CI abadingi translation credentials.

## Ilayisense

Notebook scaffolding kanye build/check scripts zi-MIT licensed. Imodeli ye-Third Intelligence ayiphinde isatshalaliswe lapha futhi ilawulwa yi-**Apache-2.0**. Third-party dependencies zigcina amalayisense azo.
