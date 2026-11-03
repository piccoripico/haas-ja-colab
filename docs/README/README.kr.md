# Haas Japanese Colab

Google Colab notebook adə Third Intelligence **Haas-ja-v1.0** kəlan Japan audio-a video-a rubu kəjiro transcription dəga kəltə.

[![Colab lan fəle](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kr.ipynb)

## Fáida-a

- **Kudin bawo:** Google Colab free GPU runtime lan suwó kəla.
- **Japan ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) kəlan, Japan kalma fəlta ngam model 0.6B-parameter gade.
- **Gashí:** Transcription də gashíro process kəltə.
- **Punctuation:** Model də Japan punctuation təmajiro output kəla.
- **Timestamps-a subtitles-a:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File kəwur processing:** Audio-a video-a file kəwur so process kəltə.
- **Google Drive support:** File-a direct upload kəltə wala Google Drive lan kərá; output ZIP so so Drive lan save kəltə.
- **Output kada:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, a ZIP.

## Kəla istifadə

1. **1. Settings** lan `INPUT_MODE` fəle, setting gade so lazimma dəyiş kə.
2. **Runtime → Run all** fəle.
3. `INPUT_MODE = "upload"` ro, **2. File selection / Google Drive mount** lan file-a fəle.
4. Processing kənde, output ZIP automatikro download kəltə.

## Timestamp mode-a

- `none`: time information bawo.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File kəwur-a

`CHUNK_SECONDS` file kəwurro internal chunk hər one-a seconds ndú control kəla. Value kəwu boundary-a gəná kəla a context kada dəran, amma inference hər one də nəmji a GPU memory kada kəltə mumkin. Value gəná inference hər one də yəwú kəla, amma boundary kada kəla, sa recognition də kadəga dəriro dəyiş kəltə mumkin. Kulu default də fáida gade.

## UI bəlama

ASR model də **Japan kalma kəla**. README-a Colab UI localization də **183 active ISO 639 Set 1 languages** kulu səba (deprecated `sh` bawo).

English (`en`) canonical translation source gade. Japan (`ja`) reviewed translation gade, repository root lan default `README.md` fəlejiro copy kəltə. Root Japanese README də translation source **bawo**. Locale gade 181 English lan machine-translated kəltə.

## Ləmar-a

- GPU bawo ro notebook də transcription fuwun stop kəla.
- Processing time də input kəwur, setting-a, a Colab GPU-a kəla. First run lan NeMo-a model 1.23 GB-a so download kəltə.
- Audio kəwur internal chunk-a lan process kəltə, ngam chunk boundary kadəga lan recognition dəyiş kəltə mumkin.

## Canonical source-a generation-a

Canonical translatable source-a:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot gade. Japan də `locales/ja.json` lan reviewed translation ro dəran, README snapshot də root `README.md` ro copy kəltə.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance də ordinary CI lan separado. Ordinary user-a CI-a translation credentials lazim bawo.

## License

Notebook scaffolding-a build/check scripts-a MIT licensed. Third Intelligence model adə nde redistribute kəltə bawo, **Apache-2.0** kəlan. Third-party dependency-a license nəmbe dəran.
