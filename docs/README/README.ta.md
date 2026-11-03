# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** பயன்படுத்தி ஜப்பானிய ஒலி மற்றும் காணொலி கோப்புகளை எழுத்தாக்குவதற்கான Google Colab நோட்புக்.

[![Colab-ல் திறக்கவும்](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ta.ipynb)

## அம்சங்கள்

- **இலவசம்:** Google Colab-ன் இலவச GPU இயக்கச் சூழலில் இயங்குகிறது.
- **ஜப்பானிய ASR:** ஜப்பானிய பேச்சறிதலுக்கான சுமார் 0.6B அளவுருக்கள் கொண்ட [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) மாதிரியைப் பயன்படுத்துகிறது.
- **வேகம்:** எழுத்தாக்கத்தை விரைவாக செயலாக்கலாம்.
- **நிறுத்தற்குறிகள்:** மாதிரி மதிப்பிடப்பட்ட ஜப்பானிய நிறுத்தற்குறிகளை வெளியிடுகிறது.
- **நேரமுத்திரைகள் மற்றும் வசனவரி:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **நீண்ட கோப்பு செயலாக்கம்:** நீண்ட ஒலி மற்றும் காணொலி கோப்புகளையும் செயலாக்கலாம்.
- **Google Drive ஆதரவு:** கோப்புகளை நேரடியாகப் பதிவேற்றலாம் அல்லது Google Drive-இலிருந்து வாசிக்கலாம்; வெளியீட்டு ZIP-ஐ விருப்பப்படி Drive-இல் சேமிக்கலாம்.
- **பல வெளியீடுகள்:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest மற்றும் ZIP.

## பயன்படுத்துவது எப்படி

1. **1. Settings** பகுதியில் `INPUT_MODE`-ஐத் தேர்ந்தெடுத்து, தேவையானால் பிற அமைப்புகளைச் சரிசெய்யவும்.
2. **Runtime → Run all** என்பதைத் தேர்ந்தெடுக்கவும்.
3. `INPUT_MODE = "upload"` என இருந்தால், **2. File selection / Google Drive mount** பகுதியில் கோப்புகளைத் தேர்ந்தெடுக்கவும்.
4. செயலாக்கம் முடிந்ததும் வெளியீட்டு ZIP தானாகப் பதிவிறக்கப்படும்.

## நேரமுத்திரை முறைகள்

- `none`: நேரத் தகவல் இல்லை.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## நீண்ட கோப்புகள்

`CHUNK_SECONDS` நீண்ட கோப்புகளுக்குப் பயன்படுத்தப்படும் உள் chunk காலத்தை கட்டுப்படுத்துகிறது. பெரிய மதிப்புகள் எல்லைகளை குறைத்து அதிக சூழலைப் பாதுகாக்கும், ஆனால் ஒவ்வொரு inference-ஐயும் கனமாக்கி GPU நினைவகப் பயன்பாட்டை அதிகரிக்கலாம். சிறிய மதிப்புகள் ஒவ்வொரு inference-ஐயும் இலகுவாக்கும், ஆனால் அதிக எல்லைகளை உருவாக்குவதால் அவற்றைச் சுற்றியுள்ள அறிதலை பாதிக்கலாம். பெரும்பாலான சூழல்களில் இயல்புநிலை பரிந்துரைக்கப்படுகிறது.

## உள்ளூர்மயமாக்கப்பட்ட UI

ASR மாதிரி தானாகவே **ஜப்பானிய மொழிக்கே** உரியது. README மற்றும் Colab UI உள்ளூர்மயமாக்கல், பழைய `sh`-ஐத் தவிர்த்து, **183 செயலில் உள்ள ISO 639 Set 1 மொழிகள்** அனைத்தையும் உள்ளடக்குகிறது.

ஆங்கிலம் (`en`) மொழிபெயர்ப்புக்கான canonical மூலம். ஜப்பானியம் (`ja`) மதிப்பாய்வு செய்யப்பட்ட மொழிபெயர்ப்பு; repository root-இல் இயல்புநிலை `README.md` காட்சியாக நகலெடுக்கப்படுகிறது. root-இல் உள்ள ஜப்பானிய README மொழிபெயர்ப்பு மூலமாக **பயன்படுத்தப்படாது**. மற்ற 181 locale-கள் ஆங்கிலத்திலிருந்து இயந்திர மொழிபெயர்ப்பு செய்யப்படுகின்றன.

## குறிப்புகள்

- GPU கிடைக்காவிட்டால், எழுத்தாக்கம் தொடங்குவதற்கு முன் நோட்புக் நிற்கும்.
- செயலாக்க நேரம் உள்ளீட்டின் நீளம், அமைப்புகள் மற்றும் Colab ஒதுக்கும் GPU ஆகியவற்றைப் பொறுத்தது. முதல் இயக்கத்தில் NeMo மற்றும் சுமார் 1.23 GB மாதிரியும் பதிவிறக்கப்படும்.
- நீண்ட ஒலி உள் chunk-களில் செயலாக்கப்படுவதால், chunk எல்லைகளுக்கு அருகில் அறிதல் பாதிக்கப்படலாம்.

## Canonical மூலம் மற்றும் உருவாக்கம்

மொழிபெயர்க்கக்கூடிய canonical மூலங்கள்:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ஒத்திசைக்கப்பட்ட canonical snapshot ஆகும். ஜப்பானியம் `locales/ja.json`-இல் மதிப்பாய்வு செய்யப்பட்ட மொழிபெயர்ப்பாக பராமரிக்கப்படுகிறது; அதன் README snapshot root `README.md`-க்கு நகலெடுக்கப்படுகிறது.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

மொழிபெயர்ப்பு பராமரிப்பு சாதாரண CI-யிலிருந்து தனியே உள்ளது. சாதாரண பயனர்களுக்கும் CI-க்கும் மொழிபெயர்ப்பு credentials தேவையில்லை.

## உரிமம்

Notebook scaffolding மற்றும் build/check scripts MIT உரிமத்தில் உள்ளன. Third Intelligence மாதிரி இங்கு மறுவிநியோகம் செய்யப்படாது; அது **Apache-2.0** விதிமுறைகளுக்கு உட்பட்டது. மூன்றாம் தரப்பு சார்புகள் தங்களது சொந்த உரிமங்களைத் தக்கவைத்துக்கொள்கின்றன.
