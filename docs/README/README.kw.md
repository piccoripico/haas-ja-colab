# Haas Japanese Colab

Notebook Google Colab rag treuskrifa son ha gwydhyow Japanek gans Third Intelligence **Haas-ja-v1.0**.

[![Ygeri yn Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kw.ipynb)

## Gallosow

- **Rydh:** Redya war runtime GPU rydh Google Colab.
- **ASR Japanek:** Devnydhya [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model a-dro dhe 0.6B parametrow rag aswon lavar Japanek.
- **Syger:** Gallos yw gul an treuskrif yn uskis.
- **Poyntya:** An model a dhispleg poyntya Japanek ragwelys.
- **Amsernodow ha islavarow:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Oberyans restrennow hir:** Gallos yw oberi restrennow son ha gwydhyow hir ynwedh.
- **Skoodhyans Google Drive:** Ughkarga restrennow yn unnfordh po redya anedha dhyworth Google Drive; gallos yw gwitha an ZIP askorrans yn Drive mar mynner.
- **Askorransow liesek:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ha ZIP.

## Devnydh

1. Dewis `INPUT_MODE` yn **1. Settyansow** ha chanjya settyansow erel mar res.
2. Dewis **Runtime → Run all**.
3. Gans `INPUT_MODE = "upload"`, dewis restrennow yn **2. Dewis restrenn / mountya Google Drive**.
4. An ZIP askorrans a vydh iskargeth yn awtomatek wosa an oberyans.

## Modhow amsernod

- `none`: data amser vyth.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Restrennow hir

`CHUNK_SECONDS` a dhyghtya hirder an chunk a-devnydhir yn an-kres rag restrennow hir. Gwerthow brassa a lehe rannow ha a with moy a destenn, mes a wra pub inference moy posek hag a yll devnydhya moy kov GPU. Gwerthow byhan a wra pub inference esya mes a wra moy a rannow, hag an re ma a yll bos posek dhe aswonnans yn ogas dhe’n poyntys. An gwerth defowt a wra talvos yn an liesa kasow.

## UI leel

An model ASR y honan yw **Japanek hepken**. Leelheans an README ha UI Colab a wra kudha oll an **183 taves ISO 639 Set 1 oberys** (`sh` koselhes a-dhiawel).

Sowsnek (`en`) yw an pennfenten canonical rag treusheans. Japanek (`ja`) yw treusheans adolygyes hag a vydh kopyes dhe wris an repository avel displegyans defowt `README.md`. README Japanek an wris **na vydh** devnydhys avel pennfenten treusheans. An 181 locale arall a vydh treusys dre beythin dhyworth Sowsnek.

## Notennow

- An notebook a hedha kyns treuskrifa mar nyns eus GPU kavadow.
- An termyn oberyans a omgelwel orth hirder an input, an settyansow ha'n GPU roys gans Colab. An kensa redyans a iskarg ynwedh NeMo ha'n model a-dro dhe 1.23 GB.
- Son hir a vydh oberys yn chunkow yn an-kres, hag y fydh possybyl dhe aswonnans bos effeythys yn ogas dhe rannow chunk.

## Pennfenten canonical ha genesans

Pennfentenow canonical treusadow:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` yw an snapshot canonical synkronys. Japanek yw gwithys avel treusheans adolygyes yn `locales/ja.json`, hag y snapshot README a vydh kopyes dhe wris `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Dalyans treusheans yw diblans dhyworth CI gnasek. Nyns eus res dhe devnydhoryon gnasek na CI kavos kredensyals treusheans.

## Lysens

Scaffold an notebook ha scriptow build/check yw lysensys MIT. An model Third Intelligence na vydh dasrannys omma hag yw gouvernys gans **Apache-2.0**. Dependensow parti tressa a with aga lysensow aga honan.
