# Haas Japanese Colab

Google Colab-notatbok for transkribering av japansk lyd og video med Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_nb.ipynb)

## Funksjoner

- **Gratis:** Kjører i Google Colabs gratis GPU-kjøretid.
- **Japansk ASR:** Bruker [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), en modell med omtrent 0.6B parametere for japansk talegjenkjenning.
- **Rask:** Transkribering kan behandles raskt.
- **Tegnsetting:** Modellen gir estimert japansk tegnsetting.
- **Tidsstempler og undertekster:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Behandling av lange filer:** Lange lyd- og videofiler kan også behandles.
- **Google Drive-støtte:** Last opp filer direkte eller les dem fra Google Drive; utdata-ZIP kan valgfritt lagres på Drive.
- **Flere utdataformater:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest og ZIP.

## Bruk

1. Velg `INPUT_MODE` under **1. Settings** og juster andre innstillinger ved behov.
2. Velg **Runtime → Run all**.
3. Med `INPUT_MODE = "upload"` velger du filer under **2. File selection / Google Drive mount**.
4. Utdata-ZIP lastes ned automatisk når behandlingen er ferdig.

## Tidsstempelmoduser

- `none`: ingen tidsinformasjon.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lange filer

`CHUNK_SECONDS` styrer den interne chunkvarigheten for lange filer. Større verdier reduserer grenser og bevarer mer kontekst, men gjør hver inferens tyngre og kan øke GPU-minnebruken. Mindre verdier gjør hver inferens lettere, men skaper flere grenser, noe som kan påvirke gjenkjenningen rundt disse punktene. Standardverdien anbefales i de fleste tilfeller.

## Lokalisert grensesnitt

ASR-modellen i seg selv er **bare for japansk**. Lokaliseringen av README og Colab-grensesnittet dekker alle **183 aktive ISO 639 Set 1-språk** (utdaterte `sh` er ekskludert).

Engelsk (`en`) er den kanoniske oversettelseskilden. Japansk (`ja`) er en gjennomgått oversettelse og kopieres til repository-roten som standardpresentasjonen `README.md`. Den japanske README-filen i roten brukes **ikke** som oversettelseskilde. De øvrige 181 lokalene maskinoversettes fra engelsk.

## Merknader

- Notatboken stopper før transkribering hvis en GPU ikke er tilgjengelig.
- Behandlingstiden avhenger av inndatalengde, innstillinger og GPU-en som Colab tildeler. Første kjøring laster også ned NeMo og modellen på omtrent 1.23 GB.
- Lang lyd behandles i interne chunks, så gjenkjenningen kan påvirkes rundt chunkgrenser.

## Kanonisk kilde og generering

Kanoniske oversettbare kilder:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` er det synkroniserte kanoniske snapshotet. Japansk vedlikeholdes som gjennomgått oversettelse i `locales/ja.json`, og README-snapshotet kopieres til roten som `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Oversettelsesvedlikehold er separat fra vanlig CI. Vanlige brukere og CI trenger ingen oversettelseslegitimasjon.

## Lisens

Notatbokstrukturen og build-/kontrollskriptene er MIT-lisensiert. Third Intelligence-modellen redistribueres ikke her og reguleres av **Apache-2.0**. Tredjepartsavhengigheter beholder sine egne lisenser.
