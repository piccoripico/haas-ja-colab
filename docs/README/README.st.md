# Haas Japanese Colab

Google Colab notebook bakeng sa ho fetolela audio le video ea Sejapane hore e be mongolo ka Third Intelligence **Haas-ja-v1.0**.

[![Bula ho Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_st.ipynb)

## Likarolo

- **Mahala:** E sebetsa ho GPU runtime ea mahala ea Google Colab.
- **Japanese ASR:** E sebelisa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model e nang le parameters tse ka bang 0.6B bakeng sa ho lemoha puo ea Sejapane.
- **Ka potlako:** Transcription e ka sebetsoa ka potlako.
- **Matšoao a puo:** Model e hlahisa Japanese punctuation eo e e hakantseng.
- **Timestamps le subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ho sebetsa files tse telele:** Audio le video files tse telele le tsona li ka sebetsoa.
- **Tšehetso ea Google Drive:** Upload files ka kotloloho kapa u li bale ho Google Drive; output ZIP e ka bolokoa ho Drive haeba ho lakatseha.
- **Outputs tse ngata:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, le ZIP.

## Mokhoa oa ho sebelisa

1. Khetha `INPUT_MODE` ho **1. Settings** 'me u fetole settings tse ling haeba ho hlokahala.
2. Khetha **Runtime → Run all**.
3. Ha `INPUT_MODE = "upload"`, khetha files ho **2. File selection / Google Drive mount**.
4. Output ZIP e download ka bo eona ka mor'a hore processing e qete.

## Timestamp modes

- `none`: ha ho timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files tse telele

`CHUNK_SECONDS` e laola internal chunk duration e sebelisoang bakeng sa files tse telele. Values tse kholo li fokotsa boundaries 'me li boloka context e ngata, empa inference ka 'ngoe e ba boima 'me e ka sebelisa GPU memory e ngata. Values tse nyenyane li etsa hore inference ka 'ngoe e be bobebe empa li hlahisa boundaries tse ngata, tse ka amang recognition haufi le libaka tseo. Default e khothaletsoa maemong a mangata.

## UI e fetoletsoeng

ASR model ka boeona ke **Japanese-only**. Localization ea README le Colab UI e akaretsa **183 active ISO 639 Set 1 languages** kaofela (deprecated `sh` e tlositsoe).

English (`en`) ke canonical translation source. Japanese (`ja`) ke reviewed translation 'me e kopitsoa repository root e le default `README.md` presentation. Root Japanese README **ha e sebelisoe** e le translation source. Locales tse ling tse 181 ke machine-translated ho tsoa English.

## Lintlha

- Notebook e ema pele ho transcription haeba GPU e sa fumanehe.
- Processing time e itšetlehile ka bolelele ba input, settings, le GPU e abetsoeng ke Colab. Run ea pele e boetse e download NeMo le model ea hoo e ka bang 1.23 GB.
- Long audio e sebetsoa ka internal chunks, kahoo recognition e ka ameha haufi le chunk boundaries.

## Canonical source le generation

Mehloli ya motheo e ka fetolelwang:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ke synchronized canonical snapshot. Japanese e bolokoa e le reviewed translation ho `locales/ja.json`, 'me README snapshot ea eona e kopitsoa ho root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance e arohane le ordinary CI. Ordinary users le CI ha ba hloke translation credentials.

## License

Notebook scaffolding le build/check scripts li na le MIT license. Third Intelligence model ha e abeloe hape mona 'me e laoloa ke **Apache-2.0**. Third-party dependencies li boloka licenses tsa tsona.
