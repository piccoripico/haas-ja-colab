# Haas Japanese Colab

Google Colab notebook handikana ho soratra ny audio sy video Japoney amin'ny Third Intelligence **Haas-ja-v1.0**.

[![Sokafy ao Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_mg.ipynb)

## Endri-javatra

- **Maimaim-poana:** Mandeha amin'ny GPU runtime maimaim-poana an'ny Google Colab.
- **Japanese ASR:** Mampiasa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model manana parameters eo amin'ny 0.6B ho an'ny Japanese speech recognition.
- **Haingana:** Azo atao haingana ny transcription.
- **Mari-piatoana:** Mamoaka Japanese punctuation tombanana ny model.
- **Timestamps sy subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Fanodinana rakitra lava:** Azo atao koa ny manodina audio sy video files lava.
- **Google Drive support:** Upload files mivantana na vakio avy amin'ny Google Drive; azo tehirizina ao amin'ny Drive ny output ZIP raha ilaina.
- **Outputs maro:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ary ZIP.

## Fampiasana

1. Safidio ny `INPUT_MODE` ao amin'ny **1. Settings** ary amboary ny settings hafa raha ilaina.
2. Safidio ny **Runtime → Run all**.
3. Raha `INPUT_MODE = "upload"`, safidio ny files ao amin'ny **2. File selection / Google Drive mount**.
4. Download ho azy ny output ZIP rehefa vita ny processing.

## Timestamp modes

- `none`: tsy misy timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files lava

`CHUNK_SECONDS` mifehy ny internal chunk duration ampiasaina amin'ny files lava. Values lehibe mampihena boundaries sy mitahiry context bebe kokoa, nefa mampavesatra ny inference tsirairay ary mety hampitombo GPU memory usage. Values kely manamaivana ny inference tsirairay nefa mamorona boundaries maro kokoa, izay mety hisy fiantraikany amin'ny recognition manodidina ireo toerana ireo. Ny default no atolotra amin'ny ankamaroan'ny tranga.

## UI voadika amin'ny fiteny maro

Ny ASR model mihitsy dia **Japanese-only**. Ny localization an'ny README sy Colab UI dia mandrakotra ny **183 active ISO 639 Set 1 languages** rehetra (tsy ao ny deprecated `sh`).

English (`en`) no canonical translation source. Japanese (`ja`) dia reviewed translation ary kopia ao amin'ny repository root ho default `README.md` presentation. Ny root Japanese README dia **tsy ampiasaina** ho translation source. Ny locales 181 hafa dia machine-translated avy amin'ny English.

## Fanamarihana

- Mijanona alohan'ny transcription ny notebook raha tsy misy GPU.
- Miankina amin'ny halavan'ny input, settings, ary GPU nomen'i Colab ny processing time. Amin'ny run voalohany dia download ihany koa ny NeMo sy ny model eo amin'ny 1.23 GB.
- Long audio dia odina amin'ny internal chunks, ka mety hisy fiantraikany amin'ny recognition manodidina chunk boundaries.

## Canonical source sy generation

Loharano kanônika azo adika:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` no synchronized canonical snapshot. Japanese dia tazonina ho reviewed translation ao amin'ny `locales/ja.json`, ary ny README snapshot-ny dia kopia ao amin'ny root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance dia misaraka amin'ny ordinary CI. Ordinary users sy CI tsy mila translation credentials.

## Lisansa

Notebook scaffolding sy build/check scripts dia MIT licensed. Ny Third Intelligence model tsy redistribute eto ary fehezin'ny **Apache-2.0**. Third-party dependencies mitazona ny licenses azy.
