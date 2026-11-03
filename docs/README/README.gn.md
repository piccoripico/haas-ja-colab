# Haas Japanese Colab

Peteĩ Google Colab notebook oñembohasáva Japonés audio ha video jehaipyre-pe Third Intelligence **Haas-ja-v1.0** rupive.

[![Eipe'a Colab-pe](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_gn.ipynb)

## Mba'e ikatúva ojapo

- **Reiete:** Omba'apo Google Colab GPU runtime reiete rehe.
- **Japonés ASR:** Oipuru [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), peteĩ model haimete 0.6B-parameter Japonés speech recognition-pe g̃uarã.
- **Pya'e:** Ikatu oñeprocess pya'e transcription.
- **Punctuation:** Model omosẽ Japonés punctuation oñeimo'ãva.
- **Timestamp ha subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Ikatu avei oñeprocess audio ha video file ipukúva.
- **Google Drive support:** Eupload file directamente térã emoñe'ẽ Google Drive-gui; output ZIP ikatu oñesave Drive-pe reipotáma.
- **Output heta:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ha ZIP.

## Jepuru

1. Eiporavo `INPUT_MODE` **1. Settings**-pe ha emoambue ambue setting tekotevẽramo.
2. Eiporavo **Runtime → Run all**.
3. `INPUT_MODE = "upload"` ramo, eiporavo file **2. File selection / Google Drive mount**-pe.
4. Processing opa rire output ZIP oñedownload ijeheguiete.

## Timestamp modes

- `none`: ndaipóri timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File ipukúva

`CHUNK_SECONDS` oisãmbyhy internal chunk pukukue ojepurúva file ipukúvape. Value tuicháva omomichĩ boundary ha oñongatuve context, katu inference peteĩteĩ ipohyive ha ikatu oipuruve GPU memory. Value michĩva ombovevýi inference peteĩteĩ katu ojapo boundary hetave, ha upéva ikatu ombyai recognition umi tenda jerére. Hetave jave oñemoneĩ default.

## UI oñembohasáva

ASR model ijeheguínte **Japanese-only**. README ha Colab UI localization oike opaite **183 active ISO 639 Set 1 languages**-pe (deprecated `sh` ndoikéi).

English (`en`) ha'e canonical translation source. Japanese (`ja`) ha'e reviewed translation ha oñecopy repository root-pe default `README.md` presentation ramo. Root Japanese README **ndojejapói** translation source ramo. Ambue 181 locales oñemachine-translate English-gui.

## Marandu

- Notebook opyta transcription mboyve ndaipóriramo GPU.
- Processing time odepende input pukukue, setting, ha GPU Colab ome'ẽvare. Run peteĩháme oñedownload avei NeMo ha model haimete 1.23 GB.
- Audio ipukúva oñeprocess internal chunks-pe, upévare recognition ikatu oñembyai chunk boundaries jerére.

## Canonical source ha generation

Ypykuéra canonical ikatúva oñembohasa ñe’ẽme:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ha'e synchronized canonical snapshot. Japanese oñeñongatu reviewed translation ramo `locales/ja.json`-pe, ha README snapshot oñecopy root `README.md`-pe.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance oĩ aparte ordinary CI-gui. Ordinary users ha CI noikotevẽi translation credentials.

## License

Notebook scaffolding ha build/check scripts ha'e MIT licensed. Third Intelligence model noñeredistribuíri ko'ápe ha oĩ **Apache-2.0** poguýpe. Third-party dependencies oñongatu i-license kuéra.
