# Haas Japanese Colab

Google Colab notlibro por transskribar Japoniana audio e video per Third Intelligence **Haas-ja-v1.0**.

[![Apertar en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_io.ipynb)

## Traiti

- **Gratis:** Funkcionas en la gratis GPU-runtime di Google Colab.
- **Japoniana ASR:** Uzas [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modelo kun cirkum 0.6B parametri por rekonocar Japoniana parolado.
- **Rapida:** La transskribo povas esar procesata rapide.
- **Punktizo:** La modelo produktas estimita Japoniana punktizo.
- **Tempostampi e subtituli:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Procesado di longa faili:** Longa audio- e video-faili povas anke esar procesata.
- **Google Drive-suporto:** Charjez faili direkte o lektez oli de Google Drive; la rezulto-ZIP povas optionale esar konservata en Drive.
- **Plura rezultati:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Uzado

1. Selektez `INPUT_MODE` en **1. Ajusti** e ajustez altra ajusti se bezonata.
2. Selektez **Runtime → Run all**.
3. Kun `INPUT_MODE = "upload"`, selektez faili en **2. Fail-selekto / Google Drive-munto**.
4. La rezulto-ZIP esas automate deskargata pos la procesado finas.

## Tempostamp-modi

- `none`: nula tempo-informo.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekodilo

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Longa faili

`CHUNK_SECONDS` kontrolas la interna blok-durado uzata por longa faili. Plu granda valori reduktas bordi e konservas plu multa kontexto, ma singla infero esas plu peza e povas uzar plu multa GPU-memoro. Plu mikra valori facas singla infero plu lejera ma kreas plu multa bordi, quo povas influar rekonoco cirkum ta punti. La predefinita valoro esas rekomendata en la majoritato di kazi.

## Lokalizita interfaso

La ASR-modelo ipsa esas **nur Japoniana**. Lokalizo di README e Colab-interfaso kovras omna **183 aktiva lingui ISO 639 Set 1** (obsoleta `sh` exkluzita).

Angla (`en`) esas la kanonika traduk-fonti. Japoniana (`ja`) esas reviziita traduko e esas kopiita a la radiko di la repository kom predefinita prezento `README.md`. La radika Japoniana README **ne** esas uzata kom traduk-fonti. La altra 181 locali esas mashin-tradukita de Angla.

## Noti

- La notlibro haltas ante transskribo se nula GPU esas disponebla.
- Proces-tempo dependas de input-longeso, ajusti e la GPU asignata da Colab. La unesma exekuto anke deskargas NeMo e la cirkum 1.23 GB modelo.
- Longa audio esas procesata en interna bloki, do rekonoco povas esar influata cirkum blok-bordi.

## Kanonika fonti e generado

Kanonika tradukebla fonti:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` esas la sinkronizita kanonika snapshot. Japoniana esas mantenata kom reviziita traduko en `locales/ja.json`, e olia README-snapshot esas kopiita a radika `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Traduk-mantenado esas separata de ordinara CI. Ordinara uzanti e CI ne bezonas traduk-kredenciali.

## Licenco

La notlibro-skeleto e build/check-skripti esas licencita sub MIT. La Third Intelligence-modelo ne esas redistribuata hike e esas regulata per **Apache-2.0**. Triaparta dependaji retenas lia propra licenci.
