# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** प्रयोग गरेर जापानी अडियो र भिडियो ट्रान्सक्राइब गर्ने Google Colab notebook.

[![Colab मा खोल्नुहोस्](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ne.ipynb)

## विशेषताहरू

- **निःशुल्क:** Google Colab को निःशुल्क GPU runtime मा चल्छ.
- **जापानी ASR:** जापानी वाणी पहिचानका लागि करिब 0.6B parameters भएको [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) प्रयोग गर्छ.
- **छिटो:** ट्रान्सक्रिप्शन छिटो process गर्न सकिन्छ.
- **विरामचिह्न:** मोडेलले अनुमानित जापानी विरामचिह्न output गर्छ.
- **टाइमस्ट्याम्प र उपशीर्षक:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **लामो फाइल process:** लामो audio र video फाइल पनि process गर्न सकिन्छ.
- **Google Drive समर्थन:** फाइल सीधै upload गर्नुहोस् वा Google Drive बाट पढ्नुहोस्; output ZIP वैकल्पिक रूपमा Drive मा save गर्न सकिन्छ.
- **धेरै output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, र ZIP.

## प्रयोग

1. **1. Settings** मा `INPUT_MODE` छान्नुहोस् र आवश्यक परे अरू settings मिलाउनुहोस्.
2. **Runtime → Run all** छान्नुहोस्.
3. `INPUT_MODE = "upload"` हुँदा **2. File selection / Google Drive mount** मा फाइल छान्नुहोस्.
4. Processing सकिएपछि output ZIP स्वतः download हुन्छ.

## Timestamp मोड

- `none`: कुनै timing जानकारी छैन.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## लामो फाइल

`CHUNK_SECONDS` ले लामो फाइलका लागि प्रयोग हुने internal chunk अवधि नियन्त्रण गर्छ. ठूलो value ले boundaries घटाएर बढी context राख्छ, तर हरेक inference भारी हुन्छ र बढी GPU memory चाहिन सक्छ. सानो value ले inference हल्का बनाउँछ तर बढी boundaries बनाउँछ, जसले ती ठाउँ वरिपरि recognition असर गर्न सक्छ. धेरै अवस्थामा default value सिफारिस गरिन्छ.

## स्थानीयकृत UI

ASR मोडेल आफैं **जापानी मात्र** हो. README र Colab UI localization ले सबै **183 active ISO 639 Set 1 languages** समेट्छ (deprecated `sh` बाहेक).

English (`en`) canonical translation source हो. Japanese (`ja`) reviewed translation हो र repository root मा default `README.md` presentation का रूपमा copy हुन्छ. Root Japanese README **translation source का रूपमा प्रयोग हुँदैन**. बाँकी 181 locales English बाट machine-translated छन्.

## नोट

- GPU उपलब्ध नभए notebook ट्रान्सक्रिप्शन अघि रोकिन्छ.
- Processing time input length, settings, र Colab ले दिएको GPU मा निर्भर हुन्छ. पहिलो run मा NeMo र करिब 1.23 GB मोडेल पनि download हुन्छ.
- लामो audio internal chunks मा process हुन्छ, त्यसैले chunk boundaries वरिपरि recognition असर पर्न सक्छ.

## Canonical source र generation

अनुवाद गर्न मिल्ने canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot हो. Japanese `locales/ja.json` मा reviewed translation का रूपमा राखिन्छ र यसको README snapshot root `README.md` मा copy हुन्छ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance सामान्य CI बाट अलग छ. सामान्य users र CI लाई translation credentials आवश्यक पर्दैन.

## License

Notebook scaffolding र build/check scripts MIT licensed छन्. Third Intelligence मोडेल यहाँ redistribute गरिँदैन र **Apache-2.0** अन्तर्गत छ. Third-party dependencies ले आफ्नै licenses राख्छन्.
