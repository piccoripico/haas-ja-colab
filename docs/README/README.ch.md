# Haas Japanese Colab

Google Colab notebook para u matugi’ i audio yan video gi fino’ Hapones ni Third Intelligence **Haas-ja-v1.0**.

[![Baba gi Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ch.ipynb)

## Siña-ta

- **Apu siha:** Mamagof gi free GPU runtime gi Google Colab.
- **Hapones ASR:** Ma’usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un model ni humihot 0.6B parameter para u tungo’ i fino’ Hapones.
- **Chaddek:** Siña ma-prosesa i transcription gi chaddek.
- **Punctuation:** I model ha na’huyong i ma’estima na punctuation Hapones.
- **Timestamp yan subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Prosesa file anåkko’:** Siña lokkue’ ma-prosesa i anåkko’ na audio yan video file.
- **Google Drive support:** Upload i file diretso pat taitai ginen Google Drive; siña ma-save i output ZIP gi Drive yanggen malago’.
- **Meggai na output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, yan ZIP.

## Månmanå’usa

1. Ayek `INPUT_MODE` gi **1. Settings** ya arregla i otro na settings yanggen nisisita.
2. Ayek **Runtime → Run all**.
3. Yanggen `INPUT_MODE = "upload"`, ayek i file gi **2. File selection / Google Drive mount**.
4. I output ZIP para u download automatico despues di ma-prosesa.

## Timestamp modes

- `none`: tåya’ timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Anåkko’ na file

`CHUNK_SECONDS` ha kontrola i durasion i internal chunk ni ma’usa para anåkko’ na file. Mas dångkolo na value ha menus i boundaries ya ha na’sahguan mas context, lao mas pesao kada inference ya siña mas meggai GPU memory ma’usa. Mas dikike’ na value ha na’liviano kada inference lao ha fa’tinas mas meggai boundaries, ni siña ha afekta i recognition gi hihot esti na punto. I default i rekomendao gi mas meggai na kaso.

## UI ni ma lokalisa

I ASR model mismo **Hapones ha’**. I localization i README yan Colab UI ha aflak i **183 active ISO 639 Set 1 languages** (deprecated `sh` ti ma’inclui).

I Ingles (`en`) i canonical translation source. I Hapones (`ja`) un reviewed translation ya ma-kopia guatu gi repository root kumu default `README.md` presentation. I root Japanese README **ti** ma’usa kumu translation source. I otro 181 locale ma-machine-translate ginen Ingles.

## Nota

- I notebook para u påra antes di transcription yanggen tåya’ GPU disponible.
- I processing time depende gi input length, settings, yan i GPU ni ha assign i Colab. Gi fine’nana na run, ma-download lokkue’ i NeMo yan i model ni humihot 1.23 GB.
- I anåkko’ na audio ma-prosesa gi internal chunks, pues siña ma-afekta i recognition gi hihot chunk boundaries.

## Canonical source yan generation

Prinsipåt na fuente siha para tinilaika:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` i synchronized canonical snapshot. I Hapones ma-mantieni kumu reviewed translation gi `locales/ja.json`, ya i README snapshot-ña ma-kopia guatu gi root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

I translation maintenance separao ginen ordinary CI. I ordinary users yan CI ti nisisita translation credentials.

## Lisensia

I notebook scaffolding yan build/check scripts MIT licensed. I Third Intelligence model ti ma-redistribute guini ya ma-gobietna ni **Apache-2.0**. I third-party dependencies ha na’sahguan i propio na lisensia-niha.
