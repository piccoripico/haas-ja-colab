# Haas Japanese Colab

I-Google Colab notebook yokubhala phansi umsindo lamavidiyo esiJapane kusetshenziswa i-Third Intelligence **Haas-ja-v1.0**.

[![Vula ku-Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_nd.ipynb)

## Okukhethekileyo

- **Mahala:** Isebenza ku-GPU runtime yamahala ye-Google Colab.
- **I-ASR yesiJapane:** Isebenzisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), imodeli elama-parameter aphose abe ngu-0.6B yokwazi inkulumo yesiJapane.
- **Iyashesha:** Ukubhala phansi kungacutshungulwa masinyane.
- **Izimpawu zokuloba:** Imodeli ikhipha izimpawu zokuloba zesiJapane ezicatshangelweyo.
- **Ama-timestamp lama-subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ukucubungula amafayela amade:** Amafayela omsindo lamavidiyo amade lawo angacutshungulwa.
- **Ukusekelwa kwe-Google Drive:** Layisha amafayela ngqo kumbe uwafunde ku-Google Drive; i-ZIP yomphumela ingagcinwa ku-Drive nxa uthanda.
- **Imiphumela eminengi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kanye ZIP.

## Indlela yokusebenzisa

1. Khetha `INPUT_MODE` ku **1. Settings** njalo ulungise ezinye settings nxa kudingeka.
2. Khetha **Runtime → Run all**.
3. Nxa `INPUT_MODE = "upload"`, khetha amafayela ku **2. File selection / Google Drive mount**.
4. I-ZIP yomphumela ilandwa ngokuzenzakalela ngemva kokucubungula.

## Ama-mode e-timestamp

- `none`: akulalwazi lwesikhathi.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Amafayela amade

`CHUNK_SECONDS` ilawula ubude be-internal chunk obusetshenziswa kumafayela amade. Amanani amakhulu anciphisa imingcele njalo agcina context enengi, kodwa i-inference ngayinye iba nzima njalo ingasebenzisa i-GPU memory enengi. Amanani amancane enza i-inference ibe lula kodwa adale imingcele eminengi, okungaphazamisa i-recognition eduze kwalezo ndawo. I-default iyelulekwa ezimeni ezinengi.

## I-UI elocalized

Imodeli ye-ASR uqobo **ngeyesiJapane kuphela**. I-localization ye-README le-Colab UI ihlanganisa zonke **izindimi ezingu-183 ze-ISO 639 Set 1 ezisebenzayo** (`sh` endala ayifakwanga).

IsiNgisi (`en`) yiso canonical translation source. IsiJapane (`ja`) yi-translation esihloliweyo njalo sikopishwa ku-root ye-repository njenge-default `README.md`. I-root Japanese README **ayisetshenziswa** njenge-translation source. Amanye ama-locale angu-181 ahunyutshwa ngumtshini esuka esiNgisini.

## Okuqakathekileyo

- I-notebook iyama ngaphambi kwe-transcription nxa i-GPU ingekho.
- Isikhathi sokucubungula sincike ebudeni be-input, settings, kanye le-GPU enikezwe yi-Colab. Ku-run yokuqala kuphinde kulandwe i-NeMo lemodeli ephose ibe ngu-1.23 GB.
- Umsindo omude ucutshungulwa ngama-internal chunks, ngakho i-recognition ingaphazamiseka eduze kwe-chunk boundaries.

## Canonical source lokwakha

Ama-canonical source ahunyutshwayo:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yi-synchronized canonical snapshot. IsiJapane sigcinwa njenge-reviewed translation ku `locales/ja.json`, njalo i-README snapshot yaso ikopishwa ku-root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Ukugcinwa kwama-translation kuhlukene le-ordinary CI. Abasebenzisi abajwayelekileyo le-CI abadingi ama-translation credentials.

## License

I-notebook scaffolding lama-build/check scripts ale-MIT license. Imodeli ye-Third Intelligence ayisabalaliswa lapha njalo ilawulwa yi **Apache-2.0**. Ama-third-party dependencies agcina ama-license awo.
