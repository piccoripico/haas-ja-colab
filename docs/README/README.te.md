# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** తో జపనీస్ ఆడియో మరియు వీడియో ఫైళ్లను ట్రాన్స్‌క్రైబ్ చేయడానికి Google Colab నోట్‌బుక్.

[![Colabలో తెరవండి](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_te.ipynb)

## లక్షణాలు

- **ఉచితం:** Google Colab ఉచిత GPU runtimeలో నడుస్తుంది.
- **జపనీస్ ASR:** జపనీస్ speech recognition కోసం సుమారు 0.6B parameters ఉన్న [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) మోడల్‌ను ఉపయోగిస్తుంది.
- **వేగంగా:** ట్రాన్స్‌క్రిప్షన్‌ను త్వరగా ప్రాసెస్ చేయవచ్చు.
- **విరామ చిహ్నాలు:** మోడల్ అంచనా వేసిన జపనీస్ punctuationను అవుట్‌పుట్ చేస్తుంది.
- **Timestamps మరియు subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **పొడవైన ఫైళ్ల ప్రాసెసింగ్:** పొడవైన ఆడియో మరియు వీడియో ఫైళ్లను కూడా ప్రాసెస్ చేయవచ్చు.
- **Google Drive support:** ఫైళ్లను నేరుగా upload చేయండి లేదా Google Drive నుండి చదవండి; output ZIPని ఐచ్చికంగా Driveలో save చేయవచ్చు.
- **అనేక outputs:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, మరియు ZIP.

## వినియోగం

1. **1. Settings** లో `INPUT_MODE` ఎంచుకుని, అవసరమైతే ఇతర settings మార్చండి.
2. **Runtime → Run all** ఎంచుకోండి.
3. `INPUT_MODE = "upload"` అయితే, **2. File selection / Google Drive mount** లో files ఎంచుకోండి.
4. Processing పూర్తయ్యాక output ZIP స్వయంచాలకంగా download అవుతుంది.

## Timestamp modes

- `none`: timing information ఉండదు.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## పొడవైన ఫైళ్లు

`CHUNK_SECONDS` పొడవైన files కోసం ఉపయోగించే internal chunk durationను నియంత్రిస్తుంది. పెద్ద values boundariesను తగ్గించి ఎక్కువ contextను కాపాడతాయి, కానీ ప్రతి inferenceను భారంగా చేసి GPU memory usageను పెంచవచ్చు. చిన్న values ప్రతి inferenceను తేలిక చేస్తాయి, కానీ ఎక్కువ boundariesను సృష్టించి వాటి దగ్గర recognitionపై ప్రభావం చూపవచ్చు. చాలా సందర్భాల్లో default సిఫార్సు చేయబడుతుంది.

## స్థానీకరించిన UI

ASR model స్వయంగా **జపనీస్‌కే పరిమితం**. README మరియు Colab UI localization, deprecated `sh` మినహా, అన్ని **183 active ISO 639 Set 1 languages**ను కవర్ చేస్తుంది.

English (`en`) canonical translation source. Japanese (`ja`) reviewed translation మరియు repository rootకు default `README.md` presentationగా copy చేయబడుతుంది. Root Japanese READMEని translation sourceగా **ఉపయోగించరు**. మిగతా 181 locales English నుంచి machine-translated అవుతాయి.

## గమనికలు

- GPU అందుబాటులో లేకపోతే, transcriptionకు ముందు notebook ఆగిపోతుంది.
- Processing time input length, settings, మరియు Colab కేటాయించిన GPUపై ఆధారపడి ఉంటుంది. మొదటి runలో NeMo మరియు సుమారు 1.23 GB model కూడా download అవుతాయి.
- Long audio internal chunksలో process అవుతుంది, కాబట్టి chunk boundaries దగ్గర recognition ప్రభావితం కావచ్చు.

## Canonical source మరియు generation

అనువదించగల ప్రామాణిక మూలాలు:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot. Japanese `locales/ja.json`లో reviewed translationగా నిర్వహించబడుతుంది, మరియు దాని README snapshot root `README.md`కు copy చేయబడుతుంది.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance సాధారణ CI నుండి వేరు. సాధారణ users మరియు CIకి translation credentials అవసరం లేదు.

## License

Notebook scaffolding మరియు build/check scripts MIT licensed. Third Intelligence model ఇక్కడ redistribute చేయబడదు మరియు **Apache-2.0**కి లోబడి ఉంటుంది. Third-party dependencies తమ స్వంత licensesను కొనసాగిస్తాయి.
