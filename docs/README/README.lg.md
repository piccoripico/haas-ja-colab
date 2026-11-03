# Haas Japanese Colab

Google Colab notebook ey'okukyusa amaloboozi ne vidiyo ez'Oluyapani okuzifuula ebiwandiiko nga ekozesa Third Intelligence **Haas-ja-v1.0**.

[![Ggulawo mu Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_lg.ipynb)

## Ebikolebwa

- **Ya bwereere:** Ekola ku GPU runtime ey'obwereere eya Google Colab.
- **Japanese ASR:** Ekozesa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model erina nga 0.6B-parameter ey'okutegeera okwogera kw'Oluyapani.
- **Ya mangu:** Transcription esobola oku processibwa amangu.
- **Punctuation:** Model efulumya Japanese punctuation gy'ekakasa nti gy'eri.
- **Timestamp ne subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio ne video file empanvu nazo zisobola oku processibwa.
- **Google Drive support:** Upload file butereevu oba zisome okuva mu Google Drive; output ZIP esobola oku savebwa ku Drive bw'oba oyagala.
- **Output nnyingi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ne ZIP.

## Enkozesa

1. Londa `INPUT_MODE` mu **1. Settings** era okyuse setting endala bwe kiba kyetaagisa.
2. Londa **Runtime → Run all**.
3. Singa `INPUT_MODE = "upload"`, londa file mu **2. File selection / Google Drive mount**.
4. Processing bw'eggwa, output ZIP edownloadibwa yokka.

## Timestamp modes

- `none`: tewali timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File empanvu

`CHUNK_SECONDS` efuga obuwanvu bwa internal chunk obukozesebwa ku file empanvu. Value ennene zikendeeza boundary ne zikuuma context nnyingi, naye buli inference ebeera nzito era eyinza okwongera ku GPU memory. Value entono zifuula buli inference ennyangu naye zikola boundary nnyingi, ezisobola okukosa recognition okumpi n'ebifo ebyo. Mu mbeera ezisinga, default y'esinga okulungi.

## UI evvuunuddwa

ASR model yennyini ya **Japanese-only**. README ne Colab UI localization bikwata ku **183 active ISO 639 Set 1 languages** zonna (deprecated `sh` tegirimu).

English (`en`) ye canonical translation source. Japanese (`ja`) ye reviewed translation era ecopibwa ku repository root nga default `README.md` presentation. Root Japanese README **tekozeesebwa** nga translation source. Locale endala 181 za machine-translated okuva mu English.

## Eby'okumanya

- Notebook eyimirira nga transcription tennatandika singa GPU teriwo.
- Processing time esinziira ku buwanvu bwa input, setting, ne GPU Colab gy'ewa. Ku run esooka, NeMo ne model erina nga 1.23 GB nazo zidownloadibwa.
- Audio empanvu eprocessibwa mu internal chunks, kale recognition eyinza okukosebwa okumpi ne chunk boundaries.

## Canonical source ne generation

Ensibuko ennene ez’okuvvuunula:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ye synchronized canonical snapshot. Japanese ekuumibwa nga reviewed translation mu `locales/ja.json`, era README snapshot yaayo ecopibwa ku root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yawukana ku ordinary CI. Ordinary users ne CI tebeetaaga translation credentials.

## License

Notebook scaffolding ne build/check scripts ziri MIT licensed. Third Intelligence model teredistributed wano era efugibwa **Apache-2.0**. Third-party dependencies zikuuma licenses zaazo.
