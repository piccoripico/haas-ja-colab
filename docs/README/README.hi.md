# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** के साथ जापानी ऑडियो और वीडियो का ट्रांसक्रिप्शन करने के लिए Google Colab नोटबुक।

[![Colab में खोलें](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_hi.ipynb)

## विशेषताएँ

- **निःशुल्क:** Google Colab के निःशुल्क GPU रनटाइम पर चलता है।
- **जापानी ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) का उपयोग करता है, जो जापानी वाक् पहचान के लिए लगभग 0.6 अरब पैरामीटर वाला मॉडल है।
- **तेज़:** ट्रांसक्रिप्शन को तेज़ी से संसाधित किया जा सकता है।
- **विराम-चिह्न:** मॉडल अनुमानित जापानी विराम-चिह्न आउटपुट करता है।
- **टाइमस्टैम्प और उपशीर्षक:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **लंबी फ़ाइलों का प्रसंस्करण:** लंबी ऑडियो और वीडियो फ़ाइलों को भी संसाधित किया जा सकता है।
- **Google Drive समर्थन:** फ़ाइलें सीधे अपलोड करें या Google Drive से पढ़ें; आउटपुट ZIP को वैकल्पिक रूप से Drive में सहेजा जा सकता है।
- **कई आउटपुट:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest और ZIP।

## उपयोग

1. **1. सेटिंग्स** में `INPUT_MODE` चुनें और आवश्यकता होने पर अन्य सेटिंग्स समायोजित करें।
2. **Runtime → Run all** चुनें।
3. `INPUT_MODE = "upload"` होने पर **2. फ़ाइल चयन / Google Drive माउंट** में फ़ाइलें चुनें।
4. प्रसंस्करण पूरा होने के बाद आउटपुट ZIP स्वतः डाउनलोड हो जाता है।

## टाइमस्टैम्प मोड

- `none`: कोई समय जानकारी नहीं।
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## डिकोडर

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## लंबी फ़ाइलें

`CHUNK_SECONDS` लंबी फ़ाइलों के लिए उपयोग की जाने वाली आंतरिक chunk अवधि नियंत्रित करता है। बड़े मान सीमाएँ कम करते हैं और अधिक संदर्भ बनाए रखते हैं, लेकिन प्रत्येक inference भारी होता है और अधिक GPU मेमोरी का उपयोग कर सकता है। छोटे मान प्रत्येक inference को हल्का करते हैं, लेकिन अधिक सीमाएँ बनाते हैं, जिससे उन बिंदुओं के आसपास पहचान प्रभावित हो सकती है। अधिकांश मामलों में डिफ़ॉल्ट मान अनुशंसित है।

## स्थानीयकृत UI

ASR मॉडल स्वयं **केवल जापानी** है। README और Colab UI स्थानीयकरण सभी **183 सक्रिय ISO 639 Set 1 भाषाओं** को कवर करता है (पुराना `sh` शामिल नहीं है)।

अंग्रेज़ी (`en`) canonical अनुवाद स्रोत है। जापानी (`ja`) समीक्षा किया हुआ अनुवाद है और डिफ़ॉल्ट `README.md` प्रस्तुति के रूप में repository root में कॉपी किया जाता है। root Japanese README को अनुवाद स्रोत के रूप में **उपयोग नहीं** किया जाता। अन्य 181 locale अंग्रेज़ी से मशीन-अनुवादित हैं।

## टिप्पणियाँ

- यदि GPU उपलब्ध नहीं है तो नोटबुक ट्रांसक्रिप्शन से पहले रुक जाती है।
- प्रसंस्करण समय इनपुट की लंबाई, सेटिंग्स और Colab द्वारा दिए गए GPU पर निर्भर करता है। पहली बार चलाने पर NeMo और लगभग 1.23 GB मॉडल भी डाउनलोड किए जाते हैं।
- लंबी ऑडियो को आंतरिक chunks में संसाधित किया जाता है, इसलिए chunk सीमाओं के आसपास पहचान प्रभावित हो सकती है।

## Canonical स्रोत और generation

Canonical अनुवाद योग्य स्रोत:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` समकालित canonical snapshot है। जापानी को `locales/ja.json` में समीक्षा किए हुए अनुवाद के रूप में रखा जाता है और उसका README snapshot root `README.md` में कॉपी किया जाता है।

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

अनुवाद रखरखाव सामान्य CI से अलग है। सामान्य उपयोगकर्ताओं और CI को अनुवाद credentials की आवश्यकता नहीं है।

## लाइसेंस

नोटबुक scaffolding और build/check scripts MIT लाइसेंस के अंतर्गत हैं। Third Intelligence मॉडल यहाँ पुनर्वितरित नहीं किया जाता और **Apache-2.0** के अधीन है। तीसरे पक्ष की dependencies अपने-अपने लाइसेंस बनाए रखती हैं।
