# Haas Japanese Colab

O se Google Colab notebook e faaliliu ai leo ma vitio faa-Iapani i tusitusiga i le Third Intelligence **Haas-ja-v1.0**.

[![Tatala i Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sm.ipynb)

## Vaega autū

- **E leai se totogi:** E tamoʻe i le GPU runtime e leai se totogi a Google Colab.
- **Japanese ASR:** E faaaogā [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), o se model e tusa ma le 0.6B-parameter mo le iloaina o le gagana Iapani.
- **Vave:** E mafai ona process vave le transcription.
- **Faailoga:** E output e le Model punctuation faa-Iapani ua fuafuaina.
- **Timestamp ma subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** E mafai foʻi ona process audio ma video file uumi.
- **Google Drive support:** Upload saʻo file pe faitau mai Google Drive; e mafai ona save le output ZIP i Drive pe a manaʻomia.
- **Output eseese:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ma ZIP.

## Faaaogāina

1. Filifili `INPUT_MODE` i le **1. Settings** ma suia isi setting pe a manaʻomia.
2. Filifili **Runtime → Run all**.
3. Afai `INPUT_MODE = "upload"`, filifili file i le **2. File selection / Google Drive mount**.
4. A uma le processing, e download otometi le output ZIP.

## Timestamp modes

- `none`: e leai se timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File uumi

O `CHUNK_SECONDS` e pulea le umi o le internal chunk mo file uumi. O value tetele e faaitiitia boundary ma taofia atili context, ae e mamafa ai inference taʻitasi ma ono faateleina le GPU memory. O value laiti e mama ai inference taʻitasi ae faia ai boundary e tele, lea e mafai ona aafia ai recognition i na vaega. E fautuaina le default i le tele o tulaga.

## UI ua faaliliuina

O le ASR model lava ia e **Japanese-only**. O le README ma le Colab UI localization e aofia uma ai **183 active ISO 639 Set 1 languages** (e lē aofia ai le deprecated `sh`).

O English (`en`) o le canonical translation source. O Japanese (`ja`) o se reviewed translation ma e copy i le repository root e avea ma default `README.md` presentation. O le root Japanese README e **lē faaaogāina** e fai ma translation source. O isi 181 locales ua machine-translated mai English.

## Faamatalaga

- E taofi le notebook a o leʻi amata transcription pe a leai se GPU.
- O le processing time e faalagolago i le umi o le input, setting, ma le GPU e tofia e Colab. I le run muamua e download foʻi NeMo ma le model e tusa ma le 1.23 GB.
- O audio uumi e process i internal chunks, o lea e ono aafia ai recognition i tafatafa o chunk boundaries.

## Canonical source ma generation

Punaoa autū e mafai ona faaliliuina:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

O `locales/en.json` o le synchronized canonical snapshot. O Japanese e tausia o se reviewed translation i `locales/ja.json`, ma e copy lona README snapshot i le root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

E ese le translation maintenance mai ordinary CI. E lē manaʻomia e ordinary users ma CI ni translation credentials.

## License

O notebook scaffolding ma build/check scripts e MIT licensed. E lē redistributed iinei le Third Intelligence model ma e pulea e **Apache-2.0**. E tumau pea license a third-party dependencies.
