# Haas Japanese Colab

Cuaderno de Google Colab para transcribir audio y vídeo en japonés con Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_es.ipynb)

## Características

- **Gratis:** Funciona en el entorno GPU gratuito de Google Colab.
- **ASR de japonés:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modelo de aproximadamente 0.6B parámetros para reconocimiento de voz japonés.
- **Rápido:** La transcripción puede procesarse con rapidez.
- **Puntuación:** El modelo genera puntuación japonesa estimada.
- **Marcas de tiempo y subtítulos:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Procesamiento de archivos largos:** También se pueden procesar archivos de audio y vídeo largos.
- **Compatibilidad con Google Drive:** Sube archivos directamente o léelos desde Google Drive; el ZIP de salida puede guardarse opcionalmente en Drive.
- **Múltiples salidas:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifiesto y ZIP.

## Uso

1. Elige `INPUT_MODE` en **1. Settings** y ajusta otras opciones si es necesario.
2. Selecciona **Runtime → Run all**.
3. Con `INPUT_MODE = "upload"`, elige archivos en **2. File selection / Google Drive mount**.
4. El ZIP de salida se descarga automáticamente al finalizar el procesamiento.

## Modos de marcas de tiempo

- `none`: sin información temporal.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificador

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Archivos largos

`CHUNK_SECONDS` controla la duración interna de cada fragmento usada para archivos largos. Los valores mayores reducen los límites entre fragmentos y conservan más contexto, pero hacen cada inferencia más pesada y pueden aumentar el uso de memoria GPU. Los valores menores hacen cada inferencia más ligera, pero crean más límites, lo que puede afectar al reconocimiento alrededor de esos puntos. En la mayoría de los casos se recomienda el valor predeterminado.

## Interfaz localizada

El modelo ASR en sí es **solo para japonés**. La localización del README y de la interfaz de Colab cubre los **183 idiomas activos de ISO 639 Set 1** (se excluye el obsoleto `sh`).

El inglés (`en`) es la fuente canónica de traducción. El japonés (`ja`) es una traducción revisada y se copia a la raíz del repositorio como presentación predeterminada `README.md`. El README japonés de la raíz **no** se usa como fuente de traducción. Los otros 181 locales se traducen automáticamente desde el inglés.

## Notas

- El cuaderno se detiene antes de la transcripción si no hay una GPU disponible.
- El tiempo de procesamiento depende de la duración de la entrada, la configuración y la GPU asignada por Colab. La primera ejecución también descarga NeMo y el modelo de aproximadamente 1.23 GB.
- El audio largo se procesa en fragmentos internos, por lo que el reconocimiento puede verse afectado cerca de los límites de los fragmentos.

## Fuente canónica y generación

Fuentes traducibles canónicas:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` es la instantánea canónica sincronizada. El japonés se mantiene como traducción revisada en `locales/ja.json`, y su instantánea del README se copia a la raíz como `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

El mantenimiento de las traducciones está separado de la CI normal. Los usuarios normales y la CI no necesitan credenciales de traducción.

## Licencia

La estructura del cuaderno y los scripts de compilación/comprobación tienen licencia MIT. El modelo de Third Intelligence no se redistribuye aquí y se rige por **Apache-2.0**. Las dependencias de terceros conservan sus propias licencias.
