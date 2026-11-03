# Haas Japanese Colab

Bonj Google Colab notebook neix yungh Third Intelligence **Haas-ja-v1.0** dawz audio caeuq video Vah Yitbun doxgaiq baenz saw.

[![Hai youq Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_za.ipynb)

## Gijndei

- **Mbouj yungh ngaenz:** Guh youq Google Colab free GPU runtime.
- **Vah Yitbun ASR:** Yungh [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), dwg model miz daih'iek 0.6B-parameter guh songj yinh Vah Yitbun.
- **Vaiq:** Transcription ndaej process vaiq.
- **Punctuation:** Model fat ok punctuation Vah Yitbun itding.
- **Timestamps caeuq subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Process file raez:** Audio caeuq video file raez cungj ndaej process.
- **Google Drive support:** Upload file doxgaiq roxnaeuz doeg de youq Google Drive; output ZIP ndaej siengj nyi save youq Drive.
- **Output lai cungj:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, caeuq ZIP.

## Cungj yungh

1. Youq **1. Settings** gwnz gen `INPUT_MODE`, caeuq gaij setting danghnaeuz aeu.
2. Gen **Runtime → Run all**.
3. Dangh `INPUT_MODE = "upload"`, youq **2. File selection / Google Drive mount** gen file.
4. Process sat le, output ZIP doenghdeih download.

## Timestamp mode

- `none`: mbouj miz timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File raez

`CHUNK_SECONDS` control geizgan internal chunk yungh guh file raez. Value hung guh boundary noix caeuq baenz context lai, hoengz inference goek ndeu dwg naek caeuq ndaej yungh GPU memory lai. Value iq guh inference yiengh ndei hoengz guh boundary lai, gij neix ndaej haih recognition youq henz. Ciengzseiz yungh default dwg ndei.

## UI Vah Deihfueng

ASR model bonjfaenh dwg **Vah Yitbun dog**. README caeuq Colab UI localization baenz cungj **183 active ISO 639 Set 1 languages** (mbouj hab deprecated `sh`).

English (`en`) dwg canonical translation source. Vah Yitbun (`ja`) dwg reviewed translation, caeuq copy bae repository root guh default `README.md` presentation. Root Japanese README **mbouj dwg** translation source. Locale lingh 181 dwg machine-translated daj English.

## Geiq

- Dangh mbouj miz GPU, notebook dingz youq transcription caengz hwnj.
- Processing time raeuz miz doxgaiq daengz input raez, setting, caeuq GPU Colab hai. Run daih'it cungj download NeMo caeuq model daih'iek 1.23 GB.
- Audio raez process baenz internal chunk, baenzneix recognition ndaej doiq youq chunk boundary henz.

## Canonical source caeuq generation

Canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` dwg synchronized canonical snapshot. Vah Yitbun baenz reviewed translation youq `locales/ja.json`, caeuq README snapshot de copy bae root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance dwg gak rox ordinary CI. User ciengzseiz caeuq CI mbouj aeu translation credentials.

## License

Notebook scaffolding caeuq build/check scripts dwg MIT licensed. Third Intelligence model mbouj redistribute youq neix caeuq aeu **Apache-2.0** guenj. Third-party dependency baenz ndei license bonjfaenh.
