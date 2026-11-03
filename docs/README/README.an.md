# Haas Japanese Colab

Notebook de Google Colab ta transcribir audio y video en chaponés con Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_an.ipynb)

## Caracteristicas

- **Gratis:** Funciona en o runtime GPU gratis de Google Colab.
- **ASR chaponés:** Fa servir [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modelo d'aproximadament 0.6B parametros ta reconoiximiento de fabla chaponés.
- **Rapido:** A transcripción se puede procesar rapidament.
- **Puntuación:** O modelo produce puntuación chaponés estimada.
- **Marcas de tiempo y subtitols:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Procesamiento de fichers largos:** Tamién se pueden procesar fichers d'audio y video largos.
- **Suporte de Google Drive:** Puya fichers directament u leye-los dende Google Drive; o ZIP de salida se puede alzar opcionalment en Drive.
- **Multiples salidas:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest y ZIP.

## Uso

1. Triga `INPUT_MODE` en **1. Settings** y achusta atras opcions si cal.
2. Triga **Runtime → Run all**.
3. Con `INPUT_MODE = "upload"`, triga os fichers en **2. File selection / Google Drive mount**.
4. O ZIP de salida se descarga automaticament dimpués d'o procesamiento.

## Modos de marcas de tiempo

- `none`: sin información de tiempo.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fichers largos

`CHUNK_SECONDS` controla a duración interna d'os trozos usada ta fichers largos. Valors mas grans reducen os limits y mantienen mas contexto, pero fan cada inferencia mas pesada y pueden aumentar l'uso de memoria GPU. Valors mas chicots fan cada inferencia mas lichera pero crean mas limits, cosa que puede afectar o reconoiximiento arredol d'ixes puntos. En a mayoría d'os casos se recomienda o valor por defecto.

## Interficie localizada

O modelo ASR mesmo ye **nomás ta chaponés**. A localización d'o README y d'a interficie Colab cubre todas as **183 luengas activas d'ISO 639 Set 1** (se excluye `sh`, obsoleta).

L'anglés (`en`) ye a fuent canonica de traducción. O chaponés (`ja`) ye una traducción revisada y se copia en a raíz d'o repositorio como presentación `README.md` por defecto. O README chaponés d'a raíz **no** s'emplega como fuent de traducción. As atras 181 locales son traducidas automaticament dende l'anglés.

## Notas

- O notebook s'atura antes d'a transcripción si no bi ha una GPU disponible.
- O tiempo de procesamiento depende d'a duración d'a dentrada, as opcions y a GPU asignada por Colab. A primera execución tamién descarga NeMo y o modelo d'aproximadament 1.23 GB.
- L'audio largo se procesa en trozos internos, asinas que o reconoiximiento puede quedar afectau cerca d'os limits d'os trozos.

## Fuent canonica y cheneración

Fuents canonicas traducibles:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ye a instantania canonica sincronizada. O chaponés se mantién como traducción revisada en `locales/ja.json`, y a suya instantania README se copia en a raíz como `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

O mantenimiento d'as traduccions ye separau d'o CI ordinario. Os usuarios ordinaris y o CI no amenesten credencials de traducción.

## Licencia

A estructura d'o notebook y os scripts build/check son baixo licencia MIT. O modelo Third Intelligence no se redistribuye aquí y ye gobernau por **Apache-2.0**. As dependencias de tercers mantienen as suyas propias licencias.
