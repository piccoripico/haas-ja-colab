# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ބޭނުންކޮށް ޖަޕާނީ އަޑާއި ވީޑިއޯ ފައިލްތައް ލިޔުމަށް ބަދަލުކުރާ Google Colab ނޯޓްބުކެކެވެ.

[![Colab ގައި ހުޅުވާ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_dv.ipynb)

## ޚާއްސިއްޔަތުތައް

- **ހިލޭ:** Google Colab ގެ ހިލޭ GPU runtime ގައި ދުއްވައެވެ.
- **ޖަޕާނީ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ބޭނުންކުރެވެއެވެ؛ މިއީ ޖަޕާނީ އަޑު ދެނެގަންނަން ހަމައެކަނި 0.6B parameter ހުންނަ މޮޑެލެކެވެ.
- **އަވަސް:** ޓްރާންސްކްރިޕްޝަން އަވަހަށް ޕްރޮސެސް ކުރެވޭނެއެވެ.
- **ނިޝާންތައް:** މޮޑެލުން ލަފާކުރެވޭ ޖަޕާނީ punctuation ނެރެއެވެ.
- **ވަގުތު ނިޝާންތަކާއި ސަބްޓައިޓަލް:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ދިގު ފައިލް ޕްރޮސެސިންގ:** ދިގު އަޑު އަދި ވީޑިއޯ ފައިލްތައްވެސް ޕްރޮސެސް ކުރެވޭނެއެވެ.
- **Google Drive ސަޕޯޓް:** ފައިލްތައް ސީދާ upload ކުރަން ނުވަތަ Google Drive އިން ކިޔަން ހެދޭނެއެވެ؛ ނަތީޖާގެ ZIP އިޚްތިޔާރީކޮށް Drive ގައި ސޭވް ކުރެވޭނެއެވެ.
- **ތަފާތު ނަތީޖާތައް:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, އަދި ZIP.

## ބޭނުންކުރާނެ ގޮތް

1. **1. Settings** ގައި `INPUT_MODE` ހޮވައި، ބޭނުންވާނަމަ އެހެން settings ބަދަލުކުރާށެވެ.
2. **Runtime → Run all** ހޮވާށެވެ.
3. `INPUT_MODE = "upload"` ނަމަ، **2. File selection / Google Drive mount** ގައި ފައިލްތައް ހޮވާށެވެ.
4. ޕްރޮސެސް ނިމުމުން ނަތީޖާގެ ZIP އޮޓޮމެޓިކްކޮށް download ވާނެއެވެ.

## Timestamp mode ތައް

- `none`: ވަގުތާ ބެހޭ މަޢުލޫމާތެއް ނެތް.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ދިގު ފައިލްތައް

`CHUNK_SECONDS` އިން ދިގު ފައިލްތަކަށް ބޭނުންކުރާ internal chunk ގެ މުއްދަތު ކޮންޓްރޯލް ކުރެއެވެ. ބޮޑު value ތަކުން boundary މަދުކޮށް context ގިނަކޮށް ބަހައްޓާނެ ނަމަވެސް، ކޮންމެ inference އެއް ބުރަވެ GPU memory ގިނައިން ބޭނުންކުރެވިދާނެއެވެ. ކުޑަ value ތަކުން ކޮންމެ inference އެއް ފަސޭހަވާ ނަމަވެސް boundary ގިނަވެ، އެ ތަންތަނުގެ ކައިރީގައި recognition އަށް އަސަރުކުރެވިދާނެއެވެ. ގިނަ ހާލަތެއްގައި default ރަނގަޅެވެ.

## ތަރުޖަމާކުރެވިފައިވާ UI

ASR މޮޑެލް އެކަނި **ޖަޕާނީ ބަހަށް** ކަމުދެއެވެ. README އަދި Colab UI ގެ localization އިން **183 active ISO 639 Set 1 languages** ހުރިހާ ބަހަކަށް ހިމެނެއެވެ (deprecated `sh` ނުހިމަނާ).

English (`en`) އަކީ canonical translation source އެވެ. ޖަޕާނީ (`ja`) އަކީ review ކުރެވިފައިވާ ތަރުޖަމާއެއް، އަދި repository root އަށް default `README.md` ދެއްކުމެއްގެ ގޮތުގައި copy ކުރެއެވެ. Root ގެ Japanese README އަކީ translation source އެއް **ނޫނެވެ**. އެހެން 181 locale އިން English އިން machine translation ކުރެވެއެވެ.

## ނޯޓްތައް

- GPU ނުލިބެންޏާ ނޯޓްބުކުން transcription ފަށާކަށް ކުރިން ހުއްޓާލައެވެ.
- ޕްރޮސެސިންގ ވަގުތު އިންޕުޓްގެ ދިގުމާއި settings އަދި Colab އިން ދޭ GPU އަށް ބަލާފައި އެބައޮތެވެ. ފުރަތަމަ run ގައި NeMo އާއި ހަމައެކަނި 1.23 GB ގެ މޮޑެލްވެސް download ކުރެއެވެ.
- ދިގު އަޑު internal chunk ތަކުގައި ޕްރޮސެސް ކުރާތީ chunk boundary ގެ ކައިރީގައި recognition އަށް އަސަރުކުރެވިދާނެއެވެ.

## Canonical source އާއި generation

ތަރުޖަމާ ކުރެވޭ canonical source ތައް:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` އަކީ synchronized canonical snapshot އެވެ. ޖަޕާނީ ބަސް `locales/ja.json` ގައި review ކުރެވިފައިވާ ތަރުޖަމާއެއްގެ ގޮތުގައި ބަހައްޓައެވެ، އަދި އޭގެ README snapshot އެ root `README.md` އަށް copy ކުރެއެވެ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

ތަރުޖަމާ maintenance އަކީ އާންމު CI އިން ވަކިކޮށް ބަހައްޓާ ކަމެކެވެ. އާންމު ބޭނުންކުރާ މީހުންނާއި CI އަށް translation credential އެއް ނުބޭނުމެވެ.

## ލައިސަންސް

Notebook scaffolding އާއި build/check scripts އަކީ MIT license އެވެ. Third Intelligence މޮޑެލް މިތަނުން އަލުން distribute ނުކުރެއެވެ އަދި **Apache-2.0** ގެ ދަށުން ހިނގައެވެ. Third-party dependency ތައް އެއެއްޗެހީގެ license ބަހައްޓައެވެ.
