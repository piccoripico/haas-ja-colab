# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** سان جاپاني آڊيو ۽ وڊيو کي متن ۾ بدلائڻ لاءِ Google Colab notebook.

[![Colab ۾ کوليو](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sd.ipynb)

## خاصيتون

- **مفت:** Google Colab جي مفت GPU runtime تي هلندو آهي.
- **جاپاني ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) استعمال ڪري ٿو، جيڪو جاپاني speech recognition لاءِ لڳ ڀڳ 0.6B-parameter model آهي.
- **تيز:** Transcription تيزيءَ سان process ڪري سگهجي ٿي.
- **اوقاف:** Model اندازي ڪيل جاپاني punctuation output ڪري ٿو.
- **Timestamp ۽ subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ڊگهي file processing:** ڊگهي audio ۽ video file پڻ process ڪري سگهجن ٿيون.
- **Google Drive support:** File سڌي upload ڪريو يا Google Drive مان پڙهو؛ output ZIP اختياري طور Drive تي save ڪري سگهجي ٿو.
- **گهڻا output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ۽ ZIP.

## استعمال

1. **1. Settings** ۾ `INPUT_MODE` چونڊيو ۽ ضرورت هجي ته ٻيون setting ترتيب ڏيو.
2. **Runtime → Run all** چونڊيو.
3. جيڪڏهن `INPUT_MODE = "upload"` هجي ته **2. File selection / Google Drive mount** ۾ file چونڊيو.
4. Processing مڪمل ٿيڻ کان پوءِ output ZIP پاڻمرادو download ٿيندو.

## Timestamp mode

- `none`: ڪا timing information نه.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ڊگهيون file

`CHUNK_SECONDS` ڊگهي file لاءِ استعمال ٿيندڙ internal chunk جي مدت کي ڪنٽرول ڪري ٿو. وڏيون value boundary گهٽ ڪن ٿيون ۽ وڌيڪ context محفوظ رکن ٿيون، پر هر inference وڌيڪ ڳرو ٿيندو ۽ GPU memory وڌي سگهي ٿي. ننڍيون value هر inference کي هلڪو ڪن ٿيون، پر وڌيڪ boundary ٺاهين ٿيون، جيڪي انهن هنڌن جي ڀرسان recognition تي اثر وجهي سگهن ٿيون. اڪثر حالتن ۾ default سفارش ڪيل آهي.

## مقامي UI

ASR model پاڻ **Japanese-only** آهي. README ۽ Colab UI localization سڀني **183 active ISO 639 Set 1 languages** کي cover ڪري ٿي (deprecated `sh` شامل نه آهي).

English (`en`) canonical translation source آهي. Japanese (`ja`) reviewed translation آهي ۽ default `README.md` presentation طور repository root ڏانهن copy ٿئي ٿي. Root Japanese README کي translation source طور **استعمال نه ڪيو ويندو آهي**. باقي 181 locale English مان machine-translated آهن.

## نوٽس

- جيڪڏهن GPU موجود نه هجي ته notebook transcription کان اڳ بند ٿي ويندو.
- Processing time input جي ڊيگهه، setting، ۽ Colab طرفان ڏنل GPU تي دارومدار رکي ٿو. پهرين run ۾ NeMo ۽ لڳ ڀڳ 1.23 GB model به download ٿيندو.
- ڊگهو audio internal chunk ۾ process ٿيندو، تنهنڪري chunk boundary جي ڀرسان recognition متاثر ٿي سگهي ٿي.

## Canonical source ۽ generation

Canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot آهي. Japanese کي `locales/ja.json` ۾ reviewed translation طور برقرار رکيو وڃي ٿو، ۽ ان جو README snapshot root `README.md` ڏانهن copy ڪيو وڃي ٿو.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance عام CI کان الڳ آهي. عام user ۽ CI کي translation credential جي ضرورت ناهي.

## License

Notebook scaffolding ۽ build/check script MIT licensed آهن. Third Intelligence model هتي redistribute نٿو ڪيو وڃي ۽ **Apache-2.0** جي تابع آهي. Third-party dependency پنهنجا license برقرار رکن ٿا.
