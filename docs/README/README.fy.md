# Haas Japanese Colab

Google Colab-notebook foar it transkribearjen fan Japanske audio en fideo mei Third Intelligence **Haas-ja-v1.0**.

[![Iepenje yn Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_fy.ipynb)

## Funksjes

- **Fergees:** Rint op de fergese GPU-runtime fan Google Colab.
- **Japanske ASR:** Brûkt [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), in model mei likernôch 0,6B parameters foar Japanske spraakherkenning.
- **Fluch:** Transkripsje kin fluch ferwurke wurde.
- **Lêstekens:** It model jout skatte Japanske lêstekens út.
- **Tiidstimpels en ûndertitels:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ferwurking fan lange bestannen:** Lange audio- en fideobestannen kinne ek ferwurke wurde.
- **Stipe foar Google Drive:** Upload bestannen direkt of lês se út Google Drive; it útfier-ZIP kin opsjoneel yn Drive bewarre wurde.
- **Meardere útfieren:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest en ZIP.

## Gebrûk

1. Kies `INPUT_MODE` yn **1. Settings** en pas oare ynstellingen oan as dat nedich is.
2. Kies **Runtime → Run all**.
3. By `INPUT_MODE = "upload"` kiesst bestannen yn **2. File selection / Google Drive mount**.
4. It útfier-ZIP wurdt automatysk ynladen nei de ferwurking.

## Tiidstimpelmodi

- `none`: gjin tiidynformaasje.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lange bestannen

`CHUNK_SECONDS` regelet de ynterne chunklingte foar lange bestannen. Gruttere wearden ferminderje grinzen en behâlde mear kontekst, mar meitsje elke inferinsje swierder en kinne mear GPU-ûnthâld brûke. Lytsere wearden meitsje elke inferinsje lichter mar meitsje mear grinzen, wat de herkenning om dy punten hinne beynfloedzje kin. De standertwearde wurdt yn de measte gefallen oanret.

## Lokalisearre brûkersynterface

It ASR-model sels is **allinnich foar Japansk**. Lokalisaasje fan README en de Colab-UI omfiemet alle **183 aktive talen fan ISO 639 Set 1** (ferâldere `sh` útsletten).

Ingelsk (`en`) is de kanonike oersetboarne. Japansk (`ja`) is in neisjoene oersetting en wurdt nei de root fan it repository kopiearre as de standert `README.md`-presintaasje. It Japanske README yn de root wurdt **net** as oersetboarne brûkt. De oare 181 locales wurde masine-oerset út it Ingelsk.

## Notysjes

- It notebook stopt foar de transkripsje as gjin GPU beskikber is.
- Ferwurkingstiid hinget ôf fan de lingte fan de ynfier, de ynstellingen en de GPU dy’t Colab tawiist. De earste run downloadt ek NeMo en it model fan likernôch 1.23 GB.
- Lange audio wurdt yn ynterne chunks ferwurke, sadat herkenning om chunkgrinzen hinne beynfloede wurde kin.

## Kanonike boarne en generaasje

Kanonike oersetbere boarnen:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` is de syngronisearre kanonike snapshot. Japansk wurdt as neisjoene oersetting ûnderholden yn `locales/ja.json`, en de README-snapshot dêrfan wurdt nei root `README.md` kopiearre.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Oersetûnderhâld stiet los fan gewoane CI. Gewoane brûkers en CI hawwe gjin oersetcredentials nedich.

## Lisinsje

De notebookstruktuer en build/check-skripts binne lisinsjearre ûnder MIT. It Third Intelligence-model wurdt hjir net opnij ferspraat en falt ûnder **Apache-2.0**. Ofhinklikheden fan tredden behâlde har eigen lisinsjes.
