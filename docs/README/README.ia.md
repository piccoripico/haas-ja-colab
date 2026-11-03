# Haas Japanese Colab

Notebook Google Colab pro transcriber audio e video japonese con Third Intelligence **Haas-ja-v1.0**.

[![Aperir in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ia.ipynb)

## Characteristicas

- **Gratuite:** Functiona in le runtime GPU gratuite de Google Colab.
- **ASR japonese:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modello de circa 0.6B parametros pro recognition de parola japonese.
- **Rapide:** Le transcription pote esser processate rapidemente.
- **Punctuation:** Le modello produce punctuation japonese estimate.
- **Marcas de tempore e subtitulos:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Processamento de files longe:** Files audio e video longe pote esser processate tamben.
- **Supporto Google Drive:** Carga files directemente o lege los ex Google Drive; le ZIP de output pote optionalmente esser salvate in Drive.
- **Output multiple:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, e ZIP.

## Uso

1. Selige `INPUT_MODE` in **1. Configurationes** e ajusta altere configurationes si necessari.
2. Selige **Runtime → Run all**.
3. Con `INPUT_MODE = "upload"`, selige files in **2. Selection de files / montage de Google Drive**.
4. Le ZIP de output es discargate automaticamente post le fin del processamento.

## Modos de marcas de tempore

- `none`: nulle information temporal.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificator

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files longe

`CHUNK_SECONDS` controla le duration del blocos interne usate pro files longe. Valores plus grande reduce le limites e conserva plus contexto, ma cata inference es plus pesante e pote usar plus memoria GPU. Valores plus parve rende cata inference plus legier ma crea plus limites, lo que pote influentiar le recognition circa ille punctos. Le valor predefinite es recommendate in le major parte del casos.

## Interfacie localisate

Le modello ASR mesme es **solmente japonese**. Le localisation del README e del interfacie Colab coperi tote le **183 linguas active ISO 639 Set 1** (`sh` obsolete excludite).

Anglese (`en`) es le fonte canonic de traduction. Japonese (`ja`) es un traduction revidite e es copiate al radice del repositorio como presentation `README.md` predefinite. Le README japonese al radice **non** es usate como fonte de traduction. Le altere 181 locales es traducite automaticamente ex anglese.

## Notas

- Le notebook se stoppa ante le transcription si nulle GPU es disponibile.
- Le tempore de processamento depende del longitude del input, del configurationes, e del GPU assignate per Colab. Le prime execution discarga tamben NeMo e le modello de circa 1.23 GB.
- Audio longe es processate in blocos interne, assi le recognition pote esser influentiate circa limites de blocos.

## Fonte canonic e generation

Fontes canonic traducibile:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` es le snapshot canonic synchronisate. Japonese es mantenite como traduction revidite in `locales/ja.json`, e su snapshot README es copiate a `README.md` al radice.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Le mantenimento de traductiones es separate del CI ordinari. Usatores ordinari e CI non necessita credentiales de traduction.

## Licentia

Le structura del notebook e le scripts de build/check es sub licentia MIT. Le modello Third Intelligence non es redistribuite hic e es governate per **Apache-2.0**. Dependentias de tertie partes conserva lor proprie licentias.
