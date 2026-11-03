# Haas Japanese Colab

Notebook Google Colab per trascrive audio è video giappunesi cù Third Intelligence **Haas-ja-v1.0**.

[![Apre in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_co.ipynb)

## Funziunalità

- **Gratuitu:** Funziona nantu à u runtime GPU gratuitu di Google Colab.
- **ASR giappunesu:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un mudellu d circa 0.6B parametri per a ricunniscenza vocale giappunese.
- **Rapidu:** A trascrizzione pò esse trattata rapidamente.
- **Puntuazione:** U mudellu produce puntuazione giappunese stimata.
- **Timestamp è sottutituli:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Trattamentu di fugliali longhi:** Si ponu trattà ancu fugliali audio è video longhi.
- **Supportu Google Drive:** Caricate i fugliali direttamente o leghjiteli da Google Drive; u ZIP d’uscita pò esse salvatu opzionalmente in Drive.
- **Parechje uscite:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest è ZIP.

## Usu

1. Sceglite `INPUT_MODE` in **1. Impostazioni** è aghjustate l’altre impostazioni s’ellu ci vole.
2. Sceglite **Runtime → Run all**.
3. Cù `INPUT_MODE = "upload"`, sceglite i fugliali in **2. Selezzione di fugliali / muntatura Google Drive**.
4. U ZIP d’uscita hè scaricatu automaticamente dopu a fine di u trattamentu.

## Modi timestamp

- `none`: nisuna infurmazione di tempu.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificatore

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fugliali longhi

`CHUNK_SECONDS` cuntrolla a durata di i blocchi interni usati per i fugliali longhi. Valori più grandi riducenu i cunfini è mantenenu più cuntestu, ma ogni inferenza hè più pesante è pò aduprà più memoria GPU. Valori più chjuchi rendenu ogni inferenza più ligera ma creanu più cunfini, chì ponu influenzà a ricunniscenza vicinu à quelli punti. U valore predefinitu hè cunsigliatu in a maiò parte di i casi.

## Interfaccia lucalizata

U mudellu ASR stessu hè **solu giappunesu**. A lucalizazione di README è di l’interfaccia Colab copre tutte e **183 lingue attive ISO 639 Set 1** (`sh` obsoletu esclusu).

L’inglese (`en`) hè a fonte canonica di traduzzione. U giappunesu (`ja`) hè una traduzzione rivista è hè cupiatu à a radica di u repositoriu cum’è presentazione predefinita `README.md`. U README giappunesu di radica **ùn hè micca** adupratu cum’è fonte di traduzzione. L’altri 181 locale sò tradutti automaticamente da l’inglese.

## Note

- U notebook si ferma prima di a trascrizzione s’ellu ùn ci hè micca GPU dispunibile.
- U tempu di trattamentu dipende da a durata di l’input, l’impostazioni è a GPU assignata da Colab. U primu avviu scarica ancu NeMo è u mudellu d circa 1.23 GB.
- L’audio longu hè trattatu in blocchi interni, cusì a ricunniscenza pò esse influenzata vicinu à i cunfini di bloccu.

## Fonte canonica è generazione

Fonti canoniche traducibili:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` hè u snapshot canonicu sincronizatu. U giappunesu hè mantenutu cum’è traduzzione rivista in `locales/ja.json`, è u so snapshot README hè cupiatu à `README.md` à a radica.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

A manutenzione di e traduzzioni hè separata da u CI ordinariu. L’utilizatori ordinarii è u CI ùn anu bisognu di credenziali di traduzzione.

## Licenza

A struttura di u notebook è i script di build/check sò sottu licenza MIT. U mudellu Third Intelligence ùn hè micca ridistribuitu quì è hè guvernatu da **Apache-2.0**. E dipendenze di terze parti mantenenu e so licenze.
