# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** इत्यस्य साहाय्येन जापानी-श्रव्य-दृश्य-सञ्चिकानां लिप्यन्तरणार्थं Google Colab-पुस्तिका।

[![Colab मध्ये उद्घाटयतु](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sa.ipynb)

## वैशिष्ट्यानि

- **निःशुल्कम्:** Google Colab इत्यस्य निःशुल्क-GPU-runtime मध्ये चलति।
- **जापानी-ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) इति, प्रायः 0.6B-parameter-युक्तं जापानी-वाक्-परिचय-मॉडलं, उपयुज्यते।
- **शीघ्रम्:** लिप्यन्तरणं शीघ्रं संसाधयितुं शक्यते।
- **विरामचिह्नानि:** मॉडलं अनुमानितानि जापानी-विरामचिह्नानि निष्पादयति।
- **कालमुद्राः उपशीर्षकाणि च:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **दीर्घ-सञ्चिका-संसाधनम्:** दीर्घाः श्रव्य-दृश्य-सञ्चिकाः अपि संसाधयितुं शक्यन्ते।
- **Google Drive समर्थनम्:** सञ्चिकाः साक्षात् आरोपयतु अथवा Google Drive तः पठतु; फल-ZIP इच्छानुसारं Drive मध्ये रक्षितुं शक्यते।
- **अनेकानि फलरूपाणि:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP च।

## उपयोगविधिः

1. **1. Settings** मध्ये `INPUT_MODE` चिनोतु तथा आवश्यकतानुसारम् अन्याः settings परिवर्तयतु।
2. **Runtime → Run all** चिनोतु।
3. `INPUT_MODE = "upload"` सति, **2. File selection / Google Drive mount** मध्ये सञ्चिकाः चिनोतु।
4. संसाधनानन्तरं फल-ZIP स्वयमेव अवरोप्यते।

## कालमुद्रा-विधयः

- `none`: किमपि कालसूचना नास्ति।
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## दीर्घाः सञ्चिकाः

`CHUNK_SECONDS` दीर्घ-सञ्चिकासु प्रयुक्तस्य आन्तरिक-chunk-स्य कालावधिं नियन्त्रयति। बृहत्तराः मानाः सीमाः न्यूनयन्ति तथा अधिकं context रक्षन्ति, किन्तु प्रत्येकं inference गुरुतरं भवति, अधिकं GPU memory च अपेक्षितुं शक्नोति। लघुतराः मानाः प्रत्येकं inference लघु कुर्वन्ति, किन्तु अधिकाः सीमाः जनयन्ति; तासां समीपे recognition प्रभावितुं शक्नोति। अधिकेषु प्रसङ्गेषु default अनुशस्यते।

## स्थानीयकृत-UI

ASR-मॉडलं स्वयम् **केवलं जापानी-भाषायै** अस्ति। README तथा Colab UI इत्ययोः स्थानीयकरणं सर्वाः **183 सक्रियाः ISO 639 Set 1 भाषाः** आच्छादयति (पुरातनं `sh` वर्जितम्)।

आङ्ग्लभाषा (`en`) canonical translation source अस्ति। जापानी (`ja`) समीक्षित-अनुवादः अस्ति तथा default `README.md`-प्रस्तुतिरूपेण repository-मूले प्रतिलिप्यते। मूलस्थ-जापानी README **अनुवादस्रोतः न भवति**। अन्याः 181 locales आङ्ग्लभाषातः यन्त्रेण अनूद्यन्ते।

## टिप्पण्यः

- GPU अनुपलब्धे notebook लिप्यन्तरणात् पूर्वं स्थगयति।
- संसाधनकालः input-दीर्घता, settings, Colab-दत्त-GPU च इत्येतेषु निर्भरति। प्रथम-run मध्ये NeMo तथा प्रायः 1.23 GB-मॉडलं अपि अवरोप्यते।
- दीर्घ-श्रव्यं आन्तरिक-chunks मध्ये संसाध्यते, अतः chunk-सीमासु recognition प्रभावितुं शक्नोति।

## Canonical स्रोतः निर्माणं च

अनुवादयोग्याः canonical स्रोतांसि:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` समन्वितः canonical snapshot अस्ति। जापानी समीक्षित-अनुवादरूपेण `locales/ja.json` मध्ये रक्ष्यते, तस्य README snapshot च मूलस्थ `README.md` मध्ये प्रतिलिप्यते।

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

अनुवाद-परिपालनं सामान्य-CI तः पृथक् अस्ति। सामान्य-उपयोक्तारः CI च translation credentials न अपेक्षन्ते।

## अनुज्ञापत्रम्

Notebook scaffolding तथा build/check scripts MIT-अनुज्ञप्ताः। Third Intelligence-मॉडलं अत्र पुनर्वितरितं न भवति तथा **Apache-2.0** अधीनम् अस्ति। Third-party dependencies स्वस्व-अनुज्ञापत्राणि धारयन्ति।
