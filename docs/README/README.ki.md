# Haas Japanese Colab

Notebook ya Google Colab ya kũandĩka mũgambo wa Kĩjapani kuuma kũrĩ audio na video na Third Intelligence **Haas-ja-v1.0**.

[![Hingũra na Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ki.ipynb)

## Maũndũ marĩa ĩngĩhota

- **Ya tũhũ:** Ĩthĩaga na GPU runtime ya tũhũ ya Google Colab.
- **ASR ya Kĩjapani:** Ĩhũthagĩra [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ĩrĩ na parameters ta 0.6B ya kũmenya mũgambo wa Kĩjapani.
- **Na ihenya:** Transcription nĩ ĩngĩhota gũthondekwo na ihenya.
- **Tũmenyithia twa maũndĩko:** Model nĩ ĩrutaga tũmenyithia twa Kĩjapani tũrĩa ĩkuona tũrĩ two.
- **Timestamps na subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Kũthondeka file nene:** Audio na video file nene nacio nĩ ingĩthondekwo.
- **Google Drive:** Upload file o rĩmwe kana ũthome kuuma Google Drive; output ZIP no ĩigwo Drive ũngĩenda.
- **Output nyingi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Ũrĩa wa kũhũthĩra

1. Thuura `INPUT_MODE` thĩinĩ wa **1. Settings** na ũgarũre settings ingĩ angĩkorwo nĩ no nginya.
2. Thuura **Runtime → Run all**.
3. Na `INPUT_MODE = "upload"`, thuura file thĩinĩ wa **2. File selection / Google Drive mount**.
4. Output ZIP nĩ ĩdownloadagwo ĩyo nyene thuutha wa processing.

## Timestamp modes

- `none`: gũtirĩ maũndũ ma mahinda.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File nene

`CHUNK_SECONDS` nĩyo ĩtongoragia ũraihu wa internal chunk ũhũthĩtwo file nene. Value nene nĩ inyihagia boundaries na igũtigĩra context nyingĩ, no kila inference ĩkagĩa ũritũ na ĩhũthĩre GPU memory nyingĩ. Value nini nĩ igũtũma kila inference ĩgĩe nyũmba, no igathondeka boundaries nyingĩ, iria ingĩthĩĩnia recognition hakuhi nacio. Default nĩyo ĩrathimwo maita maingĩ.

## UI ya thiĩna wa locale

ASR model ĩyo nyene nĩ **ya Kĩjapani tu**. README na Colab UI localization nĩ ĩhumbaga **ndimi 183 iria irĩ active ISO 639 Set 1** (`sh` ya tene ndĩrĩmo).

Gĩthungu (`en`) nĩ canonical translation source. Kĩjapani (`ja`) nĩ translation ĩrĩa ĩthuthurĩtwo na ĩkopiwo mũthia-inĩ wa repository ta default `README.md`. Root Japanese README **ndĩhũthagĩrwo** ta translation source. Locale ingĩ 181 nĩ iratranslate-gwo na machine kuuma Gĩthungu.

## Maũndũ ma kũmenya

- Notebook nĩ ĩtigaga mbere ya transcription angĩkorwo GPU ndĩrĩ.
- Processing time nĩ ĩrĩkaga na ũraihu wa input, settings, na GPU ĩrĩa Colab ĩheana. Run ya mbere nĩ ĩdownloadaga NeMo na model ya ta 1.23 GB o nayo.
- Audio nene nĩ ĩthondekagwo na internal chunks, nĩ ũndũ ũcio recognition no ĩthĩnĩke hakuhi na chunk boundaries.

## Canonical source na generation

Mĩthĩingi ya mbere ya gũtaũrwo:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` nĩ synchronized canonical snapshot. Kĩjapani nĩ gĩtũũraga ta reviewed translation thĩinĩ wa `locales/ja.json`, na README snapshot yakĩo ĩkopiwo root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance nĩ ya mwanya kuuma ordinary CI. Ordinary users na CI matirĩ na bata wa translation credentials.

## License

Notebook scaffolding na build/check scripts nĩ MIT licensed. Third Intelligence model ndĩredistribute-gwo haha na ĩtongoragwo nĩ **Apache-2.0**. Third-party dependencies nĩ itigaga licenses ciacio.
