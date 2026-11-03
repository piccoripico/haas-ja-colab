# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** apnaqasa japonés audio ukat video qillqañataki Google Colab notebook.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ay.ipynb)

## Uñacht’äwinaka

- **Inaki:** Google Colab free GPU runtime ukan irnaqi.
- **Japonés ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) apnaqi, 0.6B parameter niya modelo japonés arsuña uñt’añataki.
- **Jank’aki:** Transcription jank’aki lurasiñawa.
- **Puntuación:** Modelo japonés puntuación amuyata mistuyi.
- **Timestamp ukat subtítulo:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Jaya archivo luraña:** Jaya audio ukat video archivo lurasiñawa.
- **Google Drive yanapa:** Archivo chiqak upload luraña jan ukax Google Drive ukat ullaña; output ZIP Drive ukan imasiñawa munasaxa.
- **Walja output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## Apnaqawi

1. **1. Settings** ukan `INPUT_MODE` ajlli ukat wakisaxa yaqha settings askicha.
2. **Runtime → Run all** ajlli.
3. `INPUT_MODE = "upload"` ukaxa, **2. File selection / Google Drive mount** ukan archivos ajlli.
4. Processing tukuyata, output ZIP pachpa download lurasi.

## Timestamp modenaka

- `none`: janiwa pacha yatiyawi utjkiti.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Jaya archivonaka

`CHUNK_SECONDS` jaya archivonakataki internal chunk pacha apnaqawi controlaraki. Jach’a valoranaka boundary juk’aptayi ukat context walja imasi, ukampis sapa inference juk’amp llamp’u jan ukasti ch’amawa ukat GPU memory juk’amp apnaqaspawa. Jisk’a valoranaka inference llamp’uchayi ukampis boundary walja luri, ukax recognition uka chiqanakana jan walt’ayaspawa. Jilapacha default valorawa iwxt’ata.

## Aymararu jaqukipata UI

ASR modelo pachpa **japonés arutaki mayakiwa**. README ukat Colab UI localization **ISO 639 Set 1 ukan 183 active arunaka** taqi ch’amanchasi (`sh` jan apnaqañampi).

Inglés (`en`) canonical translation source ukawa. Japonés (`ja`) reviewed translation ukawa ukat repository root ukar default `README.md` uñacht’äwi ukhama copy lurasi. Root japonés README **janiw translation source ukhama apnaqaskiti**. Yaqha 181 locale inglés ukat machine-translate lurasi.

## Qhananchawinaka

- GPU jan utjki ukhaxa notebook transcription nayra sayt’i.
- Processing pacha input jaya, settings ukat Colab churat GPU ukarjamawa. Nayrïri run NeMo ukat 1.23 GB niya model download luri.
- Jaya audio internal chunk ukan lurasi, ukhamat chunk boundary uka jak’an recognition jan walt’ayaspawa.

## Canonical source ukat generation

Canonical traducción lurkaña sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot ukawa. Japonés `locales/ja.json` ukan reviewed translation ukhama imatawa, ukat README snapshot root `README.md` ukar copy lurasi.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI ukat sapaqa. Ordinary users ukat CI janiw translation credentials munapkiti.

## License

Notebook scaffolding ukat build/check scripts MIT license ukaniwa. Third Intelligence model janiw aka chiqana redistributekiti ukat **Apache-2.0** ukan apnaqasi. Third-party dependencies pachpa license imasi.
