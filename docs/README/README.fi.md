# Haas Japanese Colab

Google Colab -muistikirja japaninkielisen äänen ja videon litterointiin Third Intelligence **Haas-ja-v1.0** -mallilla.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_fi.ipynb)

## Ominaisuudet

- **Ilmainen:** Toimii Google Colabin ilmaisessa GPU-ajoympäristössä.
- **Japanin ASR:** Käyttää [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) -mallia, jossa on noin 0.6B parametria japaninkieliseen puheentunnistukseen.
- **Nopea:** Litterointi voidaan käsitellä nopeasti.
- **Välimerkit:** Malli tuottaa arvioituja japanin välimerkkejä.
- **Aikaleimat ja tekstitykset:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Pitkien tiedostojen käsittely:** Myös pitkiä ääni- ja videotiedostoja voidaan käsitellä.
- **Google Drive -tuki:** Lataa tiedostoja suoraan tai lue niitä Google Drivesta; tulos-ZIP voidaan haluttaessa tallentaa Driveen.
- **Useita tulostusmuotoja:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifesti ja ZIP.

## Käyttö

1. Valitse `INPUT_MODE` kohdassa **1. Settings** ja säädä muita asetuksia tarvittaessa.
2. Valitse **Runtime → Run all**.
3. Kun `INPUT_MODE = "upload"`, valitse tiedostot kohdassa **2. File selection / Google Drive mount**.
4. Tulos-ZIP ladataan automaattisesti käsittelyn valmistuttua.

## Aikaleimatilat

- `none`: ei aikatietoja.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekooderi

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Pitkät tiedostot

`CHUNK_SECONDS` määrittää pitkille tiedostoille käytettävän sisäisen lohkon keston. Suuremmat arvot vähentävät rajoja ja säilyttävät enemmän kontekstia, mutta tekevät jokaisesta päättelystä raskaamman ja voivat lisätä GPU-muistin käyttöä. Pienemmät arvot keventävät päättelyä, mutta luovat enemmän rajoja, mikä voi vaikuttaa tunnistukseen niiden ympärillä. Oletusarvoa suositellaan useimmissa tapauksissa.

## Lokalisoitu käyttöliittymä

ASR-malli itsessään on **vain japaninkielinen**. README- ja Colab-käyttöliittymän lokalisointi kattaa kaikki **183 aktiivista ISO 639 Set 1 -kieltä** (vanhentunut `sh` on jätetty pois).

Englanti (`en`) on kanoninen käännöslähde. Japani (`ja`) on tarkistettu käännös, joka kopioidaan repositorion juureen oletusnäkymäksi `README.md`. Juurihakemiston japaninkielistä README-tiedostoa **ei** käytetä käännöslähteenä. Muut 181 localea konekäännetään englannista.

## Huomautukset

- Muistikirja pysähtyy ennen litterointia, jos GPU:ta ei ole saatavilla.
- Käsittelyaika riippuu syötteen pituudesta, asetuksista ja Colabin osoittamasta GPU:sta. Ensimmäinen suoritus lataa myös NeMon ja noin 1.23 GB:n mallin.
- Pitkä ääni käsitellään sisäisinä lohkoina, joten tunnistus voi heikentyä lohkojen rajojen ympärillä.

## Kanoninen lähde ja generointi

Kanoniset käännettävät lähteet:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` on synkronoitu kanoninen snapshot. Japania ylläpidetään tarkistettuna käännöksenä tiedostossa `locales/ja.json`, ja sen README-snapshot kopioidaan juureen nimellä `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Käännösten ylläpito on erotettu tavallisesta CI:stä. Tavalliset käyttäjät ja CI eivät tarvitse käännöstunnuksia.

## Lisenssi

Muistikirjan runko ja build-/tarkistusskriptit ovat MIT-lisensoituja. Third Intelligence-mallia ei jaeta tässä uudelleen, ja siihen sovelletaan **Apache-2.0** -lisenssiä. Kolmannen osapuolen riippuvuudet säilyttävät omat lisenssinsä.
