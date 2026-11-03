# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** སྤྱད་ནས་ཉི་ཧོང་སྐད་ཀྱི་སྒྲ་དང་བརྙན་ཡིག་ཆ་རྣམས་ཡི་གེར་ཕབ་པའི་ Google Colab ནོཊ་བུག་ཅིག་ཡིན།

[![Colab ནང་ཁ་ཕྱེ།](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_bo.ipynb)

## ཁྱད་ཆོས།

- **རིན་མེད།:** Google Colab གི་རིན་མེད་ GPU runtime ཐོག་འགྲོ།
- **ཉི་ཧོང་སྐད་ཀྱི་ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) སྤྱད་པ་དང་། འདི་ནི་ཉི་ཧོང་སྐད་ངག་ངོས་འཛིན་ལ་སྤྱོད་པའི་ parameter ཧ་ལམ་ 0.6B ཡོད་པའི་མོ་ཌེལ་ཞིག་ཡིན།
- **མགྱོགས་པོ།:** སྒྲ་ཡིག་ཕབ་ཀྱི་ལས་སྣོན་མགྱོགས་པོར་བྱེད་ཐུབ།
- **ཚེག་རྟགས།:** མོ་ཌེལ་གྱིས་ཚོད་དཔག་བྱས་པའི་ཉི་ཧོང་ཡིག་གི་ཚེག་རྟགས་ཕྱིར་འདོན།
- **དུས་རྟགས་དང་ཡིག་བརྙན།:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ཡིག་ཆ་རིང་པོའི་ལས་སྣོན།:** སྒྲ་དང་བརྙན་ཡིག་ཆ་རིང་པོ་ཡང་ལས་སྣོན་བྱེད་ཐུབ།
- **Google Drive རྒྱབ་སྐྱོར།:** ཡིག་ཆ་ཐད་ཀར་ཡར་འཇུག་བྱེད་པའམ་ Google Drive ནས་ཀློག་ཐུབ། ཐོན་འབྲས་ ZIP ཀྱང་འདོད་མོས་ལྟར་ Drive ནང་ཉར་ཐུབ།
- **ཐོན་འབྲས་སྣ་ཚོགས།:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, དང་ ZIP།

## སྤྱོད་ཚུལ།

1. **1. Settings** ནང་ `INPUT_MODE` འདེམས་ཏེ་དགོས་ན་སྒྲིག་འགོད་གཞན་བསྒྱུར།
2. **Runtime → Run all** འདེམས།
3. `INPUT_MODE = "upload"` ཡིན་ན་ **2. File selection / Google Drive mount** ནང་ཡིག་ཆ་འདེམས།
4. ལས་སྣོན་ཚར་རྗེས་ཐོན་འབྲས་ ZIP རང་འགུལ་གྱིས་ཕབ་ལེན་བྱེད།

## དུས་རྟགས་རྣམ་པ།

- `none`: དུས་ཚོད་ཀྱི་གནས་ཚུལ་མེད།
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ཡིག་ཆ་རིང་པོ།

`CHUNK_SECONDS` ཡིས་ཡིག་ཆ་རིང་པོ་ལ་སྤྱོད་པའི་ནང་ཁུལ་ chunk གི་དུས་ཚོད་སྟངས་འཛིན་བྱེད། གྲངས་ཐང་ཆེ་ན་ boundary ཉུང་ཞིང་ context མང་བ་ཉར་ཐུབ་ཀྱང་ inference རེ་རེ་ལྗིད་པ་དང་ GPU memory མང་བ་སྤྱོད་སྲིད། གྲངས་ཐང་ཆུང་ན་ inference ཡང་བ་ཡིན་ཀྱང་ boundary མང་བ་བཟོས་པས་དེ་དག་གི་ཉེ་འཁོར་གྱི་ངོས་འཛིན་ལ་ཤུགས་རྐྱེན་འབྱུང་སྲིད། སྤྱིར་བཏང་སྔོན་སྒྲིག་འོས་སྦྱོར་བྱེད།

