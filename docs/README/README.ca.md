# Haas Japanese Colab

Quadern Google Colab per transcriure àudio i vídeo en japonès amb Third Intelligence **Haas-ja-v1.0**.

[![Obre a Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ca.ipynb)

## Característiques

- **Gratuït:** S’executa al runtime GPU gratuït de Google Colab.
- **ASR japonès:** Utilitza [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un model d’aproximadament 0,6B paràmetres per al reconeixement de parla japonesa.
- **Ràpid:** La transcripció es pot processar ràpidament.
- **Puntuació:** El model genera puntuació japonesa estimada.
- **Marques de temps i subtítols:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Processament de fitxers llargs:** També es poden processar fitxers d’àudio i vídeo llargs.
- **Compatibilitat amb Google Drive:** Puja fitxers directament o llegeix-los des de Google Drive; opcionalment, el ZIP de sortida es pot desar a Drive.
- **Múltiples sortides:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest i ZIP.

## Ús

1. Tria `INPUT_MODE` a **1. Settings** i ajusta la resta de configuracions si cal.
2. Selecciona **Runtime → Run all**.
3. Amb `INPUT_MODE = "upload"`, tria els fitxers a **2. File selection / muntatge de Google Drive**.
4. El ZIP de sortida es descarrega automàticament després del processament.

## Modes de marques de temps

- `none`: sense informació temporal.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Descodificador

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fitxers llargs

`CHUNK_SECONDS` controla la durada interna dels fragments utilitzats per a fitxers llargs. Els valors més grans redueixen els límits i conserven més context, però fan cada inferència més pesada i poden augmentar l’ús de memòria GPU. Els valors més petits fan cada inferència més lleugera però creen més límits, cosa que pot afectar el reconeixement al voltant d’aquests punts. En la majoria de casos es recomana el valor predeterminat.

## Interfície localitzada

El model ASR és **només per al japonès**. La localització de README i de la interfície de Colab cobreix les **183 llengües actives de ISO 639 Set 1** (s’exclou l’obsolet `sh`).

L’anglès (`en`) és la font canònica de traducció. El japonès (`ja`) és una traducció revisada i es copia a l’arrel del repositori com a presentació predeterminada de `README.md`. El README japonès de l’arrel **no** s’utilitza com a font de traducció. Les altres 181 configuracions regionals es tradueixen automàticament des de l’anglès.

## Observacions

- El quadern s’atura abans de la transcripció si no hi ha cap GPU disponible.
- El temps de processament depèn de la durada de l’entrada, la configuració i el GPU assignat per Colab. La primera execució també descarrega NeMo i el model d’aproximadament 1.23 GB.
- L’àudio llarg es processa en fragments interns, de manera que el reconeixement es pot veure afectat prop dels límits dels fragments.

## Font canònica i generació

Fonts canòniques traduïbles:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` és la instantània canònica sincronitzada. El japonès es manté com a traducció revisada a `locales/ja.json`, i la seva instantània README es copia al `README.md` de l’arrel.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

El manteniment de les traduccions és independent de la CI ordinària. Els usuaris normals i la CI no necessiten credencials de traducció.

## Llicència

L’estructura del quadern i els scripts de compilació/verificació tenen llicència MIT. El model Third Intelligence no es redistribueix aquí i es regeix per **Apache-2.0**. Les dependències de tercers conserven les seves pròpies llicències.
