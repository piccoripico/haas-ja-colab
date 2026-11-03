# Haas Japanese Colab

Google Colab notebook, Third Intelligence **Haas-ja-v1.0** ia gaukaraia, Japanese audio bona video be torea text ai.

[![Colab ai kehoa](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ho.ipynb)

## Ia kara diba

- **Free:** Google Colab ena free GPU runtime dekenai gaukara.
- **Japanese ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ia gaukaraia; model be 0.6B parameter kahana, Japanese hereva ia diba neganai.
- **Harihari:** Transcription be harihari ai kara.
- **Punctuation:** Model be Japanese punctuation ia diba-gadogadola bona ia hahedinaraia.
- **Timestamps bona subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File lata gaukara:** Audio bona video file lata danu kara diba.
- **Google Drive support:** File be direct upload, o Google Drive amo duahia; output ZIP be ura neganai Drive ai dogo diba.
- **Output momo:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, bona ZIP.

## Gaukara dala

1. **1. Settings** dekenai `INPUT_MODE` abia, bona setting ma haidahia be haidahia.
2. **Runtime → Run all** abia.
3. `INPUT_MODE = "upload"` neganai, **2. File selection / Google Drive mount** dekenai file abia.
4. Gaukara ore neganai output ZIP be ena sibona download.

## Timestamp mode

- `none`: time information lasi.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File lata

`CHUNK_SECONDS` be file lata ena internal chunk time ia haheguda. Value bada be boundary ia haidauna bona context momo ia dogo, to inference ta ta be metau bona GPU memory momo ia gaukara diba. Value maragi be inference ia haimaoro, to boundary momo ia kara, bona unu be recognition ia haidika diba. Default value be maoro, lagani momo dekenai.

## UI hereva momo

ASR model ena sibona be **Japanese mo**. README bona Colab UI translation be **183 active ISO 639 Set 1 hereva** ibounai ia atoa (`sh` be old/deprecated, ia atoa lasi).

English (`en`) be canonical translation source. Japanese (`ja`) be reviewed translation, bona repository root ai `README.md` default presentation hegeregere ia copy. Root Japanese README be translation source ai **gaukaraia lasi**. Locale 181 ma be English amo machine-translate.

## Diba-diba

- GPU lasi neganai notebook be transcription gunanai ia ura.
- Processing time be input lata, settings, bona Colab ena GPU henia ia badina. Run guna neganai NeMo bona 1.23 GB hegeregere model danu be download.
- Audio lata be internal chunk ai gaukara, bena chunk boundary kahana dekenai recognition be haidika diba.

## Canonical source bona generation

Canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` be synchronized canonical snapshot. Japanese be reviewed translation ai `locales/ja.json` dekenai dogo, bona ena README snapshot be root `README.md` dekenai copy.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance be ordinary CI ida idau. Ordinary user bona CI be translation credentials idia ura lasi.

## License

Notebook scaffolding bona build/check script be MIT license. Third Intelligence model be unusenai redistribute lasi, bona **Apache-2.0** ena rule ia badina. Third-party dependency be edia sibona license idia dogo.
