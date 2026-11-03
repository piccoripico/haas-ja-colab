# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ବ୍ୟବହାର କରି ଜାପାନୀ ଅଡିଓ ଓ ଭିଡିଓକୁ ଲେଖାରେ ପରିବର୍ତ୍ତନ କରିବା ପାଇଁ Google Colab notebook।

[![Colab ରେ ଖୋଲନ୍ତୁ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_or.ipynb)

## ବୈଶିଷ୍ଟ୍ୟ

- **ମାଗଣା:** Google Colab ର ମାଗଣା GPU runtime ରେ ଚାଲେ।
- **ଜାପାନୀ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ବ୍ୟବହାର କରେ; ଏହା ଜାପାନୀ ଭାଷଣ ପରିଚୟ ପାଇଁ ପ୍ରାୟ 0.6B-parameter model।
- **ଦ୍ରୁତ:** Transcription ଶୀଘ୍ର ପ୍ରକ୍ରିୟାକରଣ କରିହେବ।
- **ବିରାମଚିହ୍ନ:** Model ଅନୁମାନିତ ଜାପାନୀ punctuation ଆଉଟପୁଟ କରେ।
- **Timestamp ଓ subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ଦୀର୍ଘ file ପ୍ରକ୍ରିୟାକରଣ:** ଦୀର୍ଘ audio ଓ video file ମଧ୍ୟ ପ୍ରକ୍ରିୟାକରଣ କରିହେବ।
- **Google Drive ସମର୍ଥନ:** File ସିଧା upload କରନ୍ତୁ କିମ୍ବା Google Drive ରୁ ପଢ଼ନ୍ତୁ; output ZIP ଇଚ୍ଛା କଲେ Drive ରେ ସଞ୍ଚୟ କରିହେବ।
- **ଏକାଧିକ output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ଏବଂ ZIP।

## ବ୍ୟବହାର

1. **1. Settings** ରେ `INPUT_MODE` ବାଛନ୍ତୁ ଏବଂ ଆବଶ୍ୟକ ହେଲେ ଅନ୍ୟ setting ବଦଳାନ୍ତୁ।
2. **Runtime → Run all** ବାଛନ୍ତୁ।
3. `INPUT_MODE = "upload"` ହେଲେ **2. File selection / Google Drive mount** ରେ file ବାଛନ୍ତୁ।
4. ପ୍ରକ୍ରିୟା ଶେଷ ହେଲେ output ZIP ସ୍ୱୟଂଚାଳିତ ଭାବେ download ହୁଏ।

## Timestamp mode

- `none`: କୌଣସି timing information ନାହିଁ।
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ଦୀର୍ଘ file

`CHUNK_SECONDS` ଦୀର୍ଘ file ପାଇଁ ବ୍ୟବହୃତ internal chunk ର ଅବଧି ନିୟନ୍ତ୍ରଣ କରେ। ବଡ଼ value boundary କମାଇ ଅଧିକ context ରଖେ, କିନ୍ତୁ ପ୍ରତ୍ୟେକ inference ଭାରୀ ହୁଏ ଏବଂ GPU memory ବ୍ୟବହାର ବଢ଼ିପାରେ। ଛୋଟ value ପ୍ରତ୍ୟେକ inference କୁ ହାଲୁକା କରେ, କିନ୍ତୁ ଅଧିକ boundary ତିଆରି କରେ, ଯାହା ସେହି ସ୍ଥାନଗୁଡ଼ିକ ଚାରିପାଖରେ recognition କୁ ପ୍ରଭାବିତ କରିପାରେ। ଅଧିକାଂଶ କ୍ଷେତ୍ରରେ default ସୁପାରିଶ କରାଯାଏ।

## ସ୍ଥାନୀୟୀକୃତ UI

ASR model ନିଜେ **Japanese-only**। README ଓ Colab UI localization ସମସ୍ତ **183 active ISO 639 Set 1 languages** କୁ ଆବର୍ତ୍ତ କରେ (deprecated `sh` ବାଦ)।

English (`en`) canonical translation source। Japanese (`ja`) reviewed translation ଏବଂ default `README.md` presentation ଭାବେ repository root କୁ copy କରାଯାଏ। Root Japanese README କୁ translation source ଭାବେ **ବ୍ୟବହାର କରାଯାଏ ନାହିଁ**। ଅନ୍ୟ 181 locale କୁ English ରୁ machine-translate କରାଯାଇଛି।

## ଟୀକା

- GPU ଉପଲବ୍ଧ ନଥିଲେ notebook transcription ପୂର୍ବରୁ ବନ୍ଦ ହୁଏ।
- Processing time input ଲମ୍ବ, setting, ଏବଂ Colab ଦ୍ୱାରା ଦିଆଯାଇଥିବା GPU ଉପରେ ନିର୍ଭର କରେ। ପ୍ରଥମ run ରେ NeMo ଏବଂ ପ୍ରାୟ 1.23 GB model ମଧ୍ୟ download ହୁଏ।
- ଦୀର୍ଘ audio internal chunk ରେ ପ୍ରକ୍ରିୟାକରଣ ହୁଏ, ସେଥିପାଇଁ chunk boundary ଚାରିପାଖରେ recognition ପ୍ରଭାବିତ ହୋଇପାରେ।

## Canonical source ଏବଂ generation

Canonical translatable source:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot। Japanese କୁ `locales/ja.json` ରେ reviewed translation ଭାବେ ରଖାଯାଏ, ଏବଂ ତାହାର README snapshot କୁ root `README.md` କୁ copy କରାଯାଏ।

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ସାଧାରଣ CI ଠାରୁ ଅଲଗା। ସାଧାରଣ user ଓ CI ପାଇଁ translation credential ଆବଶ୍ୟକ ନୁହେଁ।

## License

Notebook scaffolding ଏବଂ build/check script MIT license ଅଧୀନରେ। Third Intelligence model ଏଠାରେ ପୁନଃବିତରଣ କରାଯାଏ ନାହିଁ ଏବଂ **Apache-2.0** ଦ୍ୱାରା ନିୟନ୍ତ୍ରିତ। Third-party dependency ନିଜ ନିଜ license ରଖେ।
