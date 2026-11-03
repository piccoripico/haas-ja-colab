# Haas Japanese Colab

Google Colab-notaboek om Japannese oudio en video met Third Intelligence **Haas-ja-v1.0** te transkribeer.

[![Maak in Colab oop](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_af.ipynb)

## Kenmerke

- **Gratis:** Loop op Google Colab se gratis GPU-looptyd.
- **Japannese ASR:** Gebruik [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), ’n model met ongeveer 0,6 miljard parameters vir Japannese spraakherkenning.
- **Vinnig:** Transkripsie kan vinnig verwerk word.
- **Leestekens:** Die model lewer geskatte Japannese leestekens.
- **Tydstempels en onderskrifte:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Verwerking van lang lêers:** Lang oudio- en videolêers kan ook verwerk word.
- **Google Drive-ondersteuning:** Laai lêers direk op of lees dit vanaf Google Drive; die uitvoer-ZIP kan opsioneel in Drive gestoor word.
- **Veelvuldige uitvoere:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest en ZIP.

## Gebruik

1. Kies `INPUT_MODE` in **1. Instellings** en pas ander instellings aan indien nodig.
2. Kies **Runtime → Run all**.
3. Met `INPUT_MODE = "upload"`, kies lêers in **2. Lêerkeuse / Google Drive-montering**.
4. Die uitvoer-ZIP word outomaties afgelaai nadat verwerking voltooi is.

## Tydstempelmodusse

- `none`: geen tydinligting nie.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekodeerder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lang lêers

`CHUNK_SECONDS` beheer die interne blokduur wat vir lang lêers gebruik word. Groter waardes verminder grense en behou meer konteks, maar maak elke afleiding swaarder en kan meer GPU-geheue gebruik. Kleiner waardes maak elke afleiding ligter maar skep meer grense, wat herkenning rondom daardie punte kan beïnvloed. Die verstekwaarde word in die meeste gevalle aanbeveel.

## Gelokaliseerde gebruikerskoppelvlak

Die ASR-model self is **slegs vir Japannees**. README- en Colab-koppelvlaklokalisering dek al **183 aktiewe ISO 639 Set 1-tale** (verouderde `sh` uitgesluit).

Engels (`en`) is die kanonieke vertaalbron. Japannees (`ja`) is ’n nagegane vertaling en word na die bewaarplek se wortel gekopieer as die verstek `README.md`-aanbieding. Die wortel-Japannese README word **nie** as vertaalbron gebruik nie. Die ander 181 locales word masjienvertaal uit Engels.

## Notas

- Die notaboek stop voor transkripsie as ’n GPU nie beskikbaar is nie.
- Verwerkingstyd hang af van invoerlengte, instellings en die GPU wat Colab toeken. Met die eerste loop word NeMo en die model van ongeveer 1.23 GB ook afgelaai.
- Lang oudio word in interne blokke verwerk, daarom kan herkenning rondom blokgrense beïnvloed word.

## Kanonieke bron en generering

Kanonieke vertaalbare bronne:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` is die gesinchroniseerde kanonieke momentopname. Japannees word as ’n nagegane vertaling in `locales/ja.json` onderhou, en die README-momentopname word na die wortel-`README.md` gekopieer.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Vertaalonderhoud is apart van gewone CI. Gewone gebruikers en CI benodig nie vertaalbewyse nie.

## Lisensie

Die notaboekstruktuur en bou-/kontroleskripte is onder MIT gelisensieer. Die Third Intelligence-model word nie hier herverdeel nie en word deur **Apache-2.0** beheer. Derdeparty-afhanklikhede behou hul eie lisensies.
