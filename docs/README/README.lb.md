# Haas Japanese Colab

Google Colab-Notebook fir japanesch Audio a Video mat Third Intelligence **Haas-ja-v1.0** ze transkribéieren.

[![An Colab opmaachen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_lb.ipynb)

## Funktiounen

- **Gratis:** Leeft op der gratiser GPU-Runtime vu Google Colab.
- **Japanesch ASR:** Benotzt [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), e Modell mat ongeféier 0,6B Parameteren fir japanesch Sproocherkennung.
- **Séier:** D’Transkriptioun kann séier veraarbecht ginn.
- **Interpunktioun:** De Modell gëtt geschaten japanesch Interpunktioun aus.
- **Zäitstempelen an Ënnertitelen:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Veraarbechtung vu laange Fichieren:** Laang Audio- a Videofichiere kënnen och veraarbecht ginn.
- **Google Drive-Ënnerstëtzung:** Luet Fichieren direkt erop oder liest se aus Google Drive; den Ausgabe-ZIP kann optional op Drive gespäichert ginn.
- **Méi Ausgaben:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest an ZIP.

## Benotzung

1. Wielt `INPUT_MODE` ënner **1. Settings** a passt aner Astellungen un, wann néideg.
2. Wielt **Runtime → Run all**.
3. Mat `INPUT_MODE = "upload"` wielt Fichieren ënner **2. File selection / Google Drive mount**.
4. Den Ausgabe-ZIP gëtt nom Veraarbechten automatesch erofgelueden.

## Zäitstempel-Modi

- `none`: keng Zäitinformatioun.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Laang Fichieren

`CHUNK_SECONDS` kontrolléiert d’intern Chunk-Dauer fir laang Fichieren. Méi grouss Wäerter reduzéieren d’Grenzen a behalen méi Kontext, maachen awer all inference méi schwéier a kënne méi GPU-Speicher benotzen. Méi kleng Wäerter maachen all inference méi liicht, erstellen awer méi Grenzen, wat d’Erkennung ronderëm dës Punkte beaflosse kann. De Standardwäert gëtt an de meeschte Fäll recommandéiert.

## Lokaliséiert UI

De ASR-Modell selwer ass **nëmme fir Japanesch**. D’Lokaliséierung vu README an der Colab-UI deckt **all 183 aktiv Sprooche vu ISO 639 Set 1** of (`sh` ass als veraltet ausgeschloss).

Englesch (`en`) ass déi kanonesch Iwwersetzungsquell. Japanesch (`ja`) ass eng iwwerpréift Iwwersetzung a gëtt an d’Wuerzel vum Repository kopéiert als Standard-`README.md`-Darstellung. Den japaneschen README an der Wuerzel gëtt **net** als Iwwersetzungsquell benotzt. Déi aner 181 Locale ginn maschinell aus dem Engleschen iwwersat.

## Notizen

- Den Notebook stoppt virun der Transkriptioun, wann kee GPU verfügbar ass.
- D’Veraarbechtungszäit hänkt vun der Input-Längt, den Astellungen an dem GPU of, deen Colab zouweist. Beim éischte Run ginn och NeMo an de Modell vun ongeféier 1.23 GB erofgelueden.
- Laangen Audio gëtt an internen Chunks veraarbecht, dofir kann d’Erkennung ronderëm Chunk-Grenze beaflosst ginn.

## Kanonesch Quell a Generatioun

Kanonesch iwwersetzbar Quellen:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ass de synchroniséierte kanonesche Snapshot. Japanesch gëtt als iwwerpréift Iwwersetzung an `locales/ja.json` ënnerhalen, an säin README-Snapshot gëtt an de Root-`README.md` kopéiert.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

D’Iwwersetzungsënnerhalt ass getrennt vum normale CI. Normal Benotzer a CI brauche keng Iwwersetzungs-Credentials.

## Lizenz

D’Notebook-Grondstruktur an d’Build/Check-Skripter stinn ënner der MIT-Lizenz. De Third Intelligence-Modell gëtt hei net nei verdeelt a steet ënner **Apache-2.0**. Drëtt-Partei-Ofhängegkeete behalen hir eege Lizenzen.
