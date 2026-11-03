# Haas Japanese Colab

Google Colab koadernoa, japoniar audioa eta bideoa Third Intelligence **Haas-ja-v1.0** erabiliz transkribatzeko.

[![Ireki Colab-en](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_eu.ipynb)

## Ezaugarriak

- **Doakoa:** Google Colab-en doako GPU runtime-an exekutatzen da.
- **Japoniar ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) erabiltzen du, japoniar hizketaren ezagutzarako gutxi gorabehera 0,6B parametrodun eredua.
- **Azkarra:** Transkripzioa azkar prozesatu daiteke.
- **Puntuazioa:** Ereduak estimatutako japoniar puntuazioa ateratzen du.
- **Denbora-markak eta azpitituluak:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Fitxategi luzeen prozesamendua:** Audio eta bideo fitxategi luzeak ere prozesatu daitezke.
- **Google Drive euskarria:** Igo fitxategiak zuzenean edo irakurri Google Drive-tik; irteerako ZIP aukeran Drive-n gorde daiteke.
- **Irteera anitz:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest eta ZIP.

## Erabilera

1. Aukeratu `INPUT_MODE` **1. Settings** atalean eta doitu beste ezarpenak behar izanez gero.
2. Aukeratu **Runtime → Run all**.
3. `INPUT_MODE = "upload"` erabiltzean, aukeratu fitxategiak **2. File selection / Google Drive mount** atalean.
4. Irteerako ZIP automatikoki deskargatzen da prozesamenduaren ondoren.

## Denbora-marken moduak

- `none`: ez dago denbora-informaziorik.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Deskodetzailea

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fitxategi luzeak

`CHUNK_SECONDS`-ek fitxategi luzeetarako erabiltzen den barneko chunk-aren iraupena kontrolatzen du. Balio handiagoek mugak murriztu eta testuinguru gehiago mantentzen dute, baina inferentzia bakoitza astunagoa da eta GPU memoria gehiago erabil dezake. Balio txikiagoek inferentzia bakoitza arintzen dute baina muga gehiago sortzen dituzte, eta horrek puntu horien inguruko ezagutzan eragina izan dezake. Kasu gehienetan lehenetsitako balioa gomendatzen da.

## Lokalizatutako interfazea

ASR eredua bera **japonierarako bakarrik** da. README eta Colab UI-aren lokalizazioak **ISO 639 Set 1eko 183 hizkuntza aktiboak** estaltzen ditu (zaharkitutako `sh` kenduta).

Ingelesa (`en`) da itzulpen-iturri kanonikoa. Japoniera (`ja`) berrikusitako itzulpena da eta biltegiaren erroan kopiatzen da `README.md` aurkezpen lehenetsi gisa. Erroko japoniar README **ez** da itzulpen-iturri gisa erabiltzen. Beste 181 locale-ak ingelesetik makinez itzultzen dira.

## Oharrak

- Koadernoa transkripzioaren aurretik gelditzen da GPU erabilgarri ez badago.
- Prozesamendu-denbora sarreraren luzeraren, ezarpenen eta Colab-ek esleitutako GPU-aren araberakoa da. Lehen exekuzioak NeMo eta gutxi gorabehera 1.23 GB-ko eredua ere deskargatzen ditu.
- Audio luzea barneko chunk-etan prozesatzen da; beraz, ezagutzak eragina izan dezake chunk-mugen inguruan.

## Iturri kanonikoa eta sorrera

Itzul daitezkeen iturri kanonikoak:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` sinkronizatutako snapshot kanonikoa da. Japoniera berrikusitako itzulpen gisa mantentzen da `locales/ja.json`-en, eta haren README snapshot-a erroko `README.md`-era kopiatzen da.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Itzulpenen mantentzea CI arruntetik bereizita dago. Ohiko erabiltzaileek eta CI-k ez dute itzulpen-kredentzialik behar.

## Lizentzia

Koadernoaren egitura eta build/check scriptak MIT lizentziapean daude. Third Intelligence eredua ez da hemen birbanatzen eta **Apache-2.0**-ren mende dago. Hirugarrenen mendekotasunek beren lizentziak mantentzen dituzte.
