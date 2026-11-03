# Haas Japanese Colab

Google Colab-notebook för transkribering av japanskt ljud och video med Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sv.ipynb)

## Funktioner

- **Gratis:** Körs i Google Colabs kostnadsfria GPU-miljö.
- **Japansk ASR:** Använder [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), en modell med cirka 0.6B parametrar för japansk taligenkänning.
- **Snabb:** Transkribering kan behandlas snabbt.
- **Interpunktion:** Modellen ger uppskattad japansk interpunktion.
- **Tidsstämplar och undertexter:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Bearbetning av långa filer:** Även långa ljud- och videofiler kan bearbetas.
- **Google Drive-stöd:** Ladda upp filer direkt eller läs dem från Google Drive; utdata-ZIP kan valfritt sparas på Drive.
- **Flera utdataformat:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest och ZIP.

## Användning

1. Välj `INPUT_MODE` under **1. Settings** och justera andra inställningar vid behov.
2. Välj **Runtime → Run all**.
3. Med `INPUT_MODE = "upload"` väljer du filer under **2. File selection / Google Drive mount**.
4. Utdata-ZIP laddas ned automatiskt när bearbetningen är klar.

## Tidsstämpellägen

- `none`: ingen tidsinformation.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Avkodare

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Långa filer

`CHUNK_SECONDS` styr den interna chunklängden för långa filer. Större värden minskar antalet gränser och bevarar mer kontext, men gör varje inferens tyngre och kan öka GPU-minnesanvändningen. Mindre värden gör varje inferens lättare men skapar fler gränser, vilket kan påverka igenkänningen runt dessa punkter. Standardvärdet rekommenderas i de flesta fall.

## Lokaliserat gränssnitt

ASR-modellen i sig är **endast för japanska**. Lokaliseringen av README och Colab-gränssnittet omfattar alla **183 aktiva ISO 639 Set 1-språk** (det föråldrade `sh` är uteslutet).

Engelska (`en`) är den kanoniska översättningskällan. Japanska (`ja`) är en granskad översättning och kopieras till repository-roten som standardpresentationen `README.md`. Den japanska README-filen i roten används **inte** som översättningskälla. De övriga 181 lokalerna maskinöversätts från engelska.

## Anmärkningar

- Notebooken stoppar före transkribering om ingen GPU är tillgänglig.
- Bearbetningstiden beror på inmatningslängd, inställningar och den GPU som Colab tilldelar. Första körningen laddar dessutom ned NeMo och modellen på cirka 1.23 GB.
- Långt ljud bearbetas i interna chunks, så igenkänningen kan påverkas runt chunkgränser.

## Kanonisk källa och generering

Kanoniska översättningsbara källor:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` är den synkroniserade kanoniska snapshoten. Japanska underhålls som granskad översättning i `locales/ja.json`, och dess README-snapshot kopieras till roten som `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Översättningsunderhåll är separat från vanlig CI. Vanliga användare och CI behöver inga översättningsuppgifter.

## Licens

Notebookstrukturen och build-/kontrollskripten är MIT-licensierade. Third Intelligence-modellen distribueras inte vidare här och omfattas av **Apache-2.0**. Tredjepartsberoenden behåller sina egna licenser.
