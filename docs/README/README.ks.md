# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** اِستعمال کٔرِتھ جاپٲنی آڈیو تہٕ ویڈیو فایِلن ہُند متن بناونہٕ خٲطرٕ Google Colab نوٹ بُک۔

[![Colab منز کھولیو](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ks.ipynb)

## خاصیتہٕ

- **مُفت:** Google Colab ہُند مُفت GPU runtime پٮ۪ٹھ چلان۔
- **جاپٲنی ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) اِستعمال کران، یُس جاپٲنی تقریر شناخٕتہٕ خٲطرٕ لگ بھگ 0.6B-parameter ماڈل چھُ۔
- **تیز:** transcription تیزی سان process کٔرِتھ ہٮ۪کَو۔
- **رموزِ اوقاف:** ماڈل جاپٲنی punctuation ہُند اندازٕ کٔرِتھ output دِوان۔
- **Timestamp تہٕ subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ژۆٹھہٕ فایِل process کرُن:** ژۆٹھہٕ آڈیو تہٕ ویڈیو فایِل تہِ process کٔرِتھ ہٮ۪کَو۔
- **Google Drive مدد:** فایِل سیدٕ upload کٔرِو یا Google Drive پٮ۪ٹھہٕ پڑھِو؛ output ZIP اختیار سان Drive منز save کٔرِتھ ہٮ۪کَو۔
- **واریاہ output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, تہٕ ZIP۔

## اِستعمال

1. **1. Settings** منز `INPUT_MODE` ژٲرِو تہٕ ضرورت آسہٕ تہٕ باقی setting بدلاوِو۔
2. **Runtime → Run all** ژٲرِو۔
3. اگر `INPUT_MODE = "upload"` آسہٕ، **2. File selection / Google Drive mount** منز فایِل ژٲرِو۔
4. processing ختم گژھنہٕ پتہٕ output ZIP خودکار طریقہٕ download گژھان۔

## Timestamp mode

- `none`: کانٛہہ timing information نَہ۔
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ژۆٹھہٕ فایِل

`CHUNK_SECONDS` ژۆٹھہٕ فایِلن خٲطرٕ اِستعمال گژھنہٕ وٲلۍ internal chunk ہُند duration control کران۔ بوٚڈ value boundary کم کران تہٕ واریاہ context محفوظ تھاوان، مگر ہر inference بھاری بناوان تہٕ GPU memory واریاہ اِستعمال گژھِتھ ہٮ۪کِ۔ لۄکٹ value ہر inference ہلکا بناوان مگر boundary واریاہ بناوان، یِمہٕ جایہٕ شناخٕتہٕ پٮ۪ٹھ اثر کٔرِتھ ہٮ۪کَن۔ عام طور default سفارش چھُ۔

## مقامی UI

ASR ماڈل پانہٕ **صرف جاپٲنی** چھُ۔ README تہٕ Colab UI localization تمام **183 active ISO 639 Set 1 languages** خٲطرٕ چھُ (deprecated `sh` خارج)۔

English (`en`) canonical translation source چھُ۔ جاپٲنی (`ja`) reviewed translation چھُ تہٕ repository root منز default `README.md` presentation بنٲوِتھ copy کرنہٕ یِوان۔ Root ہُند Japanese README translation source **نَہ چھُ**۔ باقی 181 locale English پٮ۪ٹھہٕ machine-translated چھِ۔

## نوٹ

- اگر GPU دستیاب نَہ آسہٕ تہٕ نوٹ بُک transcription شروع کرنہٕ برونٛہہ رُکان۔
- processing وقت input ہُند ژھۄٹ/ژۆٹھ، setting تہٕ Colab دِتمتِس GPU پٮ۪ٹھ منحصر چھُ۔ گۄڈنکس run منز NeMo تہٕ لگ بھگ 1.23 GB ماڈل تہِ download گژھان۔
- ژۆٹھ آڈیو internal chunk منز process گژھان، تمہٕ موجِب chunk boundary ہٕنٛدِس آس پاس recognition متاثر گژھِتھ ہٮ۪کِ۔

## Canonical source تہٕ generation

ترجمہٕ کٔرِتھ ہٮ۪کن وٲلۍ canonical source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot چھُ۔ جاپٲنی `locales/ja.json` منز reviewed translation طور برقرار تھاونہٕ یِوان، تہٕ تَمہِ ہُند README snapshot root `README.md` منز copy کرنہٕ یِوان۔

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance عام CI پٮ۪ٹھہٕ جُدا چھُ۔ عام user تہٕ CI یَن translation credential ہُند ضرورت نَہ چھُ۔

## License

Notebook scaffolding تہٕ build/check scripts MIT licensed چھِ۔ Third Intelligence ماڈل ییٚتہِ دوبارٕ redistribute نَہ گژھان تہٕ **Apache-2.0** تحت چھُ۔ Third-party dependency پنٕنۍ پنٕنۍ license برقرار تھاوان۔
