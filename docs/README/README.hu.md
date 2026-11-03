# Haas Japanese Colab

Google Colab-jegyzetfüzet a fișierelor audio și video în japoneză cu Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_hu.ipynb)

## Funkciók

- **Ingyenes:** Rulează în mediul GPU gratuit Google Colab.
- **ASR japonez:** Folosește [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un model cu aproximativ 0.6B parametri pentru recunoașterea vorbirii japoneze.
- **Gyors:** Transcrierea poate fi procesată rapid.
- **Írásjelek:** Modelul produce punctuație japoneză estimată.
- **Időbélyegek és feliratok:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Hosszú fájlok feldolgozása:** Pot fi procesate și fișiere audio și video lungi.
- **Google Drive-támogatás:** Încărcați fișiere direct sau citiți-le din Google Drive; ZIP-ul de ieșire poate fi salvat opțional în Drive.
- **Több kimenet:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest și ZIP.

## Használat

1. Alegeți `INPUT_MODE` în **1. Settings** și ajustați alte setări dacă este necesar.
2. Selectați **Runtime → Run all**.
3. Cu `INPUT_MODE = "upload"`, alegeți fișierele în **2. File selection / Google Drive mount**.
4. ZIP-ul de ieșire este descărcat automat după finalizarea procesării.

## Időbélyeg-módok

- `none`: fără informații temporale.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekóder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Hosszú fájlok

`CHUNK_SECONDS` controlează durata internă a fragmentelor pentru fișiere lungi. Valorile mai mari reduc limitele și păstrează mai mult context, dar fac fiecare inferență mai grea și pot crește utilizarea memoriei GPU. Valorile mai mici ușurează fiecare inferență, dar creează mai multe limite, ceea ce poate afecta recunoașterea în jurul acelor puncte. Valoarea implicită este recomandată în majoritatea cazurilor.

## Lokalizált felület

Modelul ASR în sine este **doar pentru japoneză**. Localizarea README și a interfeței Colab acoperă toate cele **183 de limbi active ISO 639 Set 1** (`sh` învechit este exclus).

Engleza (`en`) este sursa canonică de traducere. Japoneza (`ja`) este o traducere revizuită și este copiată în rădăcina repository-ului ca prezentare implicită `README.md`. README-ul japonez din rădăcină **nu** este folosit ca sursă de traducere. Celelalte 181 de locale sunt traduse automat din engleză.

## Megjegyzések

- Megjegyzésekbook-ul se oprește înainte de transcriere dacă nu este disponibil un GPU.
- Timpul de procesare depinde de lungimea intrării, setări și GPU-ul alocat de Colab. Prima rulare descarcă și NeMo și modelul de aproximativ 1.23 GB.
- Audio lung este procesat în fragmente interne, astfel încât recunoașterea poate fi afectată în jurul limitelor fragmentelor.

## Kanonikus forrás és generálás

Surse canonice traductibile:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` este snapshot-ul canonic sincronizat. Japoneza este menținută ca traducere revizuită în `locales/ja.json`, iar snapshot-ul README este copiat în rădăcină ca `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Întreținerea traducerilor este separată de CI obișnuit. Utilizatorii obișnuiți și CI nu au nevoie de acreditări de traducere.

## Licenc

Structura notebook-ului și scripturile de build/verificare sunt licențiate MIT. Modelul Third Intelligence nu este redistribuit aici și este guvernat de **Apache-2.0**. Dependențele terțe își păstrează propriile licențe.
