# Haas Japanese Colab

Notebook ta’ Google Colab biex tittraskrivi awdjo u vidjo Ġappuniż b’Third Intelligence **Haas-ja-v1.0**.

[![Iftaħ f’Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_mt.ipynb)

## Karatteristiċi

- **B’xejn:** Jaħdem fuq ir-runtime GPU b’xejn ta’ Google Colab.
- **ASR Ġappuniż:** Juża [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), mudell ta’ madwar 0.6B parametru għar-rikonoxximent tad-diskors Ġappuniż.
- **Mgħaġġel:** It-traskrizzjoni tista’ tiġi pproċessata malajr.
- **Punteġġjatura:** Il-mudell joħroġ punteġġjatura Ġappuniża stmata.
- **Timestamps u sottotitli:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ipproċessar ta’ fajls twal:** Jistgħu jiġu pproċessati wkoll fajls twal tal-awdjo u tal-vidjo.
- **Appoġġ għal Google Drive:** Tella’ fajls direttament jew aqrahom minn Google Drive; il-ZIP tal-output jista’ jiġi ssejvjat f’Drive b’mod fakultattiv.
- **Outputs multipli:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, u ZIP.

## Użu

1. Agħżel `INPUT_MODE` f’**1. Settings** u aġġusta settings oħra jekk meħtieġ.
2. Agħżel **Runtime → Run all**.
3. B’`INPUT_MODE = "upload"`, agħżel fajls f’**2. Għażla tal-fajls / immuntar ta’ Google Drive**.
4. Il-ZIP tal-output jitniżżel awtomatikament wara li jintemm l-ipproċessar.

## Modi tat-timestamp

- `none`: l-ebda informazzjoni dwar il-ħin.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fajls twal

`CHUNK_SECONDS` jikkontrolla t-tul tal-chunk intern użat għal fajls twal. Valuri akbar inaqqsu l-konfini u jżommu aktar kuntest, iżda kull inference tkun itqal u tista’ tuża aktar memorja GPU. Valuri iżgħar jagħmlu kull inference eħfef iżda joħolqu aktar konfini, li jistgħu jaffettwaw ir-rikonoxximent madwar dawk il-punti. Il-valur default huwa rakkomandat fil-biċċa l-kbira tal-każijiet.

## Interfaċċa lokalizzata

Il-mudell ASR innifsu huwa **Ġappuniż biss**. Il-lokalizzazzjoni tar-README u tal-interfaċċa Colab tkopri l-**183 lingwa attiva ISO 639 Set 1** kollha (`sh` skadut eskluż).

L-Ingliż (`en`) huwa s-sors kanoniku tat-traduzzjoni. Il-Ġappuniż (`ja`) huwa traduzzjoni riveduta u jiġi kkupjat fl-għerq tar-repożitorju bħala l-preżentazzjoni default `README.md`. Ir-README Ġappuniż tal-għerq **ma jintużax** bħala sors tat-traduzzjoni. Il-181 locale l-oħra huma tradotti bil-magna mill-Ingliż.

## Noti

- In-notebook jieqaf qabel it-traskrizzjoni jekk GPU ma tkunx disponibbli.
- Il-ħin tal-ipproċessar jiddependi mit-tul tal-input, is-settings, u l-GPU assenjata minn Colab. L-ewwel run iniżżel ukoll NeMo u l-mudell ta’ madwar 1.23 GB.
- Awdjo twil jiġi pproċessat f’chunks interni, għalhekk ir-rikonoxximent jista’ jiġi affettwat madwar il-konfini tal-chunks.

## Sors kanoniku u ġenerazzjoni

Sorsi kanoniċi li jistgħu jiġu tradotti:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` huwa s-snapshot kanoniku sinkronizzat. Il-Ġappuniż jinżamm bħala traduzzjoni riveduta f’`locales/ja.json`, u s-snapshot README tiegħu jiġi kkupjat għal `README.md` fl-għerq.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Il-manutenzjoni tat-traduzzjoni hija separata mis-CI ordinarju. Utenti ordinarji u CI m’għandhomx bżonn kredenzjali tat-traduzzjoni.

## Liċenzja

L-istruttura tan-notebook u l-build/check scripts huma liċenzjati taħt MIT. Il-mudell Third Intelligence ma jiġix ridistribwit hawn u huwa rregolat minn **Apache-2.0**. Dipendenzi ta’ partijiet terzi jżommu l-liċenzji tagħhom.
