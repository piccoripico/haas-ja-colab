# Haas Japanese Colab

Google Colab notebook yekushandura Japanese audio nevideo files kuita zvinyorwa uchishandisa Third Intelligence **Haas-ja-v1.0**.

[![Vhura muColab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sn.ipynb)

## Zvimiro

- **Yemahara:** Inomhanya paGoogle Colab free GPU runtime.
- **Japanese ASR:** Inoshandisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ine angangoita 0.6B parameters yeJapanese speech recognition.
- **Inokurumidza:** Transcription inogona kugadziriswa nekukurumidza.
- **Punctuation:** Model inoburitsa Japanese punctuation yakafungidzirwa.
- **Timestamps nema-subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Kugadzirisa files refu:** Audio nevideo files refu dzinogonawo kugadziriswa.
- **Google Drive support:** Upload files zvakananga kana kudziverenga kubva kuGoogle Drive; output ZIP inogona kuchengetwa kuDrive kana zvichidiwa.
- **Outputs dzakawanda:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, neZIP.

## Kushandisa

1. Sarudza `INPUT_MODE` mu **1. Settings** wogadzirisa mamwe settings kana zvichidiwa.
2. Sarudza **Runtime → Run all**.
3. Kana `INPUT_MODE = "upload"`, sarudza files mu **2. File selection / Google Drive mount**.
4. Output ZIP inodownload otomatiki kana processing yapera.

## Timestamp modes

- `none`: hapana timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files refu

`CHUNK_SECONDS` inodzora internal chunk duration inoshandiswa pa files refu. Values dzakakura dzinoderedza boundaries uye dzinochengeta context yakawanda, asi dzinoita inference imwe neimwe kurema uye dzinogona kuwedzera GPU memory usage. Values diki dzinoita inference imwe neimwe nyore asi dzinogadzira boundaries dzakawanda, izvo zvinogona kukanganisa recognition padyo nenzvimbo idzodzo. Default inokurudzirwa kazhinji.

## UI yakashandurirwa mitauro

ASR model pachayo ndeye **Japanese-only**. Localization yeREADME neColab UI inovhara **183 active ISO 639 Set 1 languages** dzese (deprecated `sh` yakabviswa).

English (`en`) ndiyo canonical translation source. Japanese (`ja`) ireviewed translation uye inokopwa ku repository root se default `README.md` presentation. Root Japanese README **haishandiswe** se translation source. Mamwe locales 181 ari machine-translated kubva kuEnglish.

## Zvinyorwa

- Notebook inomira pamberi pe transcription kana GPU isipo.
- Processing time inoenderana nehurefu hweinput, settings, neGPU yakapiwa neColab. Pa run yekutanga, NeMo nemodel inosvika 1.23 GB zvinodownloadwawo.
- Long audio inogadziriswa mu internal chunks, saka recognition inogona kukanganiswa padyo ne chunk boundaries.

## Canonical source ne generation

Zvinyorwa zvikuru zvinodudzirika:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ndiyo synchronized canonical snapshot. Japanese inochengetwa se reviewed translation mu `locales/ja.json`, uye README snapshot yayo inokopwa ku root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yakaparadzana ne ordinary CI. Ordinary users neCI havadi translation credentials.

## Rezinesi

Notebook scaffolding ne build/check scripts zviri MIT licensed. Third Intelligence model haigoverwi zvakare pano uye inotongwa ne **Apache-2.0**. Third-party dependencies dzinochengeta licenses dzadzo.
