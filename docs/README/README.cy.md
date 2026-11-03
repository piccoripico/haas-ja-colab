# Haas Japanese Colab

Llyfr nodiadau Google Colab ar gyfer trawsgrifio sain a fideo Japaneaidd gyda Third Intelligence **Haas-ja-v1.0**.

[![Agor yn Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_cy.ipynb)

## Nodweddion

- **Am ddim:** Yn rhedeg ar runtime GPU am ddim Google Colab.
- **ASR Japaneaidd:** Yn defnyddio [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model tua 0.6B paramedr ar gyfer adnabod lleferydd Japaneaidd.
- **Cyflym:** Gellir prosesu trawsgrifiad yn gyflym.
- **Atalnodi:** Mae’r model yn allbynnu atalnodi Japaneaidd amcangyfrifedig.
- **Stampiau amser ac isdeitlau:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Prosesu ffeiliau hir:** Gellir prosesu ffeiliau sain a fideo hir hefyd.
- **Cymorth Google Drive:** Llwythwch ffeiliau i fyny yn uniongyrchol neu darllenwch nhw o Google Drive; gellir cadw’r ZIP allbwn i Drive yn ddewisol.
- **Allbynnau lluosog:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, a ZIP.

## Defnydd

1. Dewiswch `INPUT_MODE` yn **1. Gosodiadau** ac addaswch osodiadau eraill os oes angen.
2. Dewiswch **Runtime → Run all**.
3. Gyda `INPUT_MODE = "upload"`, dewiswch ffeiliau yn **2. Dewis ffeil / mowntio Google Drive**.
4. Caiff y ZIP allbwn ei lawrlwytho’n awtomatig ar ôl i’r prosesu orffen.

## Moddau stamp amser

- `none`: dim gwybodaeth amseru.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Datgodiwr

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Ffeiliau hir

Mae `CHUNK_SECONDS` yn rheoli hyd y darn mewnol a ddefnyddir ar gyfer ffeiliau hir. Mae gwerthoedd mwy yn lleihau ffiniau ac yn cadw mwy o gyd-destun, ond mae pob inferiad yn drymach a gall ddefnyddio mwy o gof GPU. Mae gwerthoedd llai yn gwneud pob inferiad yn ysgafnach ond yn creu mwy o ffiniau, a all effeithio ar adnabod o gwmpas y pwyntiau hynny. Argymhellir y gwerth rhagosodedig yn y rhan fwyaf o achosion.

## Rhyngwyneb lleol

Mae’r model ASR ei hun yn **Japaneaidd yn unig**. Mae lleoleiddio README a rhyngwyneb Colab yn cwmpasu pob un o’r **183 iaith ISO 639 Set 1 weithredol** (`sh` darfodedig wedi’i hepgor).

Saesneg (`en`) yw’r ffynhonnell gyfieithu ganonaidd. Mae Japaneaidd (`ja`) yn gyfieithiad wedi’i adolygu ac yn cael ei gopïo i wraidd yr ystorfa fel y cyflwyniad `README.md` rhagosodedig. **Nid yw** README Japaneaidd y gwraidd yn cael ei ddefnyddio fel ffynhonnell gyfieithu. Mae’r 181 locale arall wedi’u cyfieithu’n beirianyddol o’r Saesneg.

## Nodiadau

- Mae’r llyfr nodiadau yn stopio cyn trawsgrifio os nad oes GPU ar gael.
- Mae amser prosesu yn dibynnu ar hyd y mewnbwn, y gosodiadau, a’r GPU a neilltuir gan Colab. Mae’r rhediad cyntaf hefyd yn lawrlwytho NeMo a’r model tua 1.23 GB.
- Mae sain hir yn cael ei phrosesu mewn darnau mewnol, felly gall adnabod gael ei effeithio o gwmpas ffiniau darnau.

## Ffynhonnell ganonaidd a chynhyrchu

Ffynonellau cyfieithadwy canonaidd:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yw’r ciplun canonaidd wedi’i gydamseru. Cedwir Japaneaidd fel cyfieithiad wedi’i adolygu yn `locales/ja.json`, a chopïir ei giplun README i `README.md` yn y gwraidd.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Mae cynnal cyfieithiadau ar wahân i CI arferol. Nid oes angen tystlythyrau cyfieithu ar ddefnyddwyr arferol na CI.

## Trwydded

Mae sgaffald y llyfr nodiadau a’r sgriptiau adeiladu/gwirio o dan drwydded MIT. Nid yw’r model Third Intelligence yn cael ei ailddosbarthu yma ac mae dan **Apache-2.0**. Mae dibyniaethau trydydd parti yn cadw eu trwyddedau eu hunain.
