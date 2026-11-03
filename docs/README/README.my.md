# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ဖြင့် ဂျပန် audio နှင့် video များကို စာသားပြောင်းရန် Google Colab notebook.

[![Colab တွင်ဖွင့်ရန်](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_my.ipynb)

## အင်္ဂါရပ်များ

- **အခမဲ့:** Google Colab ၏ အခမဲ့ GPU runtime တွင် လည်ပတ်သည်.
- **ဂျပန် ASR:** ဂျပန်စကားသံ အသိအမှတ်ပြုရန် parameter 0.6B ခန့်ရှိသော [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) model ကို အသုံးပြုသည်.
- **မြန်ဆန်:** Transcription ကို မြန်မြန်ဆန်ဆန် process လုပ်နိုင်သည်.
- **ပုဒ်ဖြတ်ပုဒ်ရပ်:** Model သည် ခန့်မှန်းထားသော ဂျပန် punctuation ကို output ထုတ်သည်.
- **Timestamps နှင့် subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ဖိုင်ရှည် processing:** Audio နှင့် video ဖိုင်ရှည်များကိုလည်း process လုပ်နိုင်သည်.
- **Google Drive ပံ့ပိုးမှု:** Files ကို တိုက်ရိုက် upload လုပ်နိုင်သလို Google Drive မှ ဖတ်နိုင်သည်; output ZIP ကို ရွေးချယ်၍ Drive တွင် save လုပ်နိုင်သည်.
- **Output မျိုးစုံ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## အသုံးပြုနည်း

1. **1. Settings** တွင် `INPUT_MODE` ကို ရွေးပြီး လိုအပ်လျှင် အခြား settings ကို ချိန်ညှိပါ.
2. **Runtime → Run all** ကို ရွေးပါ.
3. `INPUT_MODE = "upload"` ဆိုလျှင် **2. File selection / Google Drive mount** တွင် files ကို ရွေးပါ.
4. Processing ပြီးသောအခါ output ZIP ကို အလိုအလျောက် download လုပ်သည်.

## Timestamp modes

- `none`: အချိန်အချက်အလက် မရှိ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ဖိုင်ရှည်များ

`CHUNK_SECONDS` သည် ဖိုင်ရှည်များအတွက် internal chunk အရှည်ကို ထိန်းချုပ်သည်. Value ကြီးလျှင် boundaries လျော့ပြီး context ပိုထိန်းနိုင်သော်လည်း inference တစ်ကြိမ်ချင်း ပိုလေးပြီး GPU memory ပိုသုံးနိုင်သည်. Value သေးလျှင် inference ပေါ့သော်လည်း boundaries ပိုများ၍ အနီးဝန်းကျင် recognition ကို ထိခိုက်နိုင်သည်. အများအားဖြင့် default value ကို အကြံပြုသည်.

## ဒေသသုံးဘာသာပြန်ထားသော UI

ASR model ကိုယ်တိုင်သည် **ဂျပန်ဘာသာသာ** ဖြစ်သည်. README နှင့် Colab UI localization သည် **183 active ISO 639 Set 1 languages** အားလုံးကို ဖုံးလွှမ်းသည် (deprecated `sh` မပါ).

English (`en`) သည် canonical translation source ဖြစ်သည်. Japanese (`ja`) သည် reviewed translation ဖြစ်ပြီး repository root တွင် default `README.md` presentation အဖြစ် copy လုပ်သည်. Root Japanese README ကို **translation source အဖြစ် မသုံးပါ**. ကျန် 181 locales ကို English မှ machine translation လုပ်သည်.

## မှတ်ချက်များ

- GPU မရှိပါက notebook သည် transcription မစခင် ရပ်သည်.
- Processing time သည် input length, settings, Colab မှ ပေးသော GPU ပေါ်မူတည်သည်. ပထမ run တွင် NeMo နှင့် 1.23 GB ခန့် model ကိုလည်း download လုပ်သည်.
- Audio ရှည်ကို internal chunks များဖြင့် process လုပ်သောကြောင့် chunk boundaries အနီး recognition ထိခိုက်နိုင်သည်.

## Canonical source နှင့် generation

ဘာသာပြန်နိုင်သော canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` သည် synchronized canonical snapshot ဖြစ်သည်. Japanese ကို `locales/ja.json` တွင် reviewed translation အဖြစ် ထိန်းသိမ်းပြီး ၎င်း၏ README snapshot ကို root `README.md` သို့ copy လုပ်သည်.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance သည် ပုံမှန် CI နှင့် သီးခြားဖြစ်သည်. ပုံမှန် users နှင့် CI သည် translation credentials မလိုအပ်.

## License

Notebook scaffolding နှင့် build/check scripts သည် MIT licensed ဖြစ်သည်. Third Intelligence model ကို ဤနေရာတွင် redistribute မလုပ်ဘဲ **Apache-2.0** အောက်တွင် ရှိသည်. Third-party dependencies များသည် မိမိတို့ licenses ကို ထိန်းထားသည်.
