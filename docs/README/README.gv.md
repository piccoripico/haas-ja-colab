# Haas Japanese Colab

Lioar-noteyn Google Colab son çhyndaays sheean as feeshan Shapaanagh lesh Third Intelligence **Haas-ja-v1.0**.

[![Foshil ayns Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_gv.ipynb)

## Reihyn

- **Nastee:** T’eh roie er runtime GPU nastee Google Colab.
- **ASR Shapaanagh:** T’eh jannoo ymmyd jeh [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modail mysh 0.6B parameteryn son enney er glare Shapaanagh.
- **Çhappee:** Foddee yn çhyndaays ve jeant dy çhappee.
- **Poyntal:** Ta’n modail cur magh poyntal Shapaanagh er ny hoilshaghey.
- **Stampyn traa as fo-heidyn:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Gobbraghey coadanyn liauyr:** Foddee coadanyn sheean as feeshan liauyr ve gobbrit er neesht.
- **Cooney Google Drive:** Cur coadanyn seose dy jeeragh ny lhaih ad ass Google Drive; foddee yn ZIP magh ve sauailt dys Drive my vees eh er ny reih.
- **Ram maghyn:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest as ZIP.

## Ymmyd

1. Reih `INPUT_MODE` ayns **1. Settings** as caghlaa ny reihyn elley my vees feme.
2. Reih **Runtime → Run all**.
3. Lesh `INPUT_MODE = "upload"`, reih coadanyn ayns **2. File selection / mount Google Drive**.
4. Ta’n ZIP magh er ny lhieggal neose dy hene lurg y ghobbraghey.

## Modyn stamp traa

- `none`: gyn fys traa.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Jeeyder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Coadanyn liauyr

Ta `CHUNK_SECONDS` reirey fad y chunk s’thie ta goll er ymmyd son coadanyn liauyr. Ta towseyn smoo goll er y choontey jeh joaraghyn as freayll ny smoo co-hecks, agh t’ad jannoo dagh inference ny s’trome as foddee ad ymmyd ny smoo jeh cooinaghtyn GPU. Ta towseyn sloo jannoo dagh inference ny s’aashagh agh croo ny smoo joaraghyn, as foddee shen bentyn rish enney mygeayrt ny buill shen. Ta’n towse bunneydagh er ny chur er raad ayns y chooid smoo jeh cooishyn.

## Eddin ynydagh

Ta’n modail ASR hene **son Shapaanish ny-lomarcan**. Ta ynydaghey README as UI Colab coodaghey dagh **183 çhengey bio ISO 639 Set 1** (`sh` shenn er ny lhiggey magh).

She Baarle (`en`) yn bun-vooinjer çhyndaays canonical. Ta Shapaanish (`ja`) ny çhyndaays er ny chaglym as t’eh er ny choip dys bun y repository myr yn taisbeanagh `README.md` bunneydagh. Cha nel yn README Shapaanagh ec y vun **goll er ymmyd myr bun çhyndaays**. Ta ny 181 locale elley er nyn çhyndaays lesh masteyryn ass Baarle.

## Noteyn

- Ta’n lioar-noteyn scuirr roish çhyndaays mannagh vel GPU ry gheddyn.
- Ta traa gobbraghey croghey er fad y chooid stiagh, ny reihyn as yn GPU ta Colab cur da. Ec y chied roie t’eh neesht lhieggal neose NeMo as yn modail mysh 1.23 GB.
- Ta sheean liauyr er ny gobbraghey ayns chunks s’thie, myr shen foddee enney ve er ny bentyn mygeayrt joaraghyn y chunk.

## Bun canonical as croo

Bunyn canonical ry çhyndaa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

She `locales/en.json` yn snapshot canonical co-chordit. Ta Shapaanish er ny freayll myr çhyndaays er ny chaglym ayns `locales/ja.json`, as ta’n snapshot README echey er ny choip dys `README.md` ec y vun.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Ta freayll çhyndaays er leth voish CI cadjin. Cha nel feme ec ymmydeyryn cadjin ny CI er credentials çhyndaays.

## Kied

Ta strughtoor y lioar-noteyn as scripts build/check fo kied MIT. Cha nel yn modail Third Intelligence er ny rheynn noa ayns shoh as t’eh fo **Apache-2.0**. Ta dependencyn jeh deiney elley freayll nyn giedyn hene.
