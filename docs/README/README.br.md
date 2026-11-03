# Haas Japanese Colab

Notenn Colab Google evit treuzskrivañ audio ha video japanek gant Third Intelligence **Haas-ja-v1.0**.

[![Digeriñ e Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_br.ipynb)

## Perzhioù

- **Digoust:** A ya war runtime GPU digoust Google Colab.
- **ASR japanek:** A implij [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), ur model war-dro 0.6B arventenn evit anavezout komz japanek.
- **Buan:** Gallout a reer ober an treuzskrivadur buan.
- **Poentadur:** Ar model a ro poentadur japanek brasjedet.
- **Merkoù-amzer ha istitloù:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Restroù hir:** Gallout a reer ivez tretañ restroù audio ha video hir.
- **Skor Google Drive:** Pellgargit restroù war-eeun pe lennit anezho diwar Google Drive; gallout a reer ivez enrollañ an ZIP disoc’h e Drive.
- **Meur a ezvont:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ha ZIP.

## Implij

1. Dibabit `INPUT_MODE` e **1. Arventennoù** ha reizhit an arventennoù all ma vez ezhomm.
2. Dibabit **Runtime → Run all**.
3. Gant `INPUT_MODE = "upload"`, dibabit restroù e **2. Dibab restroù / stagañ Google Drive**.
4. An ZIP ezvont a vez pellgarget ent emgefreek goude ma echu an tretiñ.

## Modoù merkoù-amzer

- `none`: merkoù-amzer ebet.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dikoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Restroù hir

`CHUNK_SECONDS` a reol hirder ar rannadoù diabarzh implijet evit restroù hir. Talvoudoù brasoc’h a zigresk an harzoù hag a vir muioc’h a gendestenn, met pounneroc’h eo pep inferañs ha muioc’h a vemor GPU a c’hall implijout. Talvoudoù bihanoc’h a laka pep inferañs da vezañ skañvoc’h met a grou muioc’h a harzoù, hag ar re-se a c’hall levezoniñ an anavezout en-dro dezho. Er pep brasañ eus an degouezhioù e vez erbedet an talvoud dre ziouer.

## Etrefas lec’helaet

Ar model ASR e-unan zo **evit ar japaneg hepken**. Lec’helaat README hag etrefas Colab a c’holo an holl **183 yezh oberiant ISO 639 Set 1** (`sh` diamzeret lakaet er-maez).

Ar saozneg (`en`) eo ar mammenn droidigezh kanonek. Ar japaneg (`ja`) zo un droidigezh adwelet ha kopiet e gwrizienn ar mirlec’h evel kinnig `README.md` dre ziouer. README japanek ar gwrizienn **ne vez ket** implijet evel mammenn droidigezh. An 181 locale all zo troet dre mekanik diwar ar saozneg.

## Notennoù

- An notenn a chom a-raok an treuzskrivadur ma n’eus GPU ebet hegerz.
- An amzer tretiñ a zalc’h ouzh hirder an enank, an arventennoù hag ar GPU roet gant Colab. Er redadenn gentañ e vez pellgarget ivez NeMo hag ar model war-dro 1.23 GB.
- Audio hir a vez tretet e rannadoù diabarzh, setu e c’hall an anavezout bezañ levezonet en-dro d’an harzoù rann.

## Mammenn kanonek ha genel

Mammennoù kanonek a c’haller treiñ:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` eo an arvest kanonek sinkronelaet. Ar japaneg a vez dalc’het evel droidigezh adwelet e `locales/ja.json`, hag arvest e README a vez kopiet da `README.md` er gwrizienn.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Dalc’h an droidigezh zo disrann diouzh CI boutin. N’eus ket ezhomm kredañsoù droidigezh gant an implijerien boutin nag ar CI.

## Aotre

Framm an notenn ha skriptoù sevel/gwiriañ zo dindan aotre MIT. Model Third Intelligence ne vez ket adskignet amañ hag eo renet gant **Apache-2.0**. Pep dibendendiñ trede-parti a vir e aotre dezhañ.
