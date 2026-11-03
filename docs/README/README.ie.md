# Haas Japanese Colab

Google Colab-notebook por transscrir japonesi audio e video per Third Intelligence **Haas-ja-v1.0**.

[![Aperter in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ie.ipynb)

## Caracteristicas

- **Gratuit:** Functiona in li gratuit GPU-runtime de Google Colab.
- **Japonesi ASR:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un model con circa 0.6B parametres por recognition de japonesi parlada lingue.
- **Rapid:** Li transscrition posse esser processat rapidmen.
- **Punctuation:** Li model producte estimat japonesi punctuation.
- **Tempmarcas e subtitules:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Processament de long files:** Long audio e video files posse anc esser processat.
- **Support de Google Drive:** Charge files directmen o lee les de Google Drive; li output ZIP posse optionalmen esser salvat in Drive.
- **Multiplic outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Usu

1. Selecte `INPUT_MODE` in **1. Parametres** e ajusta altri parametres si necessi.
2. Selecte **Runtime → Run all**.
3. Con `INPUT_MODE = "upload"`, selecte files in **2. Selection de files / montation de Google Drive**.
4. Li output ZIP es automaticmen descargat pos que li processament fini.

## Modes de tempmarca

- `none`: null information temporal.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificator

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files long

`CHUNK_SECONDS` controla li duration del intern partes usat por long files. Plu grand valores reducte limites e conserva plu contextu, ma chascun inference es plu pesant e posse usar plu GPU-memorie. Plu micri valores fa chascun inference plu levi ma crea plu limites, quel posse affecter recognition circum tis punctus. Li predefinit valore es recomandat in li pluparte de casus.

## Localisat interfacie

Li ASR-model self es **solmen japonesi**. Localisation del README e Colab-interfacie covri omni **183 activ lingues ISO 639 Set 1** (obsolet `sh` exclus).

Anglesi (`en`) es li canonic fonte de traduction. Japonesi (`ja`) es un revidet traduction e es copiat al radice del repository quam predefinit presentation `README.md`. Li radic japonesi README **ne es** usat quam fonte de traduction. Li altri 181 locales es machine-traductet de anglesi.

## Notas

- Li notebook halt ante transscrition si null GPU es disponibil.
- Li témpor de processament depende del longore del input, parametres e li GPU assignat de Colab. Li unesim execution anc descarga NeMo e li circa 1.23 GB model.
- Long audio es processat in intern partes, do recognition posse esser affectet circum li limites del partes.

## Canonic fonte e generation

Canonic traductibil fontes:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` es li sincronisat canonic snapshot. Japonesi es mantenet quam revidet traduction in `locales/ja.json`, e su README-snapshot es copiat a radic `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Mantenentie de traduction es separat de ordinari CI. Ordinari usatores e CI ne besona credentiales de traduction.

## Licentie

Li notebook-squelett e build/check-scrits es licentiat sub MIT. Li Third Intelligence-model ne es redistribuet ci e es governat de **Apache-2.0**. Tert-parti dependenties conserva lor propri licenties.
