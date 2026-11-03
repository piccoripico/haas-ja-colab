# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ഉപയോഗിച്ച് ജാപ്പനീസ് ഓഡിയോയും വീഡിയോയും ട്രാൻസ്‌ക്രൈബ് ചെയ്യാനുള്ള Google Colab നോട്ട്‌ബുക്ക്.

[![Colab-ൽ തുറക്കുക](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ml.ipynb)

## സവിശേഷതകൾ

- **സൗജന്യം:** Google Colab-ന്റെ സൗജന്യ GPU runtime-ൽ പ്രവർത്തിക്കുന്നു.
- **ജാപ്പനീസ് ASR:** ജാപ്പനീസ് ശബ്ദം തിരിച്ചറിയാൻ ഏകദേശം 0.6B പാരാമീറ്ററുകളുള്ള [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) മോഡൽ ഉപയോഗിക്കുന്നു.
- **വേഗം:** ട്രാൻസ്‌ക്രിപ്ഷൻ വേഗത്തിൽ പ്രോസസ് ചെയ്യാം.
- **വിരാമചിഹ്നങ്ങൾ:** മോഡൽ കണക്കാക്കിയ ജാപ്പനീസ് വിരാമചിഹ്നങ്ങൾ ഔട്ട്പുട്ട് ചെയ്യുന്നു.
- **ടൈംസ്റ്റാമ്പുകളും സബ്‌ടൈറ്റിലുകളും:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ദീർഘ ഫയൽ പ്രോസസ്സിംഗ്:** ദീർഘമായ ഓഡിയോ, വീഡിയോ ഫയലുകളും പ്രോസസ് ചെയ്യാം.
- **Google Drive പിന്തുണ:** ഫയലുകൾ നേരിട്ട് അപ്‌ലോഡ് ചെയ്യുകയോ Google Drive-ൽ നിന്ന് വായിക്കുകയോ ചെയ്യാം; ഔട്ട്പുട്ട് ZIP ഐച്ഛികമായി Drive-ൽ സേവ് ചെയ്യാം.
- **ഒന്നിലധികം ഔട്ട്പുട്ടുകൾ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## ഉപയോഗം

1. **1. ക്രമീകരണങ്ങൾ** എന്നതിൽ `INPUT_MODE` തിരഞ്ഞെടുക്കുകയും ആവശ്യമെങ്കിൽ മറ്റ് ക്രമീകരണങ്ങൾ മാറ്റുകയും ചെയ്യുക.
2. **Runtime → Run all** തിരഞ്ഞെടുക്കുക.
3. `INPUT_MODE = "upload"` ആണെങ്കിൽ **2. ഫയൽ തിരഞ്ഞെടുക്കൽ / Google Drive മൗണ്ട്** എന്നതിൽ ഫയലുകൾ തിരഞ്ഞെടുക്കുക.
4. പ്രോസസ്സിംഗ് പൂർത്തിയായ ശേഷം ഔട്ട്പുട്ട് ZIP സ്വയം ഡൗൺലോഡ് ചെയ്യും.

## ടൈംസ്റ്റാമ്പ് മോഡുകൾ

- `none`: സമയവിവരം ഒന്നുമില്ല.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## ഡികോഡർ

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ദീർഘ ഫയലുകൾ

`CHUNK_SECONDS` ദീർഘ ഫയലുകൾക്കുള്ള ആന്തരിക chunk ദൈർഘ്യം നിയന്ത്രിക്കുന്നു. വലിയ മൂല്യങ്ങൾ chunk അതിരുകൾ കുറച്ച് കൂടുതൽ context നിലനിർത്തും, പക്ഷേ ഓരോ inference-ഉം ഭാരമേറിയതാകുകയും കൂടുതൽ GPU memory ഉപയോഗിക്കാനും ഇടയാക്കും. ചെറിയ മൂല്യങ്ങൾ inference ലഘൂകരിക്കും, പക്ഷേ കൂടുതൽ അതിരുകൾ സൃഷ്ടിക്കുന്നതിനാൽ അവിടങ്ങളിലെ തിരിച്ചറിയലിനെ ബാധിക്കാം. സാധാരണ default മൂല്യം ശുപാർശ ചെയ്യുന്നു.

## ലോക്കലൈസ്ഡ് UI

ASR മോഡൽ തന്നെ **ജാപ്പനീസ് മാത്രം** പിന്തുണക്കുന്നു. README, Colab UI ലോക്കലൈസേഷൻ **183 സജീവ ISO 639 Set 1 ഭാഷകൾ** എല്ലാം ഉൾക്കൊള്ളുന്നു (deprecated `sh` ഒഴിവാക്കി).

ഇംഗ്ലീഷ് (`en`) ആണ് canonical translation source. ജാപ്പനീസ് (`ja`) പരിശോധിച്ച വിവർത്തനമാണ്; repository root-ൽ default `README.md` ആയി കോപ്പി ചെയ്യുന്നു. Root ജാപ്പനീസ് README **വിവർത്തന സ്രോതസായി ഉപയോഗിക്കില്ല**. ശേഷിക്കുന്ന 181 locales ഇംഗ്ലീഷിൽ നിന്ന് machine translation ചെയ്യുന്നു.

## കുറിപ്പുകൾ

- GPU ലഭ്യമല്ലെങ്കിൽ ട്രാൻസ്‌ക്രിപ്ഷൻ തുടങ്ങുന്നതിന് മുമ്പ് നോട്ട്‌ബുക്ക് നിർത്തും.
- പ്രോസസ്സിംഗ് സമയം input ദൈർഘ്യം, ക്രമീകരണങ്ങൾ, Colab നൽകുന്ന GPU എന്നിവയെ ആശ്രയിക്കുന്നു. ആദ്യ run-ൽ NeMoയും ഏകദേശം 1.23 GB മോഡലും ഡൗൺലോഡ് ചെയ്യും.
- ദീർഘ ഓഡിയോ ആന്തരിക chunks ആയി പ്രോസസ് ചെയ്യുന്നതിനാൽ chunk അതിരുകൾക്കടുത്ത് തിരിച്ചറിയൽ ബാധിക്കാം.

## Canonical source-ും generation-ും

വിവർത്തനം ചെയ്യാവുന്ന canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot ആണ്. ജാപ്പനീസ് `locales/ja.json`-ൽ reviewed translation ആയി പരിപാലിക്കുന്നു; അതിന്റെ README snapshot root `README.md`-ലേക്ക് കോപ്പി ചെയ്യുന്നു.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance സാധാരണ CI-യിൽ നിന്ന് വേർതിരിച്ചിരിക്കുന്നു. സാധാരണ ഉപയോക്താക്കൾക്കും CI-ക്കും translation credentials ആവശ്യമില്ല.

## ലൈസൻസ്

Notebook scaffolding-ും build/check scripts-ും MIT ലൈസൻസിലാണ്. Third Intelligence മോഡൽ ഇവിടെ redistribute ചെയ്യുന്നില്ല; അത് **Apache-2.0** പ്രകാരമാണ്. Third-party dependencies അവരുടെ സ്വന്തം ലൈസൻസുകൾ നിലനിർത്തുന്നു.
