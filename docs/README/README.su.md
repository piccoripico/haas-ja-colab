# Haas Japanese Colab

Notebook Google Colab pikeun transkripsi audio jeung video basa Jepang nganggo Third Intelligence **Haas-ja-v1.0**.

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_su.ipynb)

## Fitur

- **Gratis:** Jalan dina GPU runtime gratis Google Colab.
- **ASR basa Jepang:** Nganggo [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modél kira-kira 0.6B parameter pikeun pangakuan ucapan basa Jepang.
- **Gancang:** Transkripsi bisa diprosés gancang.
- **Tanda baca:** Modél ngahasilkeun tanda baca basa Jepang anu diperkirakeun.
- **Timestamp jeung subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ngolah file panjang:** File audio jeung video panjang ogé bisa diprosés.
- **Rojongan Google Drive:** Upload file langsung atawa baca tina Google Drive; output ZIP bisa disimpen ka Drive sacara opsional.
- **Loba output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, jeung ZIP.

## Cara maké

1. Pilih `INPUT_MODE` dina **1. Setélan** sarta atur setélan séjén lamun diperlukeun.
2. Pilih **Runtime → Run all**.
3. Kalayan `INPUT_MODE = "upload"`, pilih file dina **2. Pilih file / mount Google Drive**.
4. Output ZIP bakal didownload otomatis sanggeus prosés réngsé.

## Mode timestamp

- `none`: teu aya informasi waktu.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File panjang

`CHUNK_SECONDS` ngatur lilana internal chunk pikeun file panjang. Nilai leuwih gedé ngurangan boundaries sarta ngajaga leuwih loba context, tapi unggal inference leuwih beurat sarta bisa ngagunakeun leuwih loba GPU memory. Nilai leuwih leutik ngajadikeun inference leuwih hampang tapi nyieun leuwih loba boundaries, anu bisa mangaruhan pangakuan di sabudeureun titik éta. Default value disarankeun dina kalolobaan kasus.

## UI lokal

Modél ASR sorangan **ngan basa Jepang**. Lokalisasi README jeung Colab UI ngawengku sakabéh **183 active ISO 639 Set 1 languages** (`sh` deprecated teu kaasup).

English (`en`) nyaéta canonical translation source. Japanese (`ja`) nyaéta reviewed translation sarta disalin ka repository root minangka default `README.md` presentation. Root Japanese README **teu dipaké minangka translation source**. 181 locales séjén ditarjamahkeun ku mesin tina English.

## Catetan

- Notebook eureun saméméh transcription lamun GPU teu aya.
- Waktu prosés gumantung kana panjang input, settings, jeung GPU anu dibikeun ku Colab. Run kahiji ogé download NeMo jeung modél kira-kira 1.23 GB.
- Audio panjang diprosés dina internal chunks, jadi pangakuan bisa kapangaruhan deukeut chunk boundaries.

## Canonical source jeung generation

Canonical sources anu bisa ditarjamahkeun:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` nyaéta synchronized canonical snapshot. Japanese dijaga minangka reviewed translation dina `locales/ja.json`, sarta README snapshot-na disalin ka root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance misah ti CI biasa. Pamaké biasa jeung CI teu merlukeun translation credentials.

## Lisénsi

Notebook scaffolding jeung build/check scripts dilisénsikeun ku MIT. Modél Third Intelligence henteu didistribusikeun deui di dieu sarta diatur ku **Apache-2.0**. Third-party dependencies tetep miboga lisénsi masing-masing.
