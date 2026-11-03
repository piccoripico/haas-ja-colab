# Haas Japanese Colab

Google Colab notebook yolembera mawu ndi kanema wa Chijapani kukhala text pogwiritsa ntchito Third Intelligence **Haas-ja-v1.0**.

[![Tsegulani mu Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ny.ipynb)

## Zomwe imatha kuchita

- **Yaulere:** Imayenda pa GPU runtime yaulere ya Google Colab.
- **Japanese ASR:** Imagwiritsa ntchito [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ya pafupifupi 0.6B-parameter yozindikira mawu a Chijapani.
- **Yachangu:** Transcription imatha ku processidwa mwachangu.
- **Punctuation:** Model imatulutsa Japanese punctuation yomwe yayerekezera.
- **Timestamp ndi subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Audio ndi video file zazitali zimathanso ku processidwa.
- **Google Drive support:** Upload file mwachindunji kapena werengani kuchokera ku Google Drive; output ZIP imatha kusavedwa ku Drive mukafuna.
- **Output zosiyanasiyana:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ndi ZIP.

## Momwe mungagwiritsire ntchito

1. Sankhani `INPUT_MODE` mu **1. Settings** ndikusintha setting zina ngati pakufunika.
2. Sankhani **Runtime → Run all**.
3. Ngati `INPUT_MODE = "upload"`, sankhani file mu **2. File selection / Google Drive mount**.
4. Processing ikatha, output ZIP imadownload yokha.

## Timestamp modes

- `none`: palibe timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File zazitali

`CHUNK_SECONDS` imayang'anira kutalika kwa internal chunk kogwiritsidwa ntchito pa file zazitali. Value zazikulu zimachepetsa boundary ndikusunga context yambiri, koma inference iliyonse imakhala yolemera ndipo ingagwiritse ntchito GPU memory yambiri. Value zazing'ono zimapangitsa inference iliyonse kukhala yopepuka koma zimapanga boundary zambiri, zomwe zingakhudze recognition pafupi ndi malo amenewo. Nthawi zambiri default imalimbikitsidwa.

## UI yomasuliridwa

ASR model yokha ndi **Japanese-only**. README ndi Colab UI localization zimaphimba zilankhulo zonse **183 active ISO 639 Set 1 languages** (deprecated `sh` sichiphatikizidwa).

English (`en`) ndi canonical translation source. Japanese (`ja`) ndi reviewed translation ndipo imacopyidwa ku repository root ngati default `README.md` presentation. Root Japanese README **sagwiritsidwa ntchito** ngati translation source. Locale zina 181 ndi machine-translated kuchokera ku English.

## Zindikirani

- Notebook imayima transcription isanayambe ngati GPU palibe.
- Processing time imadalira kutalika kwa input, setting, ndi GPU yopatsidwa ndi Colab. Pa run yoyamba, NeMo ndi model ya pafupifupi 1.23 GB zimadownloadidwanso.
- Audio yayitali imaprocessidwa mu internal chunks, choncho recognition ingakhudzidwe pafupi ndi chunk boundaries.

## Canonical source ndi generation

Magwero a canonical omasuliridwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ndi synchronized canonical snapshot. Japanese imasungidwa ngati reviewed translation mu `locales/ja.json`, ndipo README snapshot yake imacopyidwa ku root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ndi yosiyana ndi ordinary CI. Ordinary users ndi CI safuna translation credentials.

## License

Notebook scaffolding ndi build/check scripts ndi MIT licensed. Third Intelligence model siyredistributed pano ndipo imayendetsedwa ndi **Apache-2.0**. Third-party dependencies zimasunga licenses zawo.
