# Haas Japanese Colab

Google Colab piezīmju grāmata japāņu audio un video transkribēšanai ar Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_lv.ipynb)

## Iespējas

- **Bezmaksas:** Darbojas Google Colab bezmaksas GPU izpildvidē.
- **Japāņu ASR:** Izmanto [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), aptuveni 0.6B parametru modeli japāņu runas atpazīšanai.
- **Ātrs:** Transkripciju var apstrādāt ātri.
- **Pieturzīmes:** Modelis izvada prognozētas japāņu pieturzīmes.
- **Laika zīmogi un subtitri:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Garu failu apstrāde:** Var apstrādāt arī garus audio un video failus.
- **Google Drive atbalsts:** Augšupielādējiet failus tieši vai lasiet tos no Google Drive; izvades ZIP pēc izvēles var saglabāt Drive.
- **Vairāki izvades formāti:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifests un ZIP.

## Lietošana

1. Izvēlieties `INPUT_MODE` sadaļā **1. Settings** un vajadzības gadījumā pielāgojiet citus iestatījumus.
2. Izvēlieties **Runtime → Run all**.
3. Ja `INPUT_MODE = "upload"`, izvēlieties failus sadaļā **2. File selection / Google Drive mount**.
4. Izvades ZIP tiek automātiski lejupielādēts pēc apstrādes pabeigšanas.

## Laika zīmogu režīmi

- `none`: nav laika informācijas.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoders

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Gari faili

`CHUNK_SECONDS` nosaka iekšējā fragmenta ilgumu gariem failiem. Lielākas vērtības samazina robežu skaitu un saglabā vairāk konteksta, bet padara katru inferenci smagāku un var palielināt GPU atmiņas izmantošanu. Mazākas vērtības padara inferenci vieglāku, taču rada vairāk robežu, kas var ietekmēt atpazīšanu šo punktu tuvumā. Vairumā gadījumu ieteicama noklusējuma vērtība.

## Lokalizēts interfeiss

Pats ASR modelis ir **tikai japāņu valodai**. README un Colab interfeisa lokalizācija aptver visas **183 aktīvās ISO 639 Set 1 valodas** (novecojušais `sh` ir izslēgts).

Angļu valoda (`en`) ir kanoniskais tulkošanas avots. Japāņu valoda (`ja`) ir pārskatīts tulkojums, kas tiek kopēts repozitorija saknē kā noklusējuma `README.md` attēlojums. Saknes japāņu README **netiek** izmantots kā tulkošanas avots. Pārējās 181 locales tiek mašīntulkotas no angļu valodas.

## Piezīmes

- Piezīmju grāmata apstājas pirms transkripcijas, ja GPU nav pieejams.
- Apstrādes laiks ir atkarīgs no ievades garuma, iestatījumiem un Colab piešķirtā GPU. Pirmajā palaišanas reizē tiek lejupielādēts arī NeMo un aptuveni 1.23 GB modelis.
- Garš audio tiek apstrādāts iekšējos fragmentos, tāpēc atpazīšana var pasliktināties fragmentu robežu tuvumā.

## Kanoniskais avots un ģenerēšana

Kanoniskie tulkojamie avoti:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ir sinhronizētais kanoniskais snapshot. Japāņu valoda tiek uzturēta kā pārskatīts tulkojums failā `locales/ja.json`, un tās README snapshot tiek kopēts uz sakni kā `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Tulkojumu uzturēšana ir atdalīta no parastās CI. Parastajiem lietotājiem un CI nav vajadzīgi tulkošanas akreditācijas dati.

## Licence

Piezīmju grāmatas struktūra un build/pārbaudes skripti ir licencēti ar MIT licenci. Third Intelligence modelis šeit netiek tālāk izplatīts, un uz to attiecas **Apache-2.0**. Trešo pušu atkarības saglabā savas licences.
