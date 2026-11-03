# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ལག་ལེན་འཐབ་སྟེ་ ཇ་པཱན་གྱི་སྒྲ་དང་གློག་བརྙན་ཡིག་སྣོད་ཚུ་ཡིག་ཐོག་ལུ་ཕབ་ནིའི་ Google Colab ནོཊ་བུག་ཅིག་ཨིན།

[![Colab ནང་ཁ་ཕྱེ།](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_dz.ipynb)

## ཁྱད་ཆོས།

- **རིན་མེད།:** Google Colab གི་རིན་མེད་ GPU runtime གུ་གཡོག་བཀོལ་ཚུགས།
- **ཇ་པཱན་སྐད་ཀྱི་ ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ལག་ལེན་འཐབ་ཨིན། འདི་ཇ་པཱན་གྱི་ཁ་སླབ་ངོས་འཛིན་འབད་ནིའི་ parameter ཧ་ལམ་ 0.6B ཡོད་པའི་མོ་ཌེལ་ཅིག་ཨིན།
- **མགྱོགས་པ།:** སྒྲ་ཡིག་ཐོག་ཕབ་ནིའི་ལཱ་མགྱོགས་པར་འབད་ཚུགས།
- **ཚེག་རྟགས།:** མོ་ཌེལ་གྱིས་ཚོད་དཔག་འབད་མི་ཇ་པཱན་ཡིག་གི་ཚེག་རྟགས་བཏོན་བྱིནམ་ཨིན།
- **དུས་རྟགས་དང་ཡིག་བརྙན།:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ཡིག་སྣོད་རིངམོའི་ལས་སྣོན།:** སྒྲ་དང་གློག་བརྙན་ཡིག་སྣོད་རིངམོ་ཚུ་ཡང་ལས་སྣོན་འབད་ཚུགས།
- **Google Drive རྒྱབ་སྐྱོར།:** ཡིག་སྣོད་ཐད་ཀར་ཡར་བཙུགས་ནི་ཡང་ན་ Google Drive ནང་ལས་ལྷག་ནི་འབད་ཚུགས། ཐོན་འབྲས་ ZIP ཡང་གདམ་ཁ་དང་འཁྲིལ་ Drive ནང་སྲུང་བཞག་འབད་ཚུགས།
- **ཐོན་འབྲས་སྣ་ཚོགས།:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, དང་ ZIP།

## ལག་ལེན་འཐབ་ཐངས།

1. **1. Settings** ནང་ `INPUT_MODE` གདམ་ཁ་རྐྱབ་སྟེ་ དགོས་མཁོ་ཡོད་པ་ཅིན་སྒྲིག་སྟངས་གཞན་ཚུ་སོར།
2. **Runtime → Run all** གདམ་ཁ་རྐྱབ།
3. `INPUT_MODE = "upload"` ཨིན་པ་ཅིན་ **2. File selection / Google Drive mount** ནང་ཡིག་སྣོད་གདམ་ཁ་རྐྱབ།
4. ལས་སྣོན་མཇུག་བསྡུ་ཞིནམ་ལས་ ཐོན་འབྲས་ ZIP རང་བཞིན་གྱིས་ཕབ་ལེན་འབདཝ་ཨིན།

## དུས་རྟགས་ཀྱི་རྣམ་པ།

- `none`: དུས་ཚོད་གནས་ཚུལ་མེད།
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ཡིག་སྣོད་རིངམོ།

`CHUNK_SECONDS` གིས་ཡིག་སྣོད་རིངམོ་ཚུ་ལུ་ལག་ལེན་འཐབ་པའི་ནང་འཁོད་ chunk གི་དུས་ཡུན་ཚད་འཛིན་འབདཝ་ཨིན། གྲངས་ཐང་སྦོམ་སྦེ་བཞག་པ་ཅིན་ boundary ཉུང་སུ་དང་ context མང་སུ་བཞག་ཚུགས་རུང་ inference རེ་རེ་ལྗིད་ཆེ་སུ་དང་ GPU memory མང་སུ་སྤྱོད་སྲིད། གྲངས་ཐང་ཆུང་ཀུ་གིས་ inference ཡང་སུ་བཟོ་རུང་ boundary མང་སུ་བཟོ་བས་ ས་གནས་དེ་ཚུའི་ཉེ་འདབས་ཀྱི་ངོས་འཛིན་ལུ་ཤུགས་རྐྱེན་འབྱུང་སྲིད། སྤྱིར་བཏང་ལུ་སྔོན་སྒྲིག་གྲངས་ཐང་འདི་འོས་འབབ་ཡོད།

## ས་གནས་སྐད་ཡིག་གི་ UI

ASR མོ་ཌེལ་རང་འདི་ **ཇ་པཱན་སྐད་རྐྱངམ་ཅིག** ཨིན། README དང་ Colab UI གི་ས་གནས་སྐད་ཡིག་འདི་ **183 active ISO 639 Set 1 languages** ག་ར་ལུ་ཁྱབ་ཨིན (`sh` རྙིངམ་འདི་ཕུད་དེ)།

English (`en`) འདི་ཚད་ལྡན་གྱི་སྐད་བསྒྱུར་འབྱུང་ཁུངས་ཨིན། ཇ་པཱན་སྐད་ (`ja`) འདི་ཞིབ་བཤེར་འབད་ཚར་བའི་སྐད་བསྒྱུར་ཅིག་ཨིན་ཏེ་ repository root ནང་གི་སྔོན་སྒྲིག་ `README.md` སྟོན་ཐངས་སྦེ་འདྲ་བཤུས་འབདཝ་ཨིན། Root གི་ཇ་པཱན་ README འདི་སྐད་བསྒྱུར་འབྱུང་ཁུངས་ **མེན**། ས་གནས་སྐད་ཡིག་གཞན་ 181 ཚུ་ English ལས་འཕྲུལ་ཆས་ཀྱིས་སྐད་བསྒྱུར་འབདཝ་ཨིན།

## དྲན་ཐོ།

- GPU མེད་པ་ཅིན་ ནོཊ་བུག་གིས་སྒྲ་ཡིག་ཕབ་ནི་འགོ་མ་བཙུགས་པའི་ཧེ་མ་ལུ་མཚམས་འཇོགཔ་ཨིན།
- ལས་སྣོན་གྱི་དུས་ཚོད་འདི་ནང་འཇུག་གི་རིང་ཚད། སྒྲིག་སྟངས། དང་ Colab གིས་སྤྲོད་པའི་ GPU ལུ་རག་ལས། ཐེངས་དང་པ་ལུ་ NeMo དང་ཧ་ལམ་ 1.23 GB གི་མོ་ཌེལ་ཡང་ཕབ་ལེན་འབདཝ་ཨིན།
- སྒྲ་རིངམོ་ཚུ་ནང་འཁོད་ chunk སྦེ་ལས་སྣོན་འབདཝ་ལས་ chunk boundary ཉེ་འདབས་ལུ་ངོས་འཛིན་འགྱུར་སྲིད།

## ཚད་ལྡན་འབྱུང་ཁུངས་དང་བཟོ་བསྐྲུན།

སྐད་བསྒྱུར་འབད་ཆོག་པའི་ཚད་ལྡན་འབྱུང་ཁུངས།

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` འདི་མཉམ་འགྲོས་འབད་ཚར་བའི་ཚད་ལྡན་བརྙན་འཛིན་ཨིན། ཇ་པཱན་སྐད་འདི་ `locales/ja.json` ནང་ཞིབ་བཤེར་འབད་ཚར་བའི་སྐད་བསྒྱུར་སྦེ་བཞགཔ་ཨིནམ་དང་། དེའི་ README བརྙན་འཛིན་འདི་ root `README.md` ལུ་འདྲ་བཤུས་འབདཝ་ཨིན།

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

སྐད་བསྒྱུར་བདག་སྐྱོང་འདི་རྒྱུན་གྱི་ CI ལས་སོ་སོར་བཞག་ཡོད། རྒྱུན་གྱི་ལག་ལེན་པ་དང་ CI ལུ་སྐད་བསྒྱུར་གསང་ཡིག་མི་དགོས།

## ཆོག་མཆན།

Notebook scaffolding དང་ build/check scripts ཚུ་ MIT ཆོག་མཆན་འོག་ཨིན། Third Intelligence མོ་ཌེལ་འདི་ནཱ་ལས་བསྐྱར་འགྲེམས་མི་འབད་ཞིང་ **Apache-2.0** གིས་སྟངས་འཛིན་འབདཝ་ཨིན། ཕྱོགས་གསུམ་པའི་བརྟེན་ཆས་ཚུ་གིས་རང་རང་གི་ཆོག་མཆན་བཞགཔ་ཨིན།
