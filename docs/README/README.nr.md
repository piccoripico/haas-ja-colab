# Haas Japanese Colab

I-Google Colab notebook yokutlola phasi umsindo namavidiyo wesiJapani kusetshenziswa i-Third Intelligence **Haas-ja-v1.0**.

[![Vula ku-Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_nr.ipynb)

## Izinto ezikghonakalako

- **Simahla:** Isebenza ku-GPU runtime yasimahla ye-Google Colab.
- **I-ASR yesiJapani:** Isebenzisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), imodeli enamapharamitha angaba ngu-0.6B yokubona ikulumo yesiJapani.
- **Irhaba:** Ukutlola phasi kungenziwa msinyana.
- **Iimpawu zokutlola:** Imodeli ikhupha iimpawu zokutlola zesiJapani eziqikelelwako.
- **Ama-timestamp nama-subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ukusebenza ngamafayili amade:** Amafayili womsindo namavidiyo amade nawo angacutshungulwa.
- **Ukusekela i-Google Drive:** Layisha amafayili bunqopha namkha uwafunde ku-Google Drive; i-ZIP yomphumela ingagcinwa ku-Drive nawufuna.
- **Imiphumela eminengi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kanye ZIP.

## Indlela yokusebenzisa

1. Khetha `INPUT_MODE` ku **1. Settings** begodu utjhugulule ezinye settings nakufaneleko.
2. Khetha **Runtime → Run all**.
3. Nange `INPUT_MODE = "upload"`, khetha amafayili ku **2. File selection / Google Drive mount**.
4. I-ZIP yomphumela iyadawunlodeka ngokuzenzakalela ngemva kokucutshungulwa.

## Ama-mode we-timestamp

- `none`: akunalo ilwazi lesikhathi.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Amafayili amade

`CHUNK_SECONDS` ilawula ubude be-internal chunk esetjenziswa kumafayili amade. Amanani amakhulu anciphisa imikhawulo begodu agcina context enengi, kodwana i-inference ngayinye iba nzima begodu ingasebenzisa i-GPU memory enengi. Amanani amancani enza i-inference ibe lula kodwana akha imikhawulo eminengi, okungathinta i-recognition eduze kwalawo maphuzu. I-default iyaphakanyiswa ebujameni obunengi.

## I-UI etjhugululiweko

Imodeli ye-ASR uqobo **ngeyesiJapani kwaphela**. I-localization ye-README ne-Colab UI ihlanganisa zoke **iilimi ezi-183 ze-ISO 639 Set 1 ezisebenzako** (`sh` endala ayifakwanga).

IsiNgisi (`en`) ngiso canonical translation source. IsiJapani (`ja`) yi-translation ehloliweko begodu ikopishwa ku-root ye-repository njenge-default `README.md`. I-root Japanese README **ayisetjenziswa** njenge-translation source. Amanye ama-locale ama-181 atjhugululwa ngumtjhini asuselwa esiNgisini.

## Okutjhejwako

- I-notebook iyajama ngaphambi kwe-transcription nange i-GPU ingekho.
- Isikhathi sokucutshungulwa sincike ebudeni be-input, settings, kanye ne-GPU eyabelwe yi-Colab. Ku-run yokuthoma, i-NeMo nemodeli engaba ngu-1.23 GB nazo ziyadawunlodeka.
- Umsindo omude ucutshungulwa ngama-internal chunks, ngalokho i-recognition ingathinteka eduze kwe-chunk boundaries.

## Canonical source nokwakha

Ama-canonical source atjhugululekako:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yi-synchronized canonical snapshot. IsiJapani sigcinwa njenge-reviewed translation ku `locales/ja.json`, begodu i-README snapshot yaso ikopishwa ku-root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Ukugcinwa kwama-translation kuhlukene ne-ordinary CI. Abasebenzisi abajayelekileko ne-CI abadingi ama-translation credentials.

## License

I-notebook scaffolding nama-build/check scripts ane-MIT license. Imodeli ye-Third Intelligence ayisabalaliswa lapha begodu ilawulwa yi **Apache-2.0**. Ama-third-party dependencies agcina ama-license wawo.
