# Haas Japanese Colab

I-Google Colab notebook yekubhala phansi umsindvo nemavidiyo esiJapane abe text nge-Third Intelligence **Haas-ja-v1.0**.

[![Vula ku-Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ss.ipynb)

## Tici

- **Mahhala:** Isebenza ku-GPU runtime yamahhala ye-Google Colab.
- **Japanese ASR:** Isebenzisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model lenema-parameter langaba 0.6B ekubona inkhulumo yesiJapane.
- **Iyashesha:** Transcription ingaprocesswa ngekushesha.
- **Punctuation:** Model ikhipha Japanese punctuation lelinganisiwe.
- **Timestamp nema-subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio nemavidiyo file lamadze nawo angaprocesswa.
- **Google Drive support:** Upload file ngco noma uyifundze ku-Google Drive; output ZIP ingasavedvwa ku-Drive uma ufuna.
- **Output leminyenti:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ne-ZIP.

## Kusetjentiswa

1. Khetsa `INPUT_MODE` ku-**1. Settings** bese ushintja letinye setting uma kudzingeka.
2. Khetsa **Runtime → Run all**.
3. Uma `INPUT_MODE = "upload"`, khetsa file ku-**2. File selection / Google Drive mount**.
4. Uma processing seyiphelile, output ZIP idownloadwa ngekwayo.

## Timestamp modes

- `none`: akukho timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File lamadze

`CHUNK_SECONDS` ilawula budze be-internal chunk lesetjentiswa ku-file lamadze. Value lamakhulu anciphisa boundary futsi agcine context lenyenti, kodvwa inference ngayinye iba nzima futsi ingasebentisa GPU memory lenyenti. Value lamancane enza inference ngayinye ibe lula kodvwa akhe boundary letinyenti, lokungaphazamisa recognition edvute nalawo maphuzu. Esikhatsini lesinyenti, i-default inconywa.

## UI lehunyushiwe

ASR model yona iy **Japanese-only**. README ne-Colab UI localization ifaka tonkhe **183 active ISO 639 Set 1 languages** (deprecated `sh` ayifakiwe).

English (`en`) yi-canonical translation source. Japanese (`ja`) yi-reviewed translation futsi icopywa ku-repository root njenge-default `README.md` presentation. Root Japanese README **ayisetjentiswa** njenge-translation source. Lamanye ma-locale langu-181 ama-machine-translated kusuka ku-English.

## Caphela

- Notebook iyema ngaphambi kwe-transcription uma GPU ingekho.
- Processing time incike ebudzeni be-input, setting, ne-GPU lebelwe yi-Colab. Ku-run yekucala, NeMo ne-model lengaba 1.23 GB kuyadownloadwa futsi.
- Audio lendze iprocesswa kuma-internal chunks, ngako recognition ingaphazamiseka edvute nema-chunk boundaries.

## Canonical source ne-generation

Imitfombo leyinhloko lengahunyushwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yi-synchronized canonical snapshot. Japanese igcinwa njenge-reviewed translation ku-`locales/ja.json`, futsi README snapshot yayo icopywa ku-root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yehlukile ku-ordinary CI. Ordinary users ne-CI abadzingi translation credentials.

## License

Notebook scaffolding ne-build/check scripts ti-MIT licensed. Third Intelligence model ayiredistributed lapha futsi ibuswa yi-**Apache-2.0**. Third-party dependencies tigcina licenses tato.