## ས་གནས་སྐད་ཡིག་གི་ UI

ASR མོ་ཌེལ་རང་ཉིད་ནི་ **ཉི་ཧོང་སྐད་ཁོ་ན** ཡིན། README དང་ Colab UI ས་གནས་སྐད་ཡིག་གིས་ **183 active ISO 639 Set 1 languages** ཚང་མ་ཁྱབ་པ་ཡིན (`sh` རྙིང་པ་མ་བརྩིས)།

English (`en`) ནི་ཚད་ལྡན་གྱི་སྐད་བསྒྱུར་འབྱུང་ཁུངས་ཡིན། ཉི་ཧོང་སྐད་ (`ja`) ནི་ཞིབ་བཤེར་བྱས་པའི་སྐད་བསྒྱུར་ཡིན་ཞིང་ repository root ལ་སྔོན་སྒྲིག་ `README.md` མངོན་སྟངས་སུ་འདྲ་བཤུས་བྱེད། Root གི་ཉི་ཧོང་ README ནི་སྐད་བསྒྱུར་འབྱུང་ཁུངས་ **མིན**། ས་གནས་སྐད་ཡིག་གཞན་ 181 ནི་ English ནས་འཕྲུལ་ཆས་ཀྱིས་སྐད་བསྒྱུར་བྱས།

## ཟིན་ཐོ།

- GPU མེད་ན་ནོཊ་བུག་གིས་སྒྲ་ཡིག་ཕབ་མ་འགོ་འཛུགས་གོང་མཚམས་འཇོག།
- ལས་སྣོན་གྱི་དུས་ཚོད་ནི་ནང་འཇུག་གི་རིང་ཚད། སྒྲིག་འགོད། དང་ Colab གིས་བགོས་པའི་ GPU ལ་རག་ལས། ཐོག་མའི་ཐེངས་སུ་ NeMo དང་ཧ་ལམ་ 1.23 GB ཡོད་པའི་མོ་ཌེལ་ཡང་ཕབ་ལེན་བྱེད།
- སྒྲ་རིང་པོ་ནང་ཁུལ་ chunk ནས་ལས་སྣོན་བྱེད་པས་ chunk boundary ཉེ་འཁོར་དུ་ངོས་འཛིན་ལ་ཤུགས་རྐྱེན་འབྱུང་སྲིད།

## ཚད་ལྡན་འབྱུང་ཁུངས་དང་སྐྱེད་སྐྲུན།

སྐད་བསྒྱུར་བྱ་ཆོག་པའི་ཚད་ལྡན་འབྱུང་ཁུངས།

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ནི་མཉམ་འགྲོས་བྱས་པའི་ཚད་ལྡན་བརྙན་འཛིན་ཡིན། ཉི་ཧོང་སྐད་ནི་ `locales/ja.json` ནང་ཞིབ་བཤེར་བྱས་པའི་སྐད་བསྒྱུར་དུ་ཉར་ཞིང་། དེའི་ README བརྙན་འཛིན་ root `README.md` ལ་འདྲ་བཤུས་བྱེད།

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

སྐད་བསྒྱུར་བདག་སྐྱོང་ནི་རྒྱུན་ལྡན་ CI ལས་ལོགས་སུ་ཡོད། རྒྱུན་ལྡན་སྤྱོད་མཁན་དང་ CI ལ་སྐད་བསྒྱུར་གསང་ཡིག་མི་དགོས།

## ཆོག་མཆན།

Notebook scaffolding དང་ build/check scripts ནི་ MIT ཆོག་མཆན་ཅན་ཡིན། Third Intelligence མོ་ཌེལ་འདི་འདིར་བསྐྱར་འགྲེམས་མི་བྱེད་ཅིང་ **Apache-2.0** ཡིས་སྟངས་འཛིན་བྱེད། ཕྱོགས་གསུམ་པའི་བརྟེན་ཆས་རྣམས་ཀྱིས་རང་རང་གི་ཆོག་མཆན་ཉར།
