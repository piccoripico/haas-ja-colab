# Haas Japanese Colab

Google Colab notebook min bɛ Japonkan audio ni video sɛbɛnna Third Intelligence **Haas-ja-v1.0** fɛ.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_bm.ipynb)

## Nafaw

- **Fu:** A bɛ boli Google Colab ka GPU runtime fu kan.
- **Japonkan ASR:** A bɛ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) kɛ, model min bɛ se ka Japonkan kuma dɔn, a bɛɛ bɛ 0.6B parameter ɲɔgɔn na.
- **Teli:** Transcription bɛ se ka kɛ teliman na.
- **Punctuation:** Model bɛ Japonkan punctuation min bɛ miiri a kan, o bɔ.
- **Waati tamasiyɛn ni subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File janw labaarali:** Audio ni video file janw fana bɛ se ka labaarali.
- **Google Drive dɛmɛ:** Filew upload kɛ kelen-kelen walima u kalan ka bɔ Google Drive la; output ZIP bɛ se ka mara Drive la ni i b’a fɛ.
- **Output caman:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ni ZIP.

## A kɛcogo

1. `INPUT_MODE` sugandi **1. Settings** kɔnɔ, ka setting tɔw labɛn ni a mako bɛ.
2. **Runtime → Run all** sugandi.
3. Ni `INPUT_MODE = "upload"`, filew sugandi **2. File selection / Google Drive mount** kɔnɔ.
4. Processing ban kɔfɛ, output ZIP bɛ jigin a yɛrɛ ma.

## Timestamp modew

- `none`: waati kunnafoni tɛ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File janw

`CHUNK_SECONDS` bɛ internal chunk waati hakɛ mara file janw kama. Hakɛ belebelebaw bɛ boundaryw dɔgɔya ka context caman mara, nka u bɛ inference kelen-kelen girinya ka GPU memory labaarali bɔ. Hakɛ dɔgɔmanw bɛ inference nogoya nka u bɛ boundary caman dilan, min bɛ se ka recognition nɔgɔn na o yɔrɔw la. Cogoya caaman na, default ye ɲuman ye.

## UI min bɛ bamanankan na

ASR model yɛrɛ ye **Japonkan dɔrɔn** ye. README ni Colab UI localization bɛ **ISO 639 Set 1 kan 183 minnu bɛ kɛ**, olu bɛɛ datugu (`sh` min tɛ kɛ tuguni ma bɔ a kɔnɔ).

Angilɛkan (`en`) ye canonical translation source ye. Japonkan (`ja`) ye translation min lajɛra ye, a bɛ copy kɛ repository root la ka kɛ default `README.md` ye. Root Japonkan README **tɛ kɛ translation source ye**. Locale 181 tɔw bɛ machine-translate ka bɔ Angilɛkan na.

## Kɔlɔsiliw

- Ni GPU tɛ yen, notebook bɛ jɔ sani transcription ka daminɛ.
- Processing waati bɛ input jan, settingw, ni GPU min Colab b’a di, olu kan. Run fɔlɔ fana bɛ NeMo ni model min bɛ 1.23 GB ɲɔgɔn na jigin.
- Audio jan bɛ labaarali internal chunkw la, o la recognition bɛ se ka fanga dɔgɔya chunk boundaryw kɛrɛfɛ.

## Canonical source ni generation

Canonical source minnu bɛ se ka translate:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ye synchronized canonical snapshot ye. Japonkan bɛ mara `locales/ja.json` la ka kɛ translation lajɛlen ye, ani a ka README snapshot bɛ copy kɛ root `README.md` la.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ni CI kɔrɔlen tɛ kelen ye. User kɔrɔlenw ni CI mako tɛ translation credential la.

## License

Notebook scaffolding ni build/check scripts bɛ MIT license kɔnɔ. Third Intelligence model tɛ lajɛgin yan, a bɛ **Apache-2.0** kɔrɔ. Third-party dependencies bɛ u yɛrɛ ka licensew mara.
