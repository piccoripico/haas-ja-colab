# Haas Japanese Colab

He Google Colab notebook hei whakawhiti i ngā kōnae oro me ngā ataata Hapanihi ki te tuhinga mā Third Intelligence **Haas-ja-v1.0**.

[![Whakatuwhera ki Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_mi.ipynb)

## Ngā āhuatanga

- **Kore utu:** Ka rere i te GPU runtime kore utu o Google Colab.
- **Japanese ASR:** Ka whakamahi i [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), he model e tata ana ki te 0.6B parameters mō te Japanese speech recognition.
- **Tere:** Ka taea te tukatuka tere i te transcription.
- **Tohutuhi:** Ka whakaputa te model i te Japanese punctuation kua whakatau tatahia.
- **Timestamps me subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Tukatuka kōnae roa:** Ka taea hoki te tukatuka i ngā audio me video files roa.
- **Tautoko Google Drive:** Upload tika i ngā files, pānui rānei i Google Drive; ka taea te tiaki i te output ZIP ki Drive mēnā e hiahiatia ana.
- **He maha ngā outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, me ZIP.

## Te whakamahi

1. Kōwhiria `INPUT_MODE` i **1. Settings**, ā, whakatikahia ētahi atu settings mēnā e hiahiatia ana.
2. Kōwhiria **Runtime → Run all**.
3. Ina `INPUT_MODE = "upload"`, kōwhiria ngā files i **2. File selection / Google Drive mount**.
4. Ka download aunoa te output ZIP i muri i te mutunga o te processing.

## Ngā timestamp modes

- `none`: kāore he timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Ngā files roa

Ka whakahaere `CHUNK_SECONDS` i te internal chunk duration mō ngā files roa. Ka whakaiti ngā values nui i ngā boundaries me te pupuri context nui ake, engari ka taumaha ake ia inference, ā, tērā pea ka nui ake te GPU memory usage. Ka māmā ake ia inference ki ngā values iti, engari ka hanga boundaries maha ake, ka pā pea ki te recognition huri noa i aua wāhi. Ko te default te mea e taunakitia ana i te nuinga o ngā wā.

## UI kua whakarākeitia ki ngā reo

Ko te ASR model ake he **Japanese-only**. Ka kapi te localization o README me Colab UI i ngā **183 active ISO 639 Set 1 languages** katoa (kua tangohia te deprecated `sh`).

Ko English (`en`) te canonical translation source. Ko Japanese (`ja`) he reviewed translation, ā, ka copy ki te repository root hei default `README.md` presentation. Ko te root Japanese README **kāore** e whakamahia hei translation source. Ko ngā locales 181 atu he machine-translated mai i English.

## Ngā kōrero

- Ka mutu te notebook i mua i te transcription mēnā kāore he GPU.
- Ka whakawhirinaki te processing time ki te roa o te input, ngā settings, me te GPU ka tohaina e Colab. I te run tuatahi, ka download hoki a NeMo me te model e tata ana ki te 1.23 GB.
- Ka tukatukahia te long audio ki ngā internal chunks, nō reira ka pā pea ki te recognition i te taha o ngā chunk boundaries.

## Canonical source me generation

Ngā pūtake matua ka taea te whakamāori:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Ko `locales/en.json` te synchronized canonical snapshot. Ka puritia te Japanese hei reviewed translation i `locales/ja.json`, ā, ka copy tana README snapshot ki te root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

He wehe te translation maintenance i te ordinary CI. Kāore ngā ordinary users me CI e hiahia translation credentials.

## Raihana

Ko te Notebook scaffolding me ngā build/check scripts he MIT licensed. Kāore te Third Intelligence model e redistribute ki konei, ā, kei raro i te **Apache-2.0**. Ka pupuri ngā third-party dependencies i ā rātou ake licenses.
