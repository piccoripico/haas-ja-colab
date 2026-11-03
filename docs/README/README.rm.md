# Haas Japanese Colab

Notebook Google Colab per transcriver audio e video giapunais cun Third Intelligence **Haas-ja-v1.0**.

[![Avrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_rm.ipynb)

## Caracteristicas

- **Gratuit:** Cursa sin il runtime GPU gratuit da Google Colab.
- **ASR giapunais:** Dovra [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), in model cun circa 0.6B parameters per la renconuschientscha da lingua giapunaisa.
- **Svelt:** La transcripziun po vegnir elavurada svelt.
- **Punctuaziun:** Il model producescha punctuaziun giapunaisa stimada.
- **Marcaziuns da temp e suttitels:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Elavuraziun da datotecas lungas:** Er datotecas audio e video lungas pon vegnir elavuradas.
- **Sustegn Google Drive:** Chargiai datotecas directamain u legiai ellas da Google Drive; il ZIP d’output po vegnir memorisà opziunalmain en Drive.
- **Plirs outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Utilisaziun

1. Tscherna `INPUT_MODE` en **1. Parameters** ed adatta auters parameters sche necessari.
2. Tscherna **Runtime → Run all**.
3. Cun `INPUT_MODE = "upload"`, tscherna datotecas en **2. Selecziun da datotecas / montar Google Drive**.
4. Il ZIP d’output vegn telechargià automaticamain suenter che l’elavuraziun è terminada.

## Modus da marcaziuns da temp

- `none`: naginas infurmaziuns da temp.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodader

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Datotecas lungas

`CHUNK_SECONDS` controllescha la durada dals tocs interns duvrads per datotecas lungas. Valurs pli grondas reduceschan cunfins e mantegnan dapli context, ma mintga inferenza è pli greva e po duvrar dapli memoria GPU. Valurs pli pitschnas fan mintga inferenza pli leva, ma creeschan dapli cunfins che pon influenzar la renconuschientscha enturn quels puncts. La valur standard vegn recumandada en la gronda part dals cas.

## Interfatscha localisada

Il model ASR sez è **mo giapunais**. La localisaziun dal README e da l’interfatscha Colab cuvra tut las **183 linguas activas ISO 639 Set 1** (`sh` obsolet exclus).

Englais (`en`) è la funtauna canonica da translaziun. Giapunais (`ja`) è ina translaziun revisada e vegn copià a la ragisch dal repositori sco preschentaziun standard `README.md`. Il README giapunais da la ragisch **na vegn betg** duvrà sco funtauna da translaziun. Ils auters 181 locales vegnan translatads automaticamain da l’englais.

## Remartgas

- Il notebook sa ferma avant la transcripziun sche nagina GPU è disponibla.
- Il temp d’elavuraziun dependa da la lunghezza da l’input, dals parameters e da la GPU attribuida da Colab. L’emprima execuziun telechargia era NeMo ed il model da circa 1.23 GB.
- Audio lung vegn elavurà en tocs interns, uschia che la renconuschientscha po vegnir influenzada enturn ils cunfins dals tocs.

## Funtauna canonica e generaziun

Funtaunas canonicas translatablas:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` è il snapshot canonic sincronisà. Giapunais vegn mantegnì sco translaziun revisada en `locales/ja.json`, ed il snapshot README vegn copià a `README.md` a la ragisch.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

La mantegnida da translaziuns è separada dal CI ordinari. Utilisaders ordinaris e CI na dovran naginas credenzialas da translaziun.

## Licenza

La structura dal notebook e scripts build/check èn sut licenza MIT. Il model Third Intelligence na vegn betg redistribuì qua ed è reglà da **Apache-2.0**. Dependenzas da terzas partidas mantegnan lur atgnas licenzas.
