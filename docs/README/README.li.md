# Haas Japanese Colab

Google Colab-notebook veur 't transcribere van Japanse audio en video mit Third Intelligence **Haas-ja-v1.0**.

[![Äöpene in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_li.ipynb)

## Mäögelikhede

- **Gratis:** Dreijt op de gratis GPU-runtime van Google Colab.
- **Japanse ASR:** Gebroek [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), 'n model mit óngerveer 0,6B parameters veur Japanse spraokherkenning.
- **Sjnel:** Transcriptie kan sjnel waere verwaerk.
- **Leestekes:** 't Model geuf gesjatte Japanse leestekes oet.
- **Tiedstempels en óndertitels:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Lange besjtande:** Lange audio- en videobesjtande kónne ouch waere verwaerk.
- **Google Drive-óngersteuning:** Upload besjtande rechstreeks of lees ze vanaaf Google Drive; de output-ZIP kan optioneel nao Drive waere opgeslage.
- **Meerdere outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest en ZIP.

## Gebroek

1. Keus `INPUT_MODE` in **1. Instèllinge** en pas anger instèllinge aan es dat neudig is.
2. Keus **Runtime → Run all**.
3. Mit `INPUT_MODE = "upload"`, keus besjtande in **2. Besjtandskeuze / Google Drive koppelen**.
4. De output-ZIP weurt automatisch gedownload nao de verwirking.

## Tiedstempelmodi

- `none`: gein tiedinformatie.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lange besjtande

`CHUNK_SECONDS` bepaolt de interne chunkdoer die veur lange besjtande gebroek weurt. Grotere waerdes vermindere 't aantal grenze en behawte mie context, mer make eder inferentie zwaarder en kónne mie GPU-geheuge broeke. Kleinder waerdes make eder inferentie lichter, mer make mie grenze, wat de herkenning rond die punte kan beïnvleuje. De sjtanderdwaerde weurt in de mieste gevalle aongeraoje.

## Gelokaliseerde UI

't ASR-model zelf is **allein Japans**. De lokalisatie van README en de Colab-UI besleit alle **183 actieve ISO 639 Set 1-tale** (de verajerde `sh` oetgezónderd).

Ingels (`en`) is de canonieke vertaolbrón. Japans (`ja`) is 'n nagekeurde vertaoling en weurt nao de repository-root gekopieerd es de sjtanderdpresentatie `README.md`. De Japanse README in de root weurt **neet** es vertaolbrón gebroek. De anger 181 locales waere machinaal vanaaf 't Ingels vertaold.

## Opmaerkinge

- De notebook sjtopt veur de transcriptie es gein GPU besjikbaar is.
- De verwaerkingstied hink aaf van de inputlengde, instèllinge en de GPU die Colab toewies. Bie de ierste run waere ouch NeMo en 't model van óngerveer 1.23 GB gedownload.
- Lange audio weurt in interne chunks verwaerk, dus de herkenning kan rond chunkgrenze beïnvloed waere.

## Canonieke brón en generatie

Canonieke vertaolbare brónne:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` is de gesynchroniseerde canonieke snapshot. Japans weurt es nagekeurde vertaoling óngerhawwe in `locales/ja.json`, en de README-snapshot dao-van weurt nao de root `README.md` gekopieerd.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Óngerhaw van vertaolinge sjteit los van gewone CI. Gewone gebroekers en CI höbbe gein vertaolcredentials neudig.

## Licentie

De notebook-sjabloon en build/check-scripts höbbe 'n MIT-licentie. 't Third Intelligence-model weurt hie neet mitgeleverd en velt ónger **Apache-2.0**. Dependencies van derde partieje behawte häör eige licenties.
