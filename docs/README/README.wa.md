# Haas Japanese Colab

Cayet Google Colab po transcrire do son eyet des videyos djaponès avou Third Intelligence **Haas-ja-v1.0**.

[![Drovi dins Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_wa.ipynb)

## Fonccions

- **Gråtos:** I rote sol runtime GPU gråtos di Google Colab.
- **ASR djaponès:** I s’ sieve di [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), on modele di pus ou moens 0.6B parametes po rconoxhe li parole djaponese.
- **Rade:** Li transcripcion pout esse traitêye radmint.
- **Ponctuåcion:** Li modele rexhe ene ponctuåcion djaponese estimêye.
- **Markes di tins eyet sot-tites:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Traitmint des longs fitchîs:** Les longs fitchîs di son eyet d’ videyo polèt eto esse traitîs.
- **Sopoirt Google Drive:** Tcherdjîz les fitchîs direk ou lijhoz les dins Google Drive; li ZIP di rexhowe pout esse schapé dins Drive si vos vloz.
- **Sacwantès rexhowes:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest eyet ZIP.

## Eployaedje

1. Tchoezixhoz `INPUT_MODE` dins **1. Apontiaedjes** eyet candjîz les ôtes apontiaedjes si mezåjhe.
2. Tchoezixhoz **Runtime → Run all**.
3. Avou `INPUT_MODE = "upload"`, tchoezixhoz les fitchîs dins **2. Tchoezixhaedje des fitchîs / montaetche Google Drive**.
4. Li ZIP di rexhowe est aberwet otomaticmint cwand li traitmint est fini.

## Modes di markes di tins

- `none`: nole informåcion di tins.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Discodeu

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Longs fitchîs

`CHUNK_SECONDS` controle li tins des bokets intrinnes eployîs po les longs fitchîs. Des pus grandès valixhances diminiwèt les limites eyet wårdnut pus d’ contexe, mins tchaeke inferince est pus pezante eyet pout eployî pus d’ memwere GPU. Des pus ptitès valixhances rindèt tchaeke inferince pus lidjire mins fwait pus di limites, çou ki pout aveur èn efet sol rconoxhance åtoû d’ ces ponts. Li valixhance prémetowe est ricmandêye dins l’ pus grand pårt des cas.

## Eterface locålijheye

Li modele ASR lu-minme est **seulmint djaponès**. Li locålijhaedje do README eyet d’ l’ eterface Colab covixhe totes les **183 lingaedjes actifs ISO 639 Set 1** (`sh` vî metou foû).

L’ inglès (`en`) est l’ sourdant canonike do ratournaedje. Li djaponès (`ja`) est on ratournaedje rveyou eyet est copyî al raecene do dépôt come prezintaedje prémetowe `README.md`. Li README djaponès al raecene **n’ est nén** eployî come sourdant do ratournaedje. Les ôtes 181 locales sont ratournés på machine a pårti d’ l’ inglès.

## Rimårkes

- Li cayet s’ djoke divant l’ transcripcion si gn a nou GPU disponibe.
- Li tins do traitmint dipind del longreu d’ l’ intrêye, des apontiaedjes eyet do GPU diné pa Colab. Li prumî côp aberwe eto NeMo eyet l’ modele di pus ou moens 1.23 GB.
- Li long son est traitî e bokets intrinnes, don li rconoxhance pout esse candjeye åtoû des limites des bokets.

## Sourdant canonike eyet ahivaedje

Sourdants canonikes k’ on pout ratourner:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` est l’ imådje canonike sincronijheye. Li djaponès est wårdé come ratournaedje rveyou dins `locales/ja.json`, eyet si snapshot README est copyî dins `README.md` al raecene.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Li manaedjmint des ratournaedjes est separé do CI normå. Les uzeus normås eyet l’ CI n’ ont nén mezåjhe di credintiels di ratournaedje.

## Licince

Li scrifture do cayet eyet les scripts build/check sont dizo licince MIT. Li modele Third Intelligence n’ est nén ridistribouwé chal eyet est governé pa **Apache-2.0**. Les dipindinces di troejhinme pårt wårdnut leus licinces.
