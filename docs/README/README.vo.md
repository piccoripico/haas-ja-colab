# Haas Japanese Colab

Google Colab-notabuk pro penön taudi e vidios Yapänik me Third Intelligence **Haas-ja-v1.0**.

[![Maifükön in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_vo.ipynb)

## Döbotem

- **Nofeik:** Dunon su GPU-runtime nofeik Google Colab.
- **ASR Yapänik:** Gebon [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modemi labü zänodiko 0.6B paramets pro seivön püki Yapänik.
- **Spidik:** Transkrip padunon spidiko.
- **Pünetam:** Modem gevon pünetami Yapänik cädik.
- **Timamarks e sottituls:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Dunam ragivas lunik:** Ragivs tauda e vidia lunik kanons i padunön.
- **Yuf Google Drive:** Ladet ragivs stedölo u reid olis se Google Drive; ZIP-seit kanon padakipön in Drive if vilol.
- **Seits pluik:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Geb

1. Välol `INPUT_MODE` in **1. Paramets** e votükol paramets votik if zesüdos.
2. Välol **Runtime → Run all**.
3. Ko `INPUT_MODE = "upload"`, välol ragivs in **2. Väl ragiva / mont Google Drive**.
4. ZIP-seit padeladon itjäfidiko pos fin dunama.

## Mods timamarka

- `none`: nüns timik nonik.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Ragivs lunik

`CHUNK_SECONDS` komandön lunoti pätas nidetik pegeböl pro ragivs lunik. Gidots gretikum nepluükons miedis e kipons kontexti pluik, ab al inferen binon vetikum e kanon gebön memori GPU pluik. Gidots smalikum jafons infereni alik leigikum ab miedis pluik, kel kanons dädinön seivami nilü pöins at. Gidot kösömik binon komandabik in sitots mödik.

## Köpetem lokalisöl

ASR-modem it binon **Yapänik te**. Lokalisam README e köpetema Colab kobon valik **183 pükis aktivik ISO 639 Set 1** (`sh` bäldik pelüükon).

Linglänapük (`en`) binon fon traduta kanonik. Yapänapük (`ja`) binon tradut peprüföl e pacopön in stab repozitoria as jon `README.md` kösömik. README Yapänik in stab **no** pagebon as fon traduta. Locales 181 votik patradutons ma machine se Linglänapük.

## Noteds

- Notabuk stopon bü transkrip if GPU no binon gebidik.
- Tim dunama sekidon lunoti nünoda, parametis e GPU pegevöl fa Colab. Dünam balid i deladon NeMo e modemi labü zänodiko 1.23 GB.
- Taud lunik padunon in pätas nidetik, kludo seivam kanon padädinön nilü mieds päta.

## Fon kanonik e jafam

Fons kanonik tradutovik:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` binon snapshot kanonik pisünkronüköl. Yapänapük pakipon as tradut peprüföl in `locales/ja.json`, e snapshot README omik pacopon lü `README.md` in stab.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Kiped traduta binon pateilöl de CI nomik. Gebans nomik e CI no zesüdons kredentialis traduta.

## Däl

Stütam notabuka e skripts build/check labons däli MIT. Modem Third Intelligence no padidulon is e padefön fa **Apache-2.0**. Depens tridi-partik kipons dälis omsik.
