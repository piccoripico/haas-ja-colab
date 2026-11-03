# Haas Japanese Colab

Google Colab notebook bee Nihon bizaad audio dóó video file bee hane’ áłts’íísí Third Intelligence **Haas-ja-v1.0** bee haz’ánígíí.

[![Colab-gi naashá](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_nv.ipynb)

## Bee ádáat’į́

- **T’áá doo béeso da:** Google Colab free GPU runtime bikáá’ dah naashá.
- **Nihon bizaad ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) bee haz’ánígíí, 0.6B parameter bee Nihon bizaad yáłti’ígíí áłtsé áł’ąąh ná’ádoolnííł, bee naalnish.
- **Áłts’áázh:** Transcription hólǫ́ǫ́góó áłts’áázh bee naalnish.
- **Naaltsoos bikáá’ dah naazhch’į́į́d:** Model Nihon bizaad punctuation ádaat’éego bee nidahałnííł.
- **Timestamps dóó subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **File háádáníłtso:** Audio dóó video file háádáníłtso áko t’áá ájiił’į́į́ł.
- **Google Drive:** File t’áá ánááshchį́į́h upload yiłkaah, doodago Google Drive bínaalkaah; output ZIP Drive-gi bee ájít’į́į́ł nizhónígo.
- **Output łahda neel’ą́ą́’:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, dóó ZIP.

## Haash yiníł’į́

1. **1. Settings** bii’ `INPUT_MODE` yíníłtaa, doodago settings łahda háida yíníł’į́į́ł.
2. **Runtime → Run all** yíníłtaa.
3. `INPUT_MODE = "upload"` ííłtaahgo, **2. File selection / Google Drive mount** bii’ file yíníłtaa.
4. Naalnish ádeiyááłgo output ZIP t’áá bídeeshłaa download.

## Timestamp mode

- `none`: doo time information hólǫ́ǫ da.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File háádáníłtso

`CHUNK_SECONDS` internal chunk háádáníłtso file bee naalnishígíí bee haz’ánígíí bee yáłta’. Value háádáníłtso boundaries yázhí áyiilaa dóó context łahda neel’ą́ą́’ bee ájít’į́, ndi inference t’ááłá’í bee naalnish łahda nit’į́ dóó GPU memory neel’ą́ą́’ bee naalnish. Value yázhí inference bee naalnish hazh’ó’ó nizhónígo, ndi boundaries neel’ą́ą́’ áyiilaa, áko recognition bee naalnish nahaz’ą́ą́ bee doo bee ájoodlą́ą́ł da. Default t’áá ałtso bá hazh’ó’ó nizhóní.

## UI bizaad bee ájít’į́

ASR model t’áá bee **Nihon bizaad t’ááłá’í bee naalnish**. README dóó Colab UI localization **183 active ISO 639 Set 1 languages** t’áá ałtso bee naalnish (`sh` doo bee naalnish da).

English (`en`) canonical translation source át’é. Nihon bizaad (`ja`) reviewed translation át’é dóó repository root-gi default `README.md` ádaat’éego bee naalnish. Root Japanese README **translation source doo át’é da**. Locale 181 łahda English bikáá’ machine-translate daaníłkaah.

## Háida bee ájoodlą́ą́ł

- GPU doo hólǫ́ǫ da notebook transcription áłtsé bee naalnish doo áł’į́į́ł da.
- Processing time input háádáníłtso, settings, dóó Colab GPU bee naalnishígíí bikáá’ daazlį́. Run áłtséedi NeMo dóó model 1.23 GB nahalingo download áyiilaa.
- Audio háádáníłtso internal chunks bee naalnish, áko chunk boundaries nahaz’ą́ą́ recognition doo t’áá íiyisíí bee ájoodlą́ą́ł da.

## Canonical source dóó generation

Bee áłts’íísí naaltsoos t’áá ajiłiił’į́į́łígíí:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot át’é. Nihon bizaad reviewed translation ádaat’éego `locales/ja.json` bii’ bee ájít’į́, dóó README snapshot root `README.md`-gi kopii áyiilaa.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI bikáá’ háida bee naalnish. Ordinary users dóó CI doo translation credentials bee haz’ą́ą́ da.

## License

Notebook scaffolding dóó build/check scripts MIT licensed da. Third Intelligence model doo kwe’é redistribute ádaat’éego bee naalnish da, **Apache-2.0** bee haz’ánígíí bee naalnish. Third-party dependencies t’áá bíla’ashdla’ii licenses bee ájít’į́.
