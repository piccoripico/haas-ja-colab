# Haas Japanese Colab

Quasernet Google Colab per transcriure d’àudio e vidèo japonés amb Third Intelligence **Haas-ja-v1.0**.

[![Dobrir dins Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_oc.ipynb)

## Foncionals

- **Gratuit:** Fonciona sul runtime GPU gratuit de Google Colab.
- **ASR japonés:** Utiliza [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modèl d’aperaquí 0.6B paramètres per la reconeissença de paraula japonesa.
- **Rapid:** La transcripcion pòt èsser tractada rapidament.
- **Puntuacion:** Lo modèl produsís una puntuacion japonesa estimada.
- **Marcas temporalas e sostítols:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Tractament de fichièrs longs:** Los fichièrs àudio e vidèo longs pòdon tanben èsser tractats.
- **Supòrt Google Drive:** Cargatz los fichièrs dirèctament o legissètz-los dempuèi Google Drive; lo ZIP de sortida pòt opcionalament èsser enregistrat dins Drive.
- **Sortidas multiplas:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Utilizacion

1. Causissètz `INPUT_MODE` dins **1. Paramètres** e ajustatz los autres paramètres se cal.
2. Causissètz **Runtime → Run all**.
3. Amb `INPUT_MODE = "upload"`, causissètz los fichièrs dins **2. Seleccion de fichièrs / montatge Google Drive**.
4. Lo ZIP de sortida es telecargat automaticament quand lo tractament es acabat.

## Mòdes de marcas temporalas

- `none`: cap d’informacion temporala.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificador

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fichièrs longs

`CHUNK_SECONDS` contraròtla la durada dels tròces intèrnes utilizats pels fichièrs longs. De valors mai grandes redusisson las frontièras e consèrvan mai de contèxte, mas cada inferéncia es mai pesada e pòt utilizar mai de memòria GPU. De valors mai pichonas fan cada inferéncia mai leugièra mas crèan mai de frontièras, çò que pòt afectar la reconeissença a l’entorn d’aqueles punts. La valor per defaut es recomandada dins la màger part dels cases.

## Interfàcia localizada

Lo modèl ASR el meteis es **sonque japonés**. La localizacion del README e de l’interfàcia Colab cobrís totas las **183 lengas activas ISO 639 Set 1** (`sh` obsolet exclus).

L’anglés (`en`) es la font canonica de traduccion. Lo japonés (`ja`) es una traduccion revisada e es copiat a la raiç del depaus coma presentacion `README.md` per defaut. Lo README japonés de raiç **es pas** utilizat coma font de traduccion. Los 181 autres locales son traduches automaticament de l’anglés.

## Nòtas

- Lo quasernet s’arrèsta abans la transcripcion se cap de GPU es pas disponible.
- Lo temps de tractament depend de la longor de l’entrada, dels paramètres e de la GPU atribuida per Colab. La primièra execucion telecarga tanben NeMo e lo modèl d’aperaquí 1.23 GB.
- L’àudio long es tractat en tròces intèrnes, doncas la reconeissença pòt èsser afectada a l’entorn de las frontièras dels tròces.

## Font canonica e generacion

Fonts canonicas tradusiblas:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` es l’instantanèu canonic sincronizat. Lo japonés es mantengut coma traduccion revisada dins `locales/ja.json`, e son instantanèu README es copiat dins `README.md` a la raiç.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

La mantenença de las traduccions es separada del CI ordinari. Los utilizaires ordinaris e lo CI an pas besonh d’identificants de traduccion.

## Licéncia

L’estructura del quasernet e los scripts build/check son jos licéncia MIT. Lo modèl Third Intelligence es pas redistribuit aicí e es regit per **Apache-2.0**. Las dependéncias de tresens consèrvan lors pròprias licéncias.
