# Haas Japanese Colab

Google Colab notebook ti transcrire audio na vidéo ti Japonais na text na Third Intelligence **Haas-ja-v1.0**.

[![Zingo na Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sg.ipynb)

## Ayeke ti lo

- **Nzoni na mbongo pepe:** Lo yeke gi na GPU runtime ti Google Colab so ayeke na mbongo pepe.
- **Japanese ASR:** Lo yeke sara na [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ti 0.6B-parameter tongana so mpo na Japanese speech recognition.
- **Hio:** Transcription alingbi ti process hio.
- **Punctuation:** Model ayeke pika Japanese punctuation so lo pensé.
- **Timestamp na subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio na video file so ayeke kota alingbi mpe ti process.
- **Google Drive support:** Upload file droit wala diko azo ti lo na Google Drive; output ZIP alingbi ti save na Drive tongana mo ye.
- **Output mingi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Legue ti sara na ni

1. Hiri `INPUT_MODE` na **1. Settings** na changé setting oko tongana ayeke na besoin.
2. Hiri **Runtime → Run all**.
3. Tongana `INPUT_MODE = "upload"`, hiri file na **2. File selection / Google Drive mount**.
4. Tongana processing awu, output ZIP ayeke download lo oko.

## Timestamp modes

- `none`: timing information ayeke pepe.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File kota

`CHUNK_SECONDS` ayeke commander longueur ti internal chunk so ayeke sara na file kota. Value kota ayeke kiri boundary na sese na bata context mingi, mais inference oko oko ayeke kota na alingbi ti za GPU memory mingi. Value kete ayeke sala inference oko oko facile mais ayeke sala boundary mingi, so alingbi ti touché recognition na ndö ni. Na mbage mingi, default ayeke nzoni.

## UI so atraduire

ASR model lo oko ayeke **Japanese-only**. README na Colab UI localization ayeke couvrir **183 active ISO 639 Set 1 languages** kue (deprecated `sh` ayeke na ni pepe).

English (`en`) ayeke canonical translation source. Japanese (`ja`) ayeke reviewed translation na ayeke copy na repository root tongana default `README.md` presentation. Root Japanese README **ayeke sara pepe** tongana translation source. Locale 181 so asigigi ayeke machine-translated tî English.

## Atene ti hinga

- Notebook ayeke londo avant transcription tongana GPU ayeke pepe.
- Processing time ayeke depend na longueur ti input, setting, na GPU so Colab apesi. Na run ti kozo, NeMo na model ti 1.23 GB tongana so ayeke download mpe.
- Audio kota ayeke process na internal chunks, tongana ni recognition alingbi ti changé na chunk boundaries.

## Canonical source na generation

Âsource ti mbênî so alingbi ti traduction:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ayeke synchronized canonical snapshot. Japanese ayeke bata tongana reviewed translation na `locales/ja.json`, na README snapshot ti lo ayeke copy na root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ayeke separate na ordinary CI. Ordinary users na CI ayeke na besoin ti translation credentials pepe.

## License

Notebook scaffolding na build/check scripts ayeke MIT licensed. Third Intelligence model ayeke redistribute na ndo so pepe na **Apache-2.0** ayeke commander ni. Third-party dependencies ayeke bata licenses ti azo.
