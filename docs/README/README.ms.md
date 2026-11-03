# Haas Japanese Colab

Notebook Google Colab untuk mentranskripsi audio dan video Jepun dengan Third Intelligence **Haas-ja-v1.0**.

[![Buka dalam Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ms.ipynb)

## Ciri-ciri

- **Percuma:** Berjalan pada runtime GPU percuma Google Colab.
- **ASR Jepun:** Menggunakan [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model kira-kira 0.6B parameter untuk pengecaman pertuturan Jepun.
- **Pantas:** Transkripsi boleh diproses dengan pantas.
- **Tanda baca:** Model mengeluarkan tanda baca Jepun yang dianggarkan.
- **Cap masa dan sari kata:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pemprosesan fail panjang:** Fail audio dan video yang panjang juga boleh diproses.
- **Sokongan Google Drive:** Muat naik fail secara terus atau baca dari Google Drive; ZIP output boleh disimpan ke Drive secara pilihan.
- **Pelbagai output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, dan ZIP.

## Penggunaan

1. Pilih `INPUT_MODE` dalam **1. Tetapan** dan laraskan tetapan lain jika perlu.
2. Pilih **Runtime → Run all**.
3. Dengan `INPUT_MODE = "upload"`, pilih fail dalam **2. Pemilihan fail / lekap Google Drive**.
4. ZIP output dimuat turun secara automatik selepas pemprosesan selesai.

## Mod cap masa

- `none`: tiada maklumat masa.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Penyahkod

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fail panjang

`CHUNK_SECONDS` mengawal tempoh chunk dalaman yang digunakan untuk fail panjang. Nilai lebih besar mengurangkan sempadan dan mengekalkan lebih banyak konteks, tetapi setiap inference lebih berat dan mungkin menggunakan lebih banyak memori GPU. Nilai lebih kecil menjadikan setiap inference lebih ringan tetapi mencipta lebih banyak sempadan, yang boleh menjejaskan pengecaman di sekitar titik tersebut. Nilai default disyorkan dalam kebanyakan kes.

## UI disetempatkan

Model ASR itu sendiri **hanya untuk bahasa Jepun**. Penyetempatan README dan UI Colab meliputi semua **183 bahasa aktif ISO 639 Set 1** (`sh` yang lapuk dikecualikan).

Bahasa Inggeris (`en`) ialah sumber terjemahan canonical. Bahasa Jepun (`ja`) ialah terjemahan yang telah disemak dan disalin ke akar repositori sebagai paparan default `README.md`. README Jepun di akar **tidak digunakan** sebagai sumber terjemahan. 181 locale lain diterjemah mesin daripada bahasa Inggeris.

## Nota

- Notebook berhenti sebelum transkripsi jika GPU tidak tersedia.
- Masa pemprosesan bergantung pada panjang input, tetapan, dan GPU yang diberikan oleh Colab. Run pertama turut memuat turun NeMo dan model kira-kira 1.23 GB.
- Audio panjang diproses dalam chunk dalaman, jadi pengecaman boleh terjejas di sekitar sempadan chunk.

## Sumber canonical dan penjanaan

Sumber canonical yang boleh diterjemah:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ialah snapshot canonical yang disegerakkan. Bahasa Jepun dikekalkan sebagai terjemahan disemak dalam `locales/ja.json`, dan snapshot README-nya disalin ke `README.md` di akar.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Penyelenggaraan terjemahan berasingan daripada CI biasa. Pengguna biasa dan CI tidak memerlukan kelayakan terjemahan.

## Lesen

Struktur notebook dan skrip build/check dilesenkan di bawah MIT. Model Third Intelligence tidak diedarkan semula di sini dan tertakluk kepada **Apache-2.0**. Kebergantungan pihak ketiga mengekalkan lesen masing-masing.
