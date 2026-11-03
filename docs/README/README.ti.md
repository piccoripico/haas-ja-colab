# Haas Japanese Colab

ብ Third Intelligence **Haas-ja-v1.0** ጃፓንኛ audioን videoን ናብ ጽሑፍ ንምቕያር ዝጥቀም Google Colab notebook።

[![ኣብ Colab ክፈት](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ti.ipynb)

## ባህርያት

- **ነጻ:** ኣብ ናይ Google Colab ነጻ GPU runtime ይሰርሕ።
- **ጃፓንኛ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ይጥቀም፤ እዚ ንጃፓንኛ speech recognition ዝኸውን ኣስታት 0.6B-parameter model እዩ።
- **ቅልጡፍ:** Transcription ብቕልጡፍ process ክግበር ይኽእል።
- **ምልክታት ስርዓተ-ነጥቢ:** Model ዝገመቶ ጃፓንኛ punctuation የውጽእ።
- **Timestampን subtitleን:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ነዊሕ file processing:** ነዊሕ audioን video fileን እውን process ክግበር ይኽእል።
- **Google Drive support:** File ብቐጥታ upload ግበር ወይ ካብ Google Drive ኣንብብ፤ output ZIP እንተደሊኻ ኣብ Drive save ክግበር ይኽእል።
- **ብዙሕ output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ከምኡውን ZIP።

## ኣጠቓቕማ

1. ኣብ **1. Settings** `INPUT_MODE` ምረጽ እሞ እንተድለየ ካልእ setting ኣስተኻኽል።
2. **Runtime → Run all** ምረጽ።
3. `INPUT_MODE = "upload"` እንተኾይኑ ኣብ **2. File selection / Google Drive mount** file ምረጽ።
4. Processing ምስተዛዘመ output ZIP ብኣውቶማቲክ download ይግበር።

## Timestamp mode

- `none`: timing information የለን።
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ነዊሕ file

`CHUNK_SECONDS` ንነዊሕ file ዝጥቀመሉ internal chunk ንውሓት ይቆጻጸር። ዓበይቲ value boundary ይቕንሱ እሞ ዝያዳ context ይዕቅቡ፣ ግን ነፍሲ ወከፍ inference ዝኸበደ ኮይኑ GPU memory ክውስኽ ይኽእል። ንኣሽቱ value ነፍሲ ወከፍ inference የቕልሉ፣ ግን ዝያዳ boundary ይፈጥሩ እሞ ኣብ ከባቢኦም recognition ክጽልዉ ይኽእሉ። ኣብ መብዛሕትኡ ኩነታት default ይምከር።

## ዝተተርጎመ UI

ASR model ባዕሉ **Japanese-only** እዩ። READMEን Colab UI localizationን ንኹሎም **183 active ISO 639 Set 1 languages** ይሽፍን (deprecated `sh` ኣይካተትን)።

English (`en`) canonical translation source እዩ። Japanese (`ja`) reviewed translation እዩ እሞ ከም default `README.md` presentation ናብ repository root copy ይግበር። Root Japanese README ከም translation source **ኣይጥቀምን**። እቶም ካልኦት 181 locale ካብ English machine-translated እዮም።

## መዘኻኸሪ

- GPU እንተዘየሎ notebook ቅድሚ transcription ይቋረጽ።
- Processing time ኣብ input ንውሓት፣ setting፣ ከምኡውን ብ Colab ዝተመደበ GPU ይምርኮስ። ኣብ መጀመርታ run NeMoን እቲ ኣስታት 1.23 GB modelን እውን download ይግበሩ።
- ነዊሕ audio ብ internal chunk ይ process ግበር፣ ስለዚ recognition ኣብ ከባቢ chunk boundary ክጽሎ ይኽእል።

## Canonical sourceን generationን

Canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot እዩ። Japanese ኣብ `locales/ja.json` ከም reviewed translation ይዕቀብ፣ README snapshot ድማ ናብ root `README.md` copy ይግበር።

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ካብ ordinary CI ዝተፈለየ እዩ። Ordinary userን CIን translation credential ኣየድልዮምን።

## License

Notebook scaffoldingን build/check scriptን MIT licensed እዮም። Third Intelligence model ኣብዚ ዳግማይ ኣይዝርጋሕን እሞ ብ **Apache-2.0** ይመሓደር። Third-party dependency ናይ ገዛእ ርእሶም license ይዕቅቡ።
