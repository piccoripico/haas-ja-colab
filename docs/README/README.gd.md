# Haas Japanese Colab

Leabhar-nota Google Colab airson fuaim is bhidio Iapanach ath-sgrìobhadh le Third Intelligence **Haas-ja-v1.0**.

[![Fosgail ann an Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_gd.ipynb)

## Feartan

- **An-asgaidh:** Ruithidh e air runtime GPU an-asgaidh aig Google Colab.
- **ASR Iapanach:** Cleachdaidh e [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modail le mu 0.6B paramadair airson aithneachadh cainnt Iapanach.
- **Luath:** Faodar an tar-sgrìobhadh a phròiseasadh gu luath.
- **Puingeachadh:** Bheir am modail a-mach puingeachadh Iapanach tuairmseach.
- **Comharran-ama agus fo-thiotalan:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pròiseasadh fhaidhlichean fada:** Faodar faidhlichean fuaime is bhidio fada a phròiseasadh cuideachd.
- **Taic Google Drive:** Luchdaich faidhlichean suas gu dìreach no leugh iad à Google Drive; faodar an ZIP toraidh a shàbhaladh gu Drive ma thogras tu.
- **Iomadh toradh:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest agus ZIP.

## Cleachdadh

1. Tagh `INPUT_MODE` ann an **1. Settings** agus atharraich na roghainnean eile ma tha feum air.
2. Tagh **Runtime → Run all**.
3. Le `INPUT_MODE = "upload"`, tagh faidhlichean ann an **2. File selection / mount Google Drive**.
4. Thèid an ZIP toraidh a luchdachadh sìos gu fèin-obrachail às dèidh a’ phròiseasaidh.

## Modhan chomharran-ama

- `none`: gun fhiosrachadh-ama.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dì-chòdair

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Faidhlichean fada

Bidh `CHUNK_SECONDS` a’ cumail smachd air fad nan chunk a-staigh airson faidhlichean fada. Lùghdaichidh luachan nas motha crìochan agus cumaidh iad barrachd co-theacsa, ach nì iad gach inference nas truime agus dh’fhaodadh iad barrachd cuimhne GPU a chleachdadh. Nì luachan nas lugha gach inference nas aotroime ach cruthaichidh iad barrachd chrìochan, agus dh’fhaodadh sin buaidh a thoirt air aithneachadh timcheall nan puingean sin. Thathar a’ moladh an luach bunaiteach sa mhòr-chuid de chùisean.

## Eadar-aghaidh ionadail

Tha am modail ASR fhèin **airson Seapanais a-mhàin**. Tha ionadail README agus UI Colab a’ còmhdach nan **183 cànan gnìomhach ISO 639 Set 1** uile (`sh` seann-fhasanta air a dùnadh a-mach).

Is e Beurla (`en`) an tùs eadar-theangachaidh canonical. Tha Seapanais (`ja`) na h-eadar-theangachadh ath-sgrùdaichte agus thèid a copachadh gu freumh an repository mar an taisbeanadh `README.md` bunaiteach. **Cha tèid** an README Seapanach sa fhreumh a chleachdadh mar thùs eadar-theangachaidh. Tha na 181 locale eile air an eadar-theangachadh gu fèin-obrachail bhon Bheurla.

## Notaichean

- Stadaidh an leabhar-nota mus tòisich an tar-sgrìobhadh mura h-eil GPU ri fhaighinn.
- Tha ùine a’ phròiseasaidh an urra ri fad an ion-chuir, na roghainnean agus an GPU a shònraicheas Colab. Air a’ chiad ruith thèid NeMo agus am modail mu 1.23 GB a luchdachadh sìos cuideachd.
- Thèid fuaim fhada a phròiseasadh ann an chunks a-staigh, agus mar sin dh’fhaodadh buaidh a bhith air aithneachadh timcheall chrìochan nan chunks.

## Tùs canonical agus gineadh

Tùsan canonical a ghabhas eadar-theangachadh:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Is e `locales/en.json` an snapshot canonical sioncronaichte. Tha Seapanais air a cumail mar eadar-theangachadh ath-sgrùdaichte ann an `locales/ja.json`, agus thèid an snapshot README aice a chopaigeadh gu `README.md` sa fhreumh.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Tha cumail suas eadar-theangachaidh air leth bho CI àbhaisteach. Chan fheum luchd-cleachdaidh àbhaisteach no CI teisteanasan eadar-theangachaidh.

## Ceadachas

Tha structar an leabhair-nota agus na scripts build/check fo chead MIT. Chan eil am modail Third Intelligence air ath-sgaoileadh an seo agus tha e fo **Apache-2.0**. Cumaidh eisimeileachdan treas-phàrtaidh na ceadan aca fhèin.
