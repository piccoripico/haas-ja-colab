# Haas Japanese Colab

Google Colab notebook yaozdāna- Japon audio ud video transcribe-kərəna, Third Intelligence **Haas-ja-v1.0** frāyōzaṇt.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ae.ipynb)

## Hu-šyaoθna

- **Aṣ̌a-xšaθra:** Google Colab free GPU runtime andar šyaoθna kərənaoiti.
- **Japon ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) frāyōzaṇt, Japon vaca-āšnāna model, 0.6B parameter-ō.
- **Tūirya:** Transcription tūirya kərəna vīspəm.
- **Punctuation:** Model Japon punctuation fraošaiti, anumāna-kərəta.
- **Timestamp ud subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Darəga file šyaoθna:** Darəga audio ud video file-ča šyaoθna kərəna vīspəm.
- **Google Drive upastāna:** File direct upload kərəna vā Google Drive haca paθa; output ZIP Drive andar nizaŋha pairi-rakšaiti.
- **Pouru output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## Frāyōzana

1. `INPUT_MODE` **1. Settings** andar vīcina, anya settings yadi xšnūta fraša kərəna.
2. **Runtime → Run all** vīcina.
3. `INPUT_MODE = "upload"` yadi asti, file **2. File selection / Google Drive mount** andar vīcina.
4. Šyaoθna para, output ZIP xvaθra download kərənaoiti.

## Timestamp mode

- `none`: kāla-dāta nāsti.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Darəga file

`CHUNK_SECONDS` darəga file-āi internal chunk kāla pairi-kərənaoiti. Mašya value boundary kamaiti ud context pouru pairi-rakšaiti, aŋhat inference gouru kərənaoiti ud GPU memory pouru yōzaṇt. Kasyā value inference laghu kərənaoiti aŋhat boundary pouru frajanaiti, yō recognition tatra pairi-bāδaiti. Aŋhu pouru, default huda asti.

## Paourui.dāna UI

ASR model xva **Japon vaca-ēva** asti. README ud Colab UI localization **183 active ISO 639 Set 1 vaca** vīspā cover kərənaoiti (`sh` apākərəta).

English (`en`) canonical translation source asti. Japon (`ja`) reviewed translation asti ud repository root andar default `README.md` daršana-āi copy kərənaoiti. Root Japon README **translation source nōit frāyōzaṇt**. Anya 181 locale English haca machine-translate kərənaoiti.

## Niyāyəm

- GPU nāsti yadi, notebook transcription paouru para staṇt.
- Processing kāla input darəga, settings, ud Colab-dāta GPU pairi-bāδaiti. Fratəma run NeMo ud 1.23 GB model download kərənaoiti.
- Darəga audio internal chunk andar šyaoθna kərənaoiti, yō recognition chunk boundary narə pairi-bāδaiti.

## Canonical source ud generation

Canonical translate-ya source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot asti. Japon `locales/ja.json` andar reviewed translation pairi-rakšaiti, ud README snapshot root `README.md` andar copy kərənaoiti.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI haca fraša asti. Ordinary users ud CI translation credentials nōit xšaēta.

## License

Notebook scaffolding ud build/check scripts MIT license asti. Third Intelligence model ita nōit redistributem, **Apache-2.0** gubarə. Third-party dependencies xva license pairi-rakšaiti.
