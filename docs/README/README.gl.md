# Haas Japanese Colab

Caderno Google Colab para transcribir audio e vídeo en xaponés con Third Intelligence **Haas-ja-v1.0**.

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_gl.ipynb)

## Características

- **Gratuíto:** Execútase no runtime GPU gratuíto de Google Colab.
- **ASR xaponés:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modelo duns 0,6B parámetros para o recoñecemento da fala xaponesa.
- **Rápido:** A transcrición pódese procesar rapidamente.
- **Puntuación:** O modelo produce puntuación xaponesa estimada.
- **Marcas de tempo e subtítulos:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Procesamento de ficheiros longos:** Tamén se poden procesar ficheiros longos de audio e vídeo.
- **Compatibilidade con Google Drive:** Carga ficheiros directamente ou léos desde Google Drive; opcionalmente, o ZIP de saída pódese gardar en Drive.
- **Múltiples saídas:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Uso

1. Escolle `INPUT_MODE` en **1. Settings** e axusta os demais parámetros se é necesario.
2. Selecciona **Runtime → Run all**.
3. Con `INPUT_MODE = "upload"`, escolle os ficheiros en **2. File selection / montaxe de Google Drive**.
4. O ZIP de saída descárgase automaticamente despois do procesamento.

## Modos de marcas de tempo

- `none`: sen información temporal.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificador

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Ficheiros longos

`CHUNK_SECONDS` controla a duración interna dos fragmentos utilizados para ficheiros longos. Os valores máis grandes reducen os límites e conservan máis contexto, pero fan cada inferencia máis pesada e poden aumentar o uso da memoria GPU. Os valores máis pequenos fan cada inferencia máis lixeira pero crean máis límites, o que pode afectar ao recoñecemento arredor deses puntos. Na maioría dos casos recoméndase o valor predeterminado.

## Interface localizada

O modelo ASR en si é **só para xaponés**. A localización de README e da interface de Colab abrangue as **183 linguas activas de ISO 639 Set 1** (exclúese a obsoleta `sh`).

O inglés (`en`) é a fonte canónica de tradución. O xaponés (`ja`) é unha tradución revisada e cópiase á raíz do repositorio como presentación predeterminada de `README.md`. O README xaponés da raíz **non** se usa como fonte de tradución. As outras 181 configuracións rexionais tradúcense automaticamente desde o inglés.

## Notas

- O caderno detense antes da transcrición se non hai un GPU dispoñible.
- O tempo de procesamento depende da duración da entrada, da configuración e do GPU asignado por Colab. Na primeira execución tamén se descargan NeMo e o modelo duns 1.23 GB.
- O audio longo procésase en fragmentos internos, polo que o recoñecemento pode verse afectado arredor dos límites dos fragmentos.

## Fonte canónica e xeración

Fontes canónicas traducibles:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` é a instantánea canónica sincronizada. O xaponés mantense como tradución revisada en `locales/ja.json` e a súa instantánea README cópiase ao `README.md` da raíz.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

O mantemento das traducións está separado da CI ordinaria. Os usuarios normais e a CI non necesitan credenciais de tradución.

## Licenza

A estrutura do caderno e os scripts de compilación/comprobación teñen licenza MIT. O modelo Third Intelligence non se redistribúe aquí e réxese por **Apache-2.0**. As dependencias de terceiros conservan as súas propias licenzas.
