# Haas Japanese Colab

Notebook Google Colab kanggo nranskripsi audio lan video basa Jepang nganggo Third Intelligence **Haas-ja-v1.0**.

[![Bukak ing Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_jv.ipynb)

## Fitur

- **Gratis:** Mlaku ing runtime GPU gratis saka Google Colab.
- **ASR Jepang:** Nggunakake [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model kira-kira 0.6B parameter kanggo pangenalan wicara Jepang.
- **Cepet:** Transkripsi bisa diproses kanthi cepet.
- **Tandha wacan:** Model ngasilake tandha wacan Jepang sing diprakirakake.
- **Timestamp lan subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pangolahan file dawa:** File audio lan video sing dawa uga bisa diproses.
- **Dhukungan Google Drive:** Unggah file langsung utawa waca saka Google Drive; output ZIP bisa disimpen menyang Drive yen dikarepake.
- **Akeh output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, lan ZIP.

## Panggunaan

1. Pilih `INPUT_MODE` ing **1. Settings** lan atur setelan liyane yen perlu.
2. Pilih **Runtime → Run all**.
3. Kanthi `INPUT_MODE = "upload"`, pilih file ing **2. File selection / mount Google Drive**.
4. Output ZIP diundhuh kanthi otomatis sawise pangolahan.

## Mode timestamp

- `none`: ora ana informasi wektu.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File dawa

`CHUNK_SECONDS` ngontrol durasi chunk internal kanggo file dawa. Nilai luwih gedhe nyuda wates lan njaga luwih akeh konteks, nanging nggawe saben inference luwih abot lan bisa nggunakake memori GPU luwih akeh. Nilai luwih cilik nggawe saben inference luwih entheng nanging nggawe luwih akeh wates, sing bisa mengaruhi pangenalan ing cedhak titik kasebut. Nilai standar dianjurake ing umume kasus.

## UI sing dilokalisasi

Model ASR dhewe **mung kanggo basa Jepang**. Lokalisasi README lan UI Colab nyakup **183 basa aktif ISO 639 Set 1** (`sh` sing wis ora digunakake ora kalebu).

Basa Inggris (`en`) minangka sumber terjemahan canonical. Basa Jepang (`ja`) minangka terjemahan sing wis ditinjau lan disalin menyang root repository minangka tampilan `README.md` standar. README Jepang ing root **ora digunakake minangka sumber terjemahan**. 181 locale liyane diterjemahake mesin saka basa Inggris.

## Cathetan

- Notebook mandheg sadurunge transkripsi yen GPU ora kasedhiya.
- Wektu pangolahan gumantung marang dawa input, setelan, lan GPU sing diwenehake Colab. Run pisanan uga ngundhuh NeMo lan model kira-kira 1.23 GB.
- Audio dawa diproses ing chunks internal, mula pangenalan bisa kena pengaruh ing cedhak wates chunk.

## Sumber canonical lan generation

Sumber canonical sing bisa diterjemahake:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` minangka snapshot canonical sing disinkronake. Basa Jepang dijaga minangka terjemahan sing wis ditinjau ing `locales/ja.json`, lan snapshot README disalin menyang root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Pangopènan terjemahan kapisah saka CI biasa. Panganggo biasa lan CI ora mbutuhake kredensial terjemahan.

## Lisensi

Scaffolding notebook lan script build/check dilisensi miturut MIT. Model Third Intelligence ora disebarake maneh ing kene lan diatur dening **Apache-2.0**. Dependensi pihak katelu tetep nganggo lisensi dhewe.
