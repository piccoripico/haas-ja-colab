# Haas Japanese Colab

Deftera Google Colab ji bo nivîsandina deng û vîdyoya Japonî bi Third Intelligence **Haas-ja-v1.0**.

[![Di Colab de veke](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ku.ipynb)

## Taybetmendî

- **Belaş:** Li runtime GPU ya belaş a Google Colab dixebite.
- **ASR ya Japonî:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) bi kar tîne, modeleke nêzî 0.6B parametreyan ji bo nasîna axaftina Japonî.
- **Bilez:** Transkripsiyon dikare bilez were pêvajokirin.
- **Xaldayîn:** Model xaldayîna Japonî ya texmînkirî derdixe.
- **Demnîşan û binnivîs:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pêvajokirina pelên dirêj:** Pelên deng û vîdyoyê yên dirêj jî dikarin werin pêvajokirin.
- **Piştgiriya Google Drive:** Pelan rasterast bar bike an ji Google Drive bixwîne; ZIP ya derketinê dikare bi bijartin li Drive were tomarkirin.
- **Derketinên pir:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest û ZIP.

## Bikaranîn

1. `INPUT_MODE` di **1. Settings** de hilbijêre û heke pêwîst be mîhengên din biguherîne.
2. **Runtime → Run all** hilbijêre.
3. Bi `INPUT_MODE = "upload"`, pelan di **2. File selection / mount Google Drive** de hilbijêre.
4. ZIP ya derketinê piştî pêvajokirinê xweber tê daxistin.

## Modên demnîşanê

- `none`: agahdariya demê tune.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Pelên dirêj

`CHUNK_SECONDS` dirêjahiya chunk a hundirîn ya ji bo pelên dirêj tê bikaranîn kontrol dike. Nirxên mezintir sînoran kêm dikin û context zêdetir diparêzin, lê her inference girantir dikin û dibe ku memory GPU zêdetir bikar bîne. Nirxên biçûktir her inference siviktir dikin lê sînorên zêdetir diafirînin, ku dikare li derdora wan xalan nasînê bandor bike. Di piraniya rewşan de nirxa standard tê pêşniyarkirin.

## UI ya herêmîkirî

Modela ASR bixwe **tenê ji bo Japonî** ye. Herêmîkirina README û UI ya Colab **hemû 183 zimanên çalak ên ISO 639 Set 1** digire (`sh` ya kevn nayê hesibandin).

Îngilîzî (`en`) çavkaniya canonical ya wergerê ye. Japonî (`ja`) wergera nirxandî ye û wek pêşandana standard a `README.md` li root a repository tê kopîkirin. README ya Japonî ya root **wek çavkaniya wergerê nayê bikaranîn**. 181 locale yên din ji Îngilîzî bi makîneyê têne wergerandin.

## Nîşe

- Defter berî transkripsiyonê raweste heke GPU tune be.
- Dema pêvajokirinê li gorî dirêjahiya input, mîheng û GPU ya Colab dide diguhere. Run a yekem NeMo û modela nêzî 1.23 GB jî dadixe.
- Dengê dirêj di chunks ên hundirîn de tê pêvajokirin, ji ber vê yekê nasîn dikare li derdora sînorên chunk bandor bibe.

## Çavkaniya canonical û generation

Çavkaniyên canonical ên wergerbar:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` snapshot a canonical a senkronkirî ye. Japonî wek wergera nirxandî di `locales/ja.json` de tê parastin, û snapshot a README ya wê li root `README.md` tê kopîkirin.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Parastina wergerê ji CI ya asayî cuda ye. Bikarhênerên asayî û CI pêdivî bi credentials ên wergerê nakin.

## Lîsans

Scaffolding a notebook û scriptên build/check bi lîsansa MIT ne. Modela Third Intelligence li vir nû ve nayê belavkirin û di bin **Apache-2.0** de ye. Dependencies ên aliyê sêyem lîsansên xwe diparêzin.
