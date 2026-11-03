# Haas Japanese Colab

Google Colabi märkmik jaapanikeelse heli ja video transkribeerimiseks Third Intelligence **Haas-ja-v1.0** abil.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_et.ipynb)

## Funktsioonid

- **Tasuta:** Töötab Google Colabi tasuta GPU-keskkonnas.
- **Jaapani ASR:** Kasutab mudelit [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), ligikaudu 0.6B parameetriga mudelit jaapani kõnetuvastuseks.
- **Kiire:** Transkriptsiooni saab kiiresti töödelda.
- **Kirjavahemärgid:** Mudel väljastab hinnangulised jaapani kirjavahemärgid.
- **Ajatemplid ja subtiitrid:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pikkade failide töötlemine:** Töödelda saab ka pikki heli- ja videofaile.
- **Google Drive'i tugi:** Laadi failid otse üles või loe neid Google Drive'ist; väljundi ZIP-i saab soovi korral Drive'i salvestada.
- **Mitu väljundvormingut:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ja ZIP.

## Kasutamine

1. Vali `INPUT_MODE` jaotises **1. Settings** ja vajadusel kohanda muid seadeid.
2. Vali **Runtime → Run all**.
3. Kui `INPUT_MODE = "upload"`, vali failid jaotises **2. File selection / Google Drive mount**.
4. Väljundi ZIP laaditakse pärast töötlemise lõppu automaatselt alla.

## Ajatemplirežiimid

- `none`: ajateavet ei lisata.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekooder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Pikad failid

`CHUNK_SECONDS` määrab pikkade failide sisemise tüki kestuse. Suuremad väärtused vähendavad piiride arvu ja säilitavad rohkem konteksti, kuid muudavad iga inferentsi raskemaks ning võivad suurendada GPU-mälu kasutust. Väiksemad väärtused muudavad iga inferentsi kergemaks, kuid loovad rohkem piire, mis võivad nende kohtade ümber tuvastust mõjutada. Enamasti soovitatakse vaikeväärtust.

## Lokaliseeritud kasutajaliides

ASR-mudel ise on **ainult jaapani keele jaoks**. README ja Colabi kasutajaliidese lokaliseerimine hõlmab kõiki **183 aktiivset ISO 639 Set 1 keelt** (aegunud `sh` on välja jäetud).

Inglise keel (`en`) on kanooniline tõlkeallikas. Jaapani keel (`ja`) on üle vaadatud tõlge ja kopeeritakse hoidla juurkausta vaikimisi `README.md` esitusena. Juurkausta jaapanikeelset README-d **ei** kasutata tõlkeallikana. Ülejäänud 181 locale'i tõlgitakse masinaga inglise keelest.

## Märkused

- Märkmik peatub enne transkriptsiooni, kui GPU pole saadaval.
- Töötlemisaeg sõltub sisendi pikkusest, seadetest ja Colabi määratud GPU-st. Esimesel käivitamisel laaditakse alla ka NeMo ja ligikaudu 1.23 GB mudel.
- Pikka heli töödeldakse sisemiste tükkidena, mistõttu tuvastus võib tükkide piiride lähedal halveneda.

## Kanooniline allikas ja genereerimine

Kanoonilised tõlgitavad allikad:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` on sünkroonitud kanooniline snapshot. Jaapani keelt hooldatakse üle vaadatud tõlkena failis `locales/ja.json` ja selle README snapshot kopeeritakse juurkausta nimega `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Tõlgete hooldus on tavalisest CI-st eraldatud. Tavakasutajad ja CI ei vaja tõlkevolitusi.

## Litsents

Märkmiku struktuur ning build-/kontrollskriptid on MIT-litsentsiga. Third Intelligence mudelit siin edasi ei levitata ja sellele kehtib **Apache-2.0**. Kolmandate osapoolte sõltuvused säilitavad oma litsentsid.
