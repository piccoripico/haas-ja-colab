# Haas Japanese Colab

Google Colab notebook loogu talagalay in lagu qoraal-rogo cod iyo muuqaal Jabaaniis ah iyadoo la adeegsanayo Third Intelligence **Haas-ja-v1.0**.

[![Ku fur Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_so.ipynb)

## Astaamaha

- **Bilaash:** Waxay ku shaqaysaa GPU runtime-ka bilaashka ah ee Google Colab.
- **Japanese ASR:** Waxay isticmaashaa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model qiyaastii 0.6B parameter ah oo loogu talagalay aqoonsiga hadalka Jabaaniiska.
- **Degdeg:** Transcription-ka si dhakhso ah ayaa loo farsamayn karaa.
- **Calaamadaha qoraalka:** Model-ku wuxuu soo saaraa punctuation Jabaaniis ah oo la qiyaasay.
- **Timestamps iyo subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Farsamaynta faylasha dhaadheer:** Faylasha codka iyo muuqaalka ee dhaadheer sidoo kale waa la farsamayn karaa.
- **Taageerada Google Drive:** Si toos ah u upload-garee faylasha ama ka akhri Google Drive; output ZIP-ka si ikhtiyaari ah ayaa loogu kaydin karaa Drive.
- **Outputs badan:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, iyo ZIP.

## Isticmaalka

1. Ka dooro `INPUT_MODE` gudaha **1. Settings** oo hagaaji settings kale haddii loo baahdo.
2. Dooro **Runtime → Run all**.
3. Marka `INPUT_MODE = "upload"`, ka dooro faylasha **2. File selection / Google Drive mount**.
4. Output ZIP-ka si otomaatig ah ayaa loo download-gareeyaa marka processing-ku dhammaado.

## Hababka timestamp

- `none`: ma jiro timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Faylasha dhaadheer

`CHUNK_SECONDS` wuxuu xakameeyaa internal chunk duration-ka loo adeegsado faylasha dhaadheer. Values waaweyn waxay yareeyaan boundaries oo waxay ilaaliyaan context badan, laakiin inference kasta way culays badan tahay waxayna kordhin kartaa isticmaalka GPU memory. Values yaryar waxay fududeeyaan inference kasta laakiin waxay abuuraan boundaries badan, taas oo saameyn karta recognition-ka meelahaas ku dhow. Default-ka ayaa lagu talinayaa inta badan.

## UI la maxalliyey

ASR model-ku laftiisu waa **Jabaaniis-keliya**. Maxalliyeynta README iyo Colab UI waxay daboolaysaa dhammaan **183 active ISO 639 Set 1 languages** (deprecated `sh` waa laga saaray).

English (`en`) waa canonical translation source. Japanese (`ja`) waa reviewed translation waxaana lagu koobiyeeyaa repository root sida default `README.md` presentation. Root Japanese README **looma isticmaalo** translation source. 181-ka locale ee kale waxaa machine-translated laga sameeyaa English.

## Xusuusin

- Notebook-ku wuu istaagayaa ka hor transcription haddii GPU aan la heli karin.
- Processing time-ku wuxuu ku xiran yahay dhererka input-ka, settings, iyo GPU-ga Colab qoondeeyo. Run-ka ugu horreeya sidoo kale wuxuu download-gareeyaa NeMo iyo model-ka qiyaastii 1.23 GB ah.
- Long audio waxaa lagu farsameeyaa internal chunks, sidaas darteed recognition-ka wuxuu saameyn yeelan karaa agagaarka chunk boundaries.

## Canonical source iyo generation

Ilaha asalka ah ee la turjumi karo:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` waa synchronized canonical snapshot. Japanese waxaa lagu hayaa reviewed translation gudaha `locales/ja.json`, README snapshot-kiisana waxaa lagu koobiyeeyaa root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance waa ka gooni ordinary CI. Ordinary users iyo CI uma baahna translation credentials.

## Shatiga

Notebook scaffolding iyo build/check scripts waa MIT licensed. Third Intelligence model-ka halkan dib looguma qaybiyo waxaana xukuma **Apache-2.0**. Third-party dependencies waxay haystaan shatiyadooda.
