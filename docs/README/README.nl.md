# Haas Japanese Colab

Google Colab-notebook voor het transcriberen van Japanse audio en video met Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_nl.ipynb)

## Functies

- **Gratis:** Werkt in de gratis GPU-runtime van Google Colab.
- **Japanse ASR:** Gebruikt [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), een model met ongeveer 0.6B parameters voor Japanse spraakherkenning.
- **Snel:** Transcriptie kan snel worden verwerkt.
- **Interpunctie:** Het model geeft geschatte Japanse interpunctie weer.
- **Tijdstempels en ondertitels:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Verwerking van lange bestanden:** Ook lange audio- en videobestanden kunnen worden verwerkt.
- **Google Drive-ondersteuning:** Upload bestanden rechtstreeks of lees ze vanuit Google Drive; de uitvoer-ZIP kan optioneel in Drive worden opgeslagen.
- **Meerdere uitvoerformaten:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest en ZIP.

## Gebruik

1. Kies `INPUT_MODE` onder **1. Settings** en pas andere instellingen zo nodig aan.
2. Selecteer **Runtime → Run all**.
3. Kies bij `INPUT_MODE = "upload"` bestanden onder **2. File selection / Google Drive mount**.
4. De uitvoer-ZIP wordt automatisch gedownload nadat de verwerking is voltooid.

## Tijdstempelmodi

- `none`: geen timinginformatie.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lange bestanden

`CHUNK_SECONDS` bepaalt de interne chunkduur voor lange bestanden. Grotere waarden verminderen grenzen en behouden meer context, maar maken elke inferentie zwaarder en kunnen het GPU-geheugengebruik verhogen. Kleinere waarden maken elke inferentie lichter maar creëren meer grenzen, wat de herkenning rond die punten kan beïnvloeden. In de meeste gevallen wordt de standaardwaarde aanbevolen.

## Gelokaliseerde interface

Het ASR-model zelf is **alleen Japans**. De lokalisatie van README en Colab-UI omvat alle **183 actieve ISO 639 Set 1-talen** (het verouderde `sh` is uitgesloten).

Engels (`en`) is de canonieke vertaalbron. Japans (`ja`) is een beoordeelde vertaling en wordt naar de repository-root gekopieerd als de standaardpresentatie `README.md`. De Japanse root-README wordt **niet** als vertaalbron gebruikt. De overige 181 locales worden machinaal vanuit het Engels vertaald.

## Opmerkingen

- Het notebook stopt vóór transcriptie als er geen GPU beschikbaar is.
- De verwerkingstijd hangt af van de invoerlengte, instellingen en de door Colab toegewezen GPU. Bij de eerste run worden ook NeMo en het model van ongeveer 1.23 GB gedownload.
- Lange audio wordt in interne chunks verwerkt, waardoor de herkenning rond chunkgrenzen kan worden beïnvloed.

## Canonieke bron en generatie

Canonieke vertaalbare bronnen:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` is de gesynchroniseerde canonieke snapshot. Japans wordt onderhouden als beoordeelde vertaling in `locales/ja.json`, en de README-snapshot wordt naar de root gekopieerd als `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Vertaalonderhoud staat los van gewone CI. Gewone gebruikers en CI hebben geen vertaalreferenties nodig.

## Licentie

De notebookstructuur en build-/controlescripts hebben een MIT-licentie. Het Third Intelligence-model wordt hier niet herverdeeld en valt onder **Apache-2.0**. Afhankelijkheden van derden behouden hun eigen licenties.
