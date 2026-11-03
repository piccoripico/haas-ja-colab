# Haas Japanese Colab

Google Colab notebook japanimiut oqaasiinik nipinik videonillu Third Intelligence **Haas-ja-v1.0** atorlugu allaganngortitsinissamut.

[![Colab-imi ammaruk](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kl.ipynb)

## Suliarineqarsinnaasut

- **Akeqanngilaq:** Google Colab-ip akeqanngitsumik GPU runtime-ani ingerlasarpoq.
- **Japanimiut oqaasiinut ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model miss. 0.6B parameterilik japanimiut oqaasiinik ilisarsinermut, atorneqartarpoq.
- **Sukkasuumik:** Transcription sukkasuumik suliarineqarsinnaavoq.
- **Allannermi ilisarnaatit:** Model japanimiut oqaasiini allannermi ilisarnaatit naatsorsuutigineqartut anillatsittarpai.
- **Timestamps aamma subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File-t takisuut:** Audio aamma video file-t takisuut aamma suliarineqarsinnaapput.
- **Google Drive:** File-t toqqaannartumik upload-ikkit imaluunniit Google Drive-imit atuakkit; output ZIP kissaatigigaanni Drive-mut toqqorneqarsinnaavoq.
- **Output-it assigiinngitsut:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest aamma ZIP.

## Atornissaa

1. **1. Settings**-imi `INPUT_MODE` toqqaruk, pisariaqarpallu settings allat allanngortikkit.
2. **Runtime → Run all** toqqaruk.
3. `INPUT_MODE = "upload"`-imi, **2. File selection / Google Drive mount**-imi file-t toqqakkit.
4. Suliarineqareerpat output ZIP nammineq download-issaaq.

## Timestamp mode-t

- `none`: piffissamut paasissutissaqanngilaq.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File-t takisuut

`CHUNK_SECONDS` file-ni takisuuni internal chunk-ip sivisussusaa aqutsarpaa. Value-t anginerit boundaries ikilisittarpaat context-ilu annertunerusoq pigiinnarlugu, kisianni inference ataasiakkaat oqimaannerulersarput GPU memory-lu annertunerusoq atorneqarsinnaalluni. Value-t minnerit inference ataasiakkaat oqinnerulersittarpaat, kisianni boundaries amerlanerulersittarlugit, tamannalu taakkua eqqaanni recognition-imut sunniuteqarsinnaavoq. Pisuni amerlanerni default innersuussutigineqarpoq.

## UI nutserneqarsimasoq

ASR model nammineq **japanimiut oqaasiinut kisimi** naatsorsuussaavoq. README aamma Colab UI localization **ISO 639 Set 1-imi oqaatsit active 183-it tamarmik** ilanngullugit suliarineqarput (`sh` pisoqaq ilanngunneqanngilaq).

Tuluttut (`en`) canonical translation source-iuvoq. Japanimiutut (`ja`) reviewed translation-iuvoq repository-p root-ianut default `README.md`-itut kopiigaq. Root-imi Japanese README **translation source-itut atorneqanngilaq**. Locale-t allat 181-it tuluttut machine-translate-erneqartarput.

## Maluginiagassat

- GPU atorneqarsinnaanngippat notebook transcription sioqqullugu unittarpoq.
- Processing time input-ip sivisussusaa, settings aamma Colab-ip GPU tunniussaa apeqqutaallutik allanngortarpoq. Run siulleq NeMo aamma model miss. 1.23 GB download-erneqarput.
- Audio takisooq internal chunks atorlugit suliarineqartarpoq, taamaattumillu recognition chunk boundaries eqqaanni sunnerneqarsinnaavoq.

## Canonical source aamma generation

Nutserneqarsinnaasut aallaaviit pingaarnerit:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot-iuvoq. Japanimiutut reviewed translation-itut `locales/ja.json`-imi нигоҳineqarpoq, README snapshot-ialu root `README.md`-imut kopiigaavoq.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI-mit immikkoortuuvoq. Ordinary users aamma CI translation credentials pisariaqartinngilaat.

## License

Notebook scaffolding aamma build/check scripts MIT licenseqarput. Third Intelligence model uani redistributerneqanngilaq, **Apache-2.0**-imillu aqunneqarpoq. Third-party dependencies namminneq license-tik pigiinnartarpaat.
