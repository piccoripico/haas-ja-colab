# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** वापरून जपानी ऑडिओ आणि व्हिडिओचे लिप्यंतरण करण्यासाठी Google Colab notebook.

[![Colab मध्ये उघडा](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_mr.ipynb)

## वैशिष्ट्ये

- **मोफत:** Google Colab च्या मोफत GPU runtime वर चालते.
- **जपानी ASR:** जपानी वाणी ओळखण्यासाठी सुमारे 0.6B पॅरामीटर्स असलेले [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) मॉडेल वापरते.
- **वेगवान:** लिप्यंतरण जलद प्रक्रिया करता येते.
- **विरामचिन्हे:** मॉडेल अंदाजित जपानी विरामचिन्हे देते.
- **टाइमस्टॅम्प आणि उपशीर्षके:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **लांब फाइल प्रक्रिया:** लांब ऑडिओ आणि व्हिडिओ फाइल्सही प्रक्रिया करता येतात.
- **Google Drive समर्थन:** फाइल्स थेट अपलोड करा किंवा Google Drive मधून वाचा; output ZIP ऐच्छिकरित्या Drive मध्ये जतन करता येते.
- **अनेक आउटपुट:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, आणि ZIP.

## वापर

1. **1. सेटिंग्ज** मध्ये `INPUT_MODE` निवडा आणि आवश्यक असल्यास इतर सेटिंग्ज बदला.
2. **Runtime → Run all** निवडा.
3. `INPUT_MODE = "upload"` असल्यास **2. फाइल निवड / Google Drive mount** मध्ये फाइल्स निवडा.
4. प्रक्रिया पूर्ण झाल्यानंतर output ZIP आपोआप डाउनलोड होते.

## टाइमस्टॅम्प मोड

- `none`: कोणतीही वेळ माहिती नाही.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## डिकोडर

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## लांब फाइल्स

`CHUNK_SECONDS` लांब फाइल्ससाठी वापरल्या जाणाऱ्या internal chunk कालावधीचे नियंत्रण करते. मोठी मूल्ये boundaries कमी करून अधिक context ठेवतात, पण प्रत्येक inference जड होते आणि अधिक GPU memory वापरू शकते. छोटी मूल्ये प्रत्येक inference हलकी करतात पण अधिक boundaries तयार करतात, ज्यामुळे त्या ठिकाणांभोवती recognition प्रभावित होऊ शकते. बहुतेक वेळा default मूल्य सुचवले जाते.

## स्थानिकीकरण केलेला UI

ASR मॉडेल स्वतः **फक्त जपानी** आहे. README आणि Colab UI चे स्थानिकीकरण सर्व **183 सक्रिय ISO 639 Set 1 भाषा** व्यापते (deprecated `sh` वगळून).

इंग्रजी (`en`) हा canonical translation source आहे. जपानी (`ja`) हे reviewed translation आहे आणि repository root मध्ये default `README.md` म्हणून कॉपी केले जाते. Root जपानी README **translation source म्हणून वापरले जात नाही**. उर्वरित 181 locales इंग्रजीवरून machine-translated आहेत.

## नोंदी

- GPU उपलब्ध नसल्यास notebook लिप्यंतरणापूर्वी थांबते.
- प्रक्रियेचा वेळ input length, settings आणि Colab ने दिलेल्या GPU वर अवलंबून असतो. पहिल्या run मध्ये NeMo आणि सुमारे 1.23 GB मॉडेलही डाउनलोड होते.
- लांब ऑडिओ internal chunks मध्ये प्रक्रिया होतो, त्यामुळे chunk boundaries जवळ recognition प्रभावित होऊ शकते.

## Canonical source आणि generation

भाषांतरयोग्य canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` हा synchronized canonical snapshot आहे. जपानी `locales/ja.json` मध्ये reviewed translation म्हणून राखले जाते आणि त्याचा README snapshot root `README.md` मध्ये कॉपी होतो.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance सामान्य CI पासून वेगळे आहे. सामान्य वापरकर्ते आणि CI ला translation credentials आवश्यक नाहीत.

## परवाना

Notebook scaffolding आणि build/check scripts MIT परवान्याखाली आहेत. Third Intelligence मॉडेल येथे redistribute केले जात नाही आणि **Apache-2.0** अंतर्गत आहे. Third-party dependencies त्यांचे स्वतःचे परवाने राखतात.
