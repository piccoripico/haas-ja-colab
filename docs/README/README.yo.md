# Haas Japanese Colab

Google Colab notebook fún yíyí ohùn àti fídíò Japanese padà sí ìkọ̀wé pẹ̀lú Third Intelligence **Haas-ja-v1.0**.

[![Ṣí ní Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_yo.ipynb)

## Àwọn ànfààní

- **Ọ̀fẹ́:** Ó ń ṣiṣẹ́ lórí GPU runtime ọ̀fẹ́ ti Google Colab.
- **Japanese ASR:** Ó ń lo [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model tó ní bí 0.6B parameters fún Japanese speech recognition.
- **Yára:** A lè ṣe transcription ní kíákíá.
- **Àwọn àmì ìkọ̀wé:** Model náà ń ṣe àgbéjáde Japanese punctuation tí a fojú díwọ̀n.
- **Timestamps àti subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Ṣíṣe àwọn file gígùn:** A tún lè ṣe audio àti video files gígùn.
- **Àtìlẹ́yìn Google Drive:** Upload files taara tàbí ka wọn láti Google Drive; a lè fi output ZIP pamọ́ sí Drive bí a bá fẹ́.
- **Ọ̀pọ̀ outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, àti ZIP.

## Bí a ṣe ń lò ó

1. Yan `INPUT_MODE` ní **1. Settings** kí o sì ṣàtúnṣe settings míì bí ó bá yẹ.
2. Yan **Runtime → Run all**.
3. Nígbà tí `INPUT_MODE = "upload"`, yan files ní **2. File selection / Google Drive mount**.
4. Output ZIP máa download fúnra rẹ̀ lẹ́yìn tí processing bá parí.

## Àwọn mode timestamp

- `none`: kò sí timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Àwọn file gígùn

`CHUNK_SECONDS` ń ṣàkóso internal chunk duration tí a lò fún files gígùn. Values tó tóbi dín boundaries kù, wọ́n sì pa context púpọ̀ mọ́, ṣùgbọ́n wọ́n mú inference kọ̀ọ̀kan wuwo, wọ́n sì lè pọ̀ sí GPU memory usage. Values kékeré mú inference kọ̀ọ̀kan rọrùn ṣùgbọ́n wọ́n ṣẹ̀dá boundaries púpọ̀, èyí tó lè ní ipa lórí recognition lẹ́gbẹ̀ẹ́ àwọn ibi wọ̀nyẹn. Default ni a dámọ̀ràn ní ọ̀pọ̀ ìgbà.

## UI tí a ṣe sí èdè agbègbè

ASR model fúnra rẹ̀ jẹ́ **Japanese-only**. Localization README àti Colab UI bo gbogbo **183 active ISO 639 Set 1 languages** (a yọ deprecated `sh` kúrò).

English (`en`) ni canonical translation source. Japanese (`ja`) jẹ́ reviewed translation, a sì ń copy rẹ̀ sí repository root gẹ́gẹ́ bí default `README.md` presentation. Root Japanese README **kì í ṣe** translation source. Àwọn locale 181 tó kù jẹ́ machine-translated láti English.

## Àwọn àkíyèsí

- Notebook máa dúró kí transcription tó bẹ̀rẹ̀ bí GPU kò bá sí.
- Processing time dale lórí gígùn input, settings, àti GPU tí Colab pín. Ní run àkọ́kọ́, NeMo àti model tó tó 1.23 GB tún máa download.
- Long audio ni a ń ṣe ní internal chunks, nítorí náà recognition lè ní ipa lẹ́gbẹ̀ẹ́ chunk boundaries.

## Canonical source àti generation

Àwọn orísun àkọ́kọ́ tí a lè túmọ̀:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ni synchronized canonical snapshot. Japanese ni a ń tọju gẹ́gẹ́ bí reviewed translation ní `locales/ja.json`, a sì ń copy README snapshot rẹ̀ sí root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance yàtọ̀ sí ordinary CI. Ordinary users àti CI kò nílò translation credentials.

## Ìwé-àṣẹ

Notebook scaffolding àti build/check scripts jẹ́ MIT licensed. Third Intelligence model kò tún pin káàkiri níbí, **Apache-2.0** ló sì ń ṣàkóso rẹ̀. Third-party dependencies pa licenses tiwọn mọ́.
