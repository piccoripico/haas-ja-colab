# Haas Japanese Colab

Notebook Google Colab untuk mentranskripsikan audio dan video bahasa Jepang dengan Third Intelligence **Haas-ja-v1.0**.

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_id.ipynb)

## Fitur

- **Gratis:** Berjalan pada runtime GPU gratis Google Colab.
- **ASR bahasa Jepang:** Menggunakan [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model sekitar 0,6 miliar parameter untuk pengenalan ucapan bahasa Jepang.
- **Cepat:** Transkripsi dapat diproses dengan cepat.
- **Tanda baca:** Model menghasilkan perkiraan tanda baca bahasa Jepang.
- **Timestamp dan subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pemrosesan file panjang:** File audio dan video panjang juga dapat diproses.
- **Dukungan Google Drive:** Unggah file secara langsung atau baca dari Google Drive; ZIP keluaran dapat disimpan ke Drive secara opsional.
- **Beragam keluaran:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, dan ZIP.

## Penggunaan

1. Pilih `INPUT_MODE` di **1. Pengaturan** dan sesuaikan pengaturan lain jika diperlukan.
2. Pilih **Runtime → Run all**.
3. Dengan `INPUT_MODE = "upload"`, pilih file di **2. Pemilihan file / pemasangan Google Drive**.
4. ZIP keluaran diunduh secara otomatis setelah pemrosesan selesai.

## Mode timestamp

- `none`: tanpa informasi waktu.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File panjang

`CHUNK_SECONDS` mengontrol durasi chunk internal yang digunakan untuk file panjang. Nilai lebih besar mengurangi batas chunk dan mempertahankan lebih banyak konteks, tetapi membuat setiap inferensi lebih berat dan dapat menggunakan lebih banyak memori GPU. Nilai lebih kecil membuat setiap inferensi lebih ringan tetapi menciptakan lebih banyak batas, yang dapat memengaruhi pengenalan di sekitar titik tersebut. Nilai default direkomendasikan dalam kebanyakan kasus.

## UI terlokalisasi

Model ASR itu sendiri **hanya untuk bahasa Jepang**. Pelokalan README dan UI Colab mencakup semua **183 bahasa aktif ISO 639 Set 1** (`sh` yang usang dikecualikan).

Bahasa Inggris (`en`) adalah sumber terjemahan kanonik. Bahasa Jepang (`ja`) adalah terjemahan yang telah ditinjau dan disalin ke root repositori sebagai tampilan default `README.md`. README bahasa Jepang di root **tidak** digunakan sebagai sumber terjemahan. 181 locale lainnya diterjemahkan mesin dari bahasa Inggris.

## Catatan

- Notebook berhenti sebelum transkripsi jika GPU tidak tersedia.
- Waktu pemrosesan bergantung pada panjang input, pengaturan, dan GPU yang diberikan oleh Colab. Pada eksekusi pertama, NeMo dan model sekitar 1.23 GB juga diunduh.
- Audio panjang diproses dalam chunk internal, sehingga pengenalan dapat terpengaruh di sekitar batas chunk.

## Sumber kanonik dan pembuatan

Sumber kanonik yang dapat diterjemahkan:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` adalah snapshot kanonik yang tersinkronisasi. Bahasa Jepang dipelihara sebagai terjemahan yang ditinjau di `locales/ja.json`, dan snapshot README-nya disalin ke `README.md` di root.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Pemeliharaan terjemahan terpisah dari CI biasa. Pengguna biasa dan CI tidak memerlukan kredensial terjemahan.

## Lisensi

Kerangka notebook dan skrip build/check berlisensi MIT. Model Third Intelligence tidak didistribusikan ulang di sini dan diatur oleh **Apache-2.0**. Dependensi pihak ketiga mempertahankan lisensi masing-masing.
