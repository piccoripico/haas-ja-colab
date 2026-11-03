# Haas Japanese Colab

Google Colab mazina'igan gaa-ozhichigaadeg ji-ozhibii'igewin Japanin odoodemag audio miinawaa video, Third Intelligence **Haas-ja-v1.0** ji-odaabajichigaadeg.

[![Baatiin Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_oj.ipynb)

## Aaniin ge-izhichigaadeg

- **Giizhigad:** Odaabajichigaade Google Colab free GPU runtime.
- **Japanin ASR:** Odaabajitoon [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), aapiji 0.6B parameter model gaa-ozhichigaadeg Japanin gidawewin ji-ozhibii'igewin.
- **Wiiba:** Gashkitoon wiiba ji-gichi-ozhibii'igewin.
- **Gikinoo'amaadiwin mazina'iganan:** Model biindig ozhichige Japanin punctuation gaa-inaadiziwang.
- **Timestamps miinawaa subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Gichi-file da-odaapinigaade:** Gichi audio miinawaa video files gashkitoon da-izhichigaadewag.
- **Google Drive:** File baatiin nagamonan gemaa onaakonan gaa-ayaawan Google Drive; output ZIP gashkitoon da-ashkigaade Drive ishkode gii-ikidooyan.
- **Midaaswiin output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, miinawaa ZIP.

## Aaniin ji-odaabajitooyan

1. Onaakon `INPUT_MODE` **1. Settings** nindoonji, miinawaa ozhibii'an geyaabi settings apane ge-izhichigeyin.
2. Onaakon **Runtime → Run all**.
3. Giishpin `INPUT_MODE = "upload"`, onaakon files **2. File selection / Google Drive mount** nindoonji.
4. Gii-ishkwaa-izhichigaadeg, output ZIP gagwe da-download-igaade.

## Timestamp modes

- `none`: gaawiin wiiji-timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Gichi files

`CHUNK_SECONDS` onaakon aaniin apii internal chunk da-ayaamagak gichi file. Gichi values maakadewag boundaries miinawaa nawaj ganawendaan context, dash bebe inference nawaj gichi miinawaa gashkitoon nawaj GPU memory ji-odaabajitoog. Agaasing values bebe inference bebakaan da-izhichige, dash nawaj boundaries ozhichigaadewag, ge-onji recognition ji-ani-bakaanagak asemaa. Default mino-inaakonigaade gechiwaag cases.

## Geyaabi localized UI

ASR model gagwe **Japanin gidawewin eta** odaabajitoon. README miinawaa Colab UI localization gashkitoon **183 active ISO 639 Set 1 languages** (`sh` gaa-ani-deprecated gaawiin biindigesinoon).

English (`en`) wiin canonical translation source. Japanese (`ja`) reviewed translation, miinawaa ozhichigaade repository root ji-ayaamagak default `README.md`. Root Japanese README **gaawiin** translation source. Aanind 181 locales machine-translated English nindoonji.

## Gagwejiganan

- Notebook gii-gashkiwan wiin transcription ji-maajitaag, giishpin GPU gaawiin ayaasinoon.
- Processing time aaniin minik input, settings, miinawaa GPU gaa-miinigowin Google Colab. Niigaan run gii-maajitaag, NeMo miinawaa aapiji 1.23 GB model da-download-igaadewag.
- Gichi audio internal chunks izhichigaadewag, ge-onji recognition ji-bakaanagak chunk boundaries asemaa.

## Canonical source miinawaa generation

Gichi-mazina’iganan gaa-gashkitoowaad ji-aazhaawizowag:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot. Japanese reviewed translation gaa-ganawendamaag `locales/ja.json`, miinawaa README snapshot ozhichigaade root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance bebakaan izhichigaade ordinary CI nindoonji. Ordinary users miinawaa CI gaawiin translation credentials gagwejitoosiig.

## License

Notebook scaffolding miinawaa build/check scripts MIT licensed. Third Intelligence model gaawiin izhichigaadesinoon omaa, miinawaa **Apache-2.0** onaakonigewin gagwe. Third-party dependencies ganawendamoog bezhig-bezhig o-do-license-wa.
