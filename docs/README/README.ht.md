# Haas Japanese Colab

Kaye Google Colab pou transkri odyo ak videyo japonè ak Third Intelligence **Haas-ja-v1.0**.

[![Louvri nan Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ht.ipynb)

## Karakteristik

- **Gratis:** Li mache sou runtime GPU gratis Google Colab la.
- **ASR japonè:** Li itilize [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), yon modèl anviwon 0.6B paramèt pou rekonesans lapawòl japonè.
- **Rapid:** Transkripsyon an ka trete rapidman.
- **Ponktiyasyon:** Modèl la bay ponktiyasyon japonè li estime.
- **Tan ak soutit:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Tretman fichye long:** Fichye odyo ak videyo ki long ka trete tou.
- **Sipò Google Drive:** Telechaje fichye dirèkteman oswa li yo nan Google Drive; ou ka chwazi pou sove ZIP rezilta a sou Drive.
- **Plizyè rezilta:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ak ZIP.

## Itilizasyon

1. Chwazi `INPUT_MODE` nan **1. Settings** epi ajiste lòt paramèt si sa nesesè.
2. Chwazi **Runtime → Run all**.
3. Avèk `INPUT_MODE = "upload"`, chwazi fichye nan **2. File selection / mount Google Drive**.
4. ZIP rezilta a telechaje otomatikman apre tretman an.

## Mòd tan

- `none`: pa gen enfòmasyon sou tan.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekodè

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fichye long

`CHUNK_SECONDS` kontwole dire chunk entèn yo itilize pou fichye long. Pi gwo valè diminye limit yo epi konsève plis kontèks, men yo fè chak inference pi lou epi yo ka itilize plis memwa GPU. Pi piti valè fè chak inference pi lejè men kreye plis limit, sa ki ka afekte rekonesans bò kote pwen sa yo. Valè pa default la rekòmande nan pifò ka.

## Entèfas lokalize

Modèl ASR la menm **se sèlman pou japonè**. Lokalizasyon README ak entèfas Colab la kouvri **tout 183 lang aktif ISO 639 Set 1** yo (`sh` ki demode a pa ladan).

Angle (`en`) se sous tradiksyon canonical la. Japonè (`ja`) se yon tradiksyon revize epi yo kopye li nan rasin repository a kòm prezantasyon `README.md` pa default. README japonè ki nan rasin lan **pa itilize kòm sous tradiksyon**. Lòt 181 locale yo tradui otomatikman soti nan angle.

## Nòt

- Kaye a kanpe anvan transkripsyon si pa gen GPU disponib.
- Tan tretman an depann de longè input la, paramèt yo ak GPU Colab bay la. Premye run lan telechaje NeMo ak modèl anviwon 1.23 GB la tou.
- Yo trete odyo long an chunks entèn, konsa rekonesans ka afekte bò kote limit chunks yo.

## Sous canonical ak jenerasyon

Sous canonical ki ka tradui:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` se snapshot canonical senkronize a. Yo kenbe japonè kòm tradiksyon revize nan `locales/ja.json`, epi yo kopye snapshot README li a nan `README.md` rasin lan.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Antretyen tradiksyon separe ak CI nòmal. Itilizatè nòmal ak CI pa bezwen kalifikasyon tradiksyon.

## Lisans

Estrikti notebook la ak scripts build/check yo anba lisans MIT. Modèl Third Intelligence la pa redistribye isit la epi li anba **Apache-2.0**. Depandans twazyèm pati yo kenbe pwòp lisans pa yo.
