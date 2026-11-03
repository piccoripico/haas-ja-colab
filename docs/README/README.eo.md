# Haas Japanese Colab

Google Colab-kajero por transskribi japanan aŭdion kaj videon per Third Intelligence **Haas-ja-v1.0**.

[![Malfermi en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_eo.ipynb)

## Trajtoj

- **Senpaga:** Funkcias en la senpaga GPU-rultempo de Google Colab.
- **Japana ASR:** Uzas [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modelon kun proksimume 0,6B parametroj por japana parolrekono.
- **Rapida:** La transskribo povas esti prilaborata rapide.
- **Interpunkcio:** La modelo eligas taksitan japanan interpunkcion.
- **Tempostampoj kaj subtitoloj:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Prilaboro de longaj dosieroj:** Ankaŭ longaj aŭdio- kaj videodosieroj povas esti prilaborataj.
- **Subteno por Google Drive:** Alŝutu dosierojn rekte aŭ legu ilin el Google Drive; la eliga ZIP laŭvole povas esti konservita en Drive.
- **Pluraj eligoj:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest kaj ZIP.

## Uzado

1. Elektu `INPUT_MODE` en **1. Settings** kaj laŭbezone ĝustigu la aliajn agordojn.
2. Elektu **Runtime → Run all**.
3. Kun `INPUT_MODE = "upload"`, elektu dosierojn en **2. File selection / muntado de Google Drive**.
4. La eliga ZIP estas aŭtomate elŝutata post la prilaboro.

## Tempostampaj reĝimoj

- `none`: neniu tempa informo.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Malĉifrilo

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Longaj dosieroj

`CHUNK_SECONDS` regas la internan fragmentodaŭron uzatan por longaj dosieroj. Pli grandaj valoroj reduktas limojn kaj konservas pli da kunteksto, sed igas ĉiun inferencon pli peza kaj povas pliigi uzon de GPU-memoro. Pli malgrandaj valoroj igas ĉiun inferencon pli malpeza sed kreas pli da limoj, kio povas influi rekonon ĉirkaŭ tiuj punktoj. La defaŭlta valoro estas rekomendata plejofte.

## Lokalizita interfaco

La modelo ASR mem estas **nur por la japana**. Lokalizado de README kaj de la Colab-interfaco kovras ĉiujn **183 aktivajn lingvojn de ISO 639 Set 1** (la eksmoda `sh` estas ekskludita).

La angla (`en`) estas la kanona tradukfonto. La japana (`ja`) estas reviziita traduko kaj estas kopiita al la radiko de la deponejo kiel la defaŭlta prezento de `README.md`. La radika japana README **ne** estas uzata kiel tradukfonto. La aliaj 181 lokaĵaroj estas maŝine tradukitaj el la angla.

## Notoj

- La kajero haltas antaŭ transskribo se GPU ne disponeblas.
- La prilabora tempo dependas de la eniga longo, agordoj kaj la GPU asignita de Colab. La unua rulo ankaŭ elŝutas NeMo kaj la modelon de proksimume 1.23 GB.
- Longa aŭdio estas prilaborata en internaj fragmentoj, do rekono povas esti influita ĉirkaŭ fragmentlimoj.

## Kanona fonto kaj generado

Kanonaj tradukeblaj fontoj:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` estas la sinkronigita kanona momentfoto. La japana estas prizorgata kiel reviziita traduko en `locales/ja.json`, kaj ĝia README-momentfoto estas kopiita al la radika `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Tradukprizorgado estas aparta de ordinara CI. Ordinaraj uzantoj kaj CI ne bezonas tradukajn akreditaĵojn.

## Permesilo

La kajera strukturo kaj la skriptoj por konstruo/kontrolo estas licencitaj laŭ MIT. La modelo Third Intelligence ne estas redistribuata ĉi tie kaj estas regata de **Apache-2.0**. Triaj dependecoj konservas siajn proprajn permesilojn.
