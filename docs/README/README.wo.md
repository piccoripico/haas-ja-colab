# Haas Japanese Colab

Google Colab notebook ngir tekki audio ak video bu Japon ci mbind ak Third Intelligence **Haas-ja-v1.0**.

[![Ubbi ci Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_wo.ipynb)

## Man-man yi

- **Dara du fay:** Dafay dox ci GPU runtime bu Google Colab di joxe doomu xel.
- **Japanese ASR:** Dafay jëfandikoo [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model bu am lu tollu ci 0.6B parameters ngir Japanese speech recognition.
- **Gaaw:** Mën nañu processing transcription bi ci gaaw.
- **Punctuation:** Model bi dafay génne Japanese punctuation yu mu xalaat.
- **Timestamps ak subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Processing file yu gudd:** Audio ak video files yu gudd itam mën nañu leen processing.
- **Google Drive support:** Upload files ci saasi walla jàng leen ci Google Drive; output ZIP mën nañu ko denc ci Drive bu fekkee bëgg nañu.
- **Outputs yu bari:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ak ZIP.

## Jëfandikoo

1. Tànn `INPUT_MODE` ci **1. Settings** te soppi yeneen settings su ko soxlaa.
2. Tànn **Runtime → Run all**.
3. Bu `INPUT_MODE = "upload"`, tànn files ci **2. File selection / Google Drive mount**.
4. Output ZIP bi dina download boppam gannaaw processing bi jeexee.

## Timestamp modes

- `none`: amul timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Files yu gudd

`CHUNK_SECONDS` moo di saytu internal chunk duration bi ñuy jëfandikoo ci files yu gudd. Values yu mag dañuy wàññi boundaries te denc context bu bari, waaye inference bu nekk dina gëna diis te mën na yokk GPU memory usage. Values yu ndaw dañuy yombal inference bu nekk waaye dañuy sos boundaries yu bari, loolu mën na laal recognition ci wet yooyu. Default bi lañu gëna digle ci lu ëpp.

## UI bu lokalize

ASR model bi boppam **Japanese-only** la. Localization README ak Colab UI dafay couvré lépp **183 active ISO 639 Set 1 languages** (deprecated `sh` du ci).

English (`en`) mooy canonical translation source. Japanese (`ja`) mooy reviewed translation te ñu copy ko ci repository root ngir mu doon default `README.md` presentation. Root Japanese README **du** translation source. 181 locales yi des ñu ngi leen machine-translated ci English.

## Kàddu yu am solo

- Notebook bi dina taxaw bala transcription su GPU amul.
- Processing time mi aju na ci guddaayu input, settings, ak GPU bi Colab joxe. Ci run bu njëkk, NeMo ak model bi tollu ci 1.23 GB itam ñu ngi leen download.
- Long audio ñu ngi ko processing ci internal chunks, kon recognition mën na am jafe-jafe ci chunk boundaries.

## Canonical source ak generation

Gongikuwaay yu sax yi ñu man a tekki:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` mooy synchronized canonical snapshot. Japanese ñu ngi ko denc ni reviewed translation ci `locales/ja.json`, te README snapshotam ñu ngi ko copy ci root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance wuute na ak ordinary CI. Ordinary users ak CI soxlawuñu translation credentials.

## License

Notebook scaffolding ak build/check scripts ñu ngi ci MIT licensed. Third Intelligence model bi ñu ko dul redistribute fii, te **Apache-2.0** moo koy saytu. Third-party dependencies dañuy denc seen licenses.
