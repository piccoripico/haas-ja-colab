# Haas Japanese Colab

אַ Google Colab notebook צו טראַנסקריבירן יאַפּאַניש אַודיאָ און ווידעאָ מיט Third Intelligence **Haas-ja-v1.0**.

[![עפֿענען אין Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_yi.ipynb)

## פֿעיִקייטן

- **פֿרײַ:** לויפט אויף Google Colab'ס פֿרײַעם GPU runtime.
- **יאַפּאַנישער ASR:** ניצט [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), אַן בערך 0.6B-parameter model פֿאַר יאַפּאַנישער speech recognition.
- **שנעל:** Transcription קען ווערן שנעל processירט.
- **פּונקטואַציע:** דער Model גיט אַרויס געשאַצטע יאַפּאַנישע punctuation.
- **Timestamp און subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **לאַנגע file processing:** לאַנגע audio און video file קענען אויך ווערן processירט.
- **Google Drive support:** Upload file גלײַך אָדער לייענט זיי פֿון Google Drive; דער output ZIP קען אָפּציאָנעל ווערן saveד אויף Drive.
- **פֿאַרשידענע outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, און ZIP.

## באַניץ

1. קלײַבט `INPUT_MODE` אין **1. Settings** און פּאַסט אָן אַנדערע setting אויב נייטיק.
2. קלײַבט **Runtime → Run all**.
3. מיט `INPUT_MODE = "upload"`, קלײַבט file אין **2. File selection / Google Drive mount**.
4. דער output ZIP ווערט אויטאָמאַטיש downloadעד נאָך processing איז פֿאַרענדיקט.

## Timestamp modes

- `none`: קיין timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## לאַנגע files

`CHUNK_SECONDS` קאָנטראָלירט די internal chunk duration פֿאַר לאַנגע file. גרעסערע value רעדוצירן boundary און האַלטן מער context, אָבער יעדער inference ווערט שווערער און קען נוצן מער GPU memory. קלענערע value מאַכן יעדער inference לײַכטער, אָבער שאַפֿן מער boundary, וואָס קען ווירקן recognition אַרום יענע פּונקטן. אין רובֿ פֿאַלן ווערט דער default רעקאָמענדירט.

## לאָקאַליזירטער UI

דער ASR model אַליין איז **Japanese-only**. README און Colab UI localization דעקט אַלע **183 active ISO 639 Set 1 languages** (deprecated `sh` איז אַרויסגענומען).

English (`en`) איז דער canonical translation source. Japanese (`ja`) איז אַ reviewed translation און ווערט copyד צום repository root ווי דער default `README.md` presentation. דער root Japanese README ווערט **נישט** געניצט ווי translation source. די אַנדערע 181 locales זענען machine-translated פֿון English.

## באַמערקונגען

- דער notebook שטעלט זיך אָפּ פֿאַר transcription אויב קיין GPU איז נישט פֿאַראַן.
- Processing time ווענדט זיך אין input length, setting, און דעם GPU וואָס Colab גיט. בײַם ערשטן run ווערן אויך NeMo און דער בערך 1.23 GB model downloadעד.
- לאַנג audio ווערט processירט אין internal chunks, דערפֿאַר קען recognition ווערן באַאיינפלוסט אַרום chunk boundaries.

## Canonical source און generation

קאַנאָנישע קוועלער וואָס מע קען איבערזעצן:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` איז דער synchronized canonical snapshot. Japanese ווערט געהאַלטן ווי אַ reviewed translation אין `locales/ja.json`, און זײַן README snapshot ווערט copyד צו root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance איז באַזונדער פֿון ordinary CI. Ordinary users און CI דאַרפֿן נישט translation credentials.

## License

Notebook scaffolding און build/check scripts זענען MIT licensed. דער Third Intelligence model ווערט דאָ נישט redistributed און ווערט רעגולירט דורך **Apache-2.0**. Third-party dependencies האַלטן זייערע אייגענע licenses.
