# Haas Japanese Colab

Google Colab-notebook til transskribering af japansk lyd og video med Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_da.ipynb)

## Funktioner

- **Gratis:** Kører på Google Colabs gratis GPU-runtime.
- **Japansk ASR:** Bruger [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), en model med cirka 0.6B parametre til japansk talegenkendelse.
- **Hurtig:** Transskribering kan behandles hurtigt.
- **Tegnsætning:** Modellen leverer estimeret japansk tegnsætning.
- **Tidsstempler og undertekster:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Behandling af lange filer:** Lange lyd- og videofiler kan også behandles.
- **Google Drive-understøttelse:** Upload filer direkte eller læs dem fra Google Drive; output-ZIP kan valgfrit gemmes på Drive.
- **Flere outputformater:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest og ZIP.

## Brug

1. Vælg `INPUT_MODE` under **1. Settings**, og juster andre indstillinger om nødvendigt.
2. Vælg **Runtime → Run all**.
3. Med `INPUT_MODE = "upload"` vælges filer under **2. File selection / Google Drive mount**.
4. Output-ZIP downloades automatisk, når behandlingen er færdig.

## Tidsstempeltilstande

- `none`: ingen tidsinformation.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lange filer

`CHUNK_SECONDS` styrer den interne chunkvarighed for lange filer. Større værdier reducerer grænser og bevarer mere kontekst, men gør hver inferens tungere og kan øge GPU-hukommelsesforbruget. Mindre værdier gør hver inferens lettere, men skaber flere grænser, hvilket kan påvirke genkendelsen omkring disse punkter. Standardværdien anbefales i de fleste tilfælde.

## Lokaliseret brugerflade

Selve ASR-modellen er **kun japansk**. Lokaliseringen af README og Colab-brugerfladen dækker alle **183 aktive ISO 639 Set 1-sprog** (forældede `sh` er udeladt).

Engelsk (`en`) er den kanoniske oversættelseskilde. Japansk (`ja`) er en gennemgået oversættelse og kopieres til repository-roden som standardvisningen `README.md`. Den japanske README i roden bruges **ikke** som oversættelseskilde. De øvrige 181 locales maskinoversættes fra engelsk.

## Bemærkninger

- Notebooken stopper før transskribering, hvis en GPU ikke er tilgængelig.
- Behandlingstiden afhænger af inputlængde, indstillinger og den GPU, som Colab tildeler. Første kørsel downloader også NeMo og modellen på cirka 1.23 GB.
- Lang lyd behandles i interne chunks, så genkendelsen kan påvirkes omkring chunkgrænser.

## Kanonisk kilde og generering

Kanoniske oversættelige kilder:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` er det synkroniserede kanoniske snapshot. Japansk vedligeholdes som en gennemgået oversættelse i `locales/ja.json`, og dens README-snapshot kopieres til roden som `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Oversættelsesvedligeholdelse er adskilt fra almindelig CI. Almindelige brugere og CI behøver ikke oversættelseslegitimationsoplysninger.

## Licens

Notebook-strukturen og build-/kontrolscripts er MIT-licenserede. Third Intelligence-modellen redistribueres ikke her og er underlagt **Apache-2.0**. Tredjepartsafhængigheder beholder deres egne licenser.
