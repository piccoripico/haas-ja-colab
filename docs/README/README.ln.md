# Haas Japanese Colab

Google Colab notebook mpo na kobongola audio mpe video ya Japon na text na Third Intelligence **Haas-ja-v1.0**.

[![Fungola na Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ln.ipynb)

## Makoki

- **Ofelé:** Esalaka na GPU runtime ya ofelé ya Google Colab.
- **Japanese ASR:** Esalelaka [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ya pene na 0.6B-parameter mpo na Japanese speech recognition.
- **Noki:** Transcription ekoki ko processama noki.
- **Punctuation:** Model ebimisaka Japanese punctuation oyo ekanisi ete ezali malamu.
- **Timestamp mpe subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio mpe video file milai ekoki mpe ko processama.
- **Google Drive support:** Upload file mbala moko to tangá yango na Google Drive; output ZIP ekoki ko save na Drive soki olingi.
- **Output ebele:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, mpe ZIP.

## Ndenge ya kosalela

1. Pona `INPUT_MODE` na **1. Settings** mpe bongola setting mosusu soki esengeli.
2. Pona **Runtime → Run all**.
3. Soki `INPUT_MODE = "upload"`, pona file na **2. File selection / Google Drive mount**.
4. Sima ya processing kosila, output ZIP eko download yango moko.

## Timestamp modes

- `none`: timing information ezali te.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File milai

`CHUNK_SECONDS` etambwisaka bolai ya internal chunk oyo esalelamaka mpo na file milai. Value minene ekitisaka boundary mpe ebombaka context mingi, kasi inference moko na moko ekómaka kilo mpe ekoki kosalela GPU memory mingi. Value mike ekómisaka inference pete kasi esalaka boundary mingi, oyo ekoki kobebisa recognition pene ya bisika wana. Na makambo mingi, default ezali malamu.

## UI ebongolami

ASR model yango moko ezali **Japanese-only**. README mpe Colab UI localization ezipaka **183 active ISO 639 Set 1 languages** nyonso (deprecated `sh` ezali na kati te).

English (`en`) ezali canonical translation source. Japanese (`ja`) ezali reviewed translation mpe e copy na repository root lokola default `README.md` presentation. Root Japanese README **esalelamaka te** lokola translation source. Locale 181 mosusu ezali machine-translated uta na English.

## Makambo ya koyeba

- Notebook etelemaka liboso ya transcription soki GPU ezali te.
- Processing time etalelaka bolai ya input, setting, mpe GPU oyo Colab epesi. Na run ya liboso, NeMo mpe model ya pene na 1.23 GB e downloadaka mpe.
- Audio molai e processama na internal chunks, yango wana recognition ekoki kobebisama pene ya chunk boundaries.

## Canonical source mpe generation

Maziba ya moboko oyo ekoki kobongolama:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ezali synchronized canonical snapshot. Japanese ebombami lokola reviewed translation na `locales/ja.json`, mpe README snapshot na yango e copy na root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ekeseni na ordinary CI. Ordinary users mpe CI basengeli translation credentials te.

## License

Notebook scaffolding mpe build/check scripts ezali MIT licensed. Third Intelligence model e redistributed awa te mpe etambwisami na **Apache-2.0**. Third-party dependencies ebombaka licenses na yango.
