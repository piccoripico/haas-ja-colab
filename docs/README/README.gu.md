# Haas Japanese Colab

Google Colab નોટબુક, Third Intelligence **Haas-ja-v1.0** વડે જાપાની ઑડિયો અને વિડિયોનું ટ્રાન્સક્રિપ્શન કરવા માટે.

[![Colab માં ખોલો](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_gu.ipynb)

## વિશેષતાઓ

- **મફત:** Google Colab ના મફત GPU રનટાઇમ પર ચાલે છે.
- **જાપાની ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) નો ઉપયોગ કરે છે, જે જાપાની વાણી ઓળખ માટે અંદાજે 0.6B પેરામીટર ધરાવતું મોડેલ છે.
- **ઝડપી:** ટ્રાન્સક્રિપ્શન ઝડપથી પ્રક્રિયા કરી શકાય છે.
- **વિરામચિહ્નો:** મોડેલ અંદાજિત જાપાની વિરામચિહ્નો આઉટપુટ કરે છે.
- **ટાઇમસ્ટેમ્પ અને સબટાઇટલ:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **લાંબી ફાઇલ પ્રક્રિયા:** લાંબી ઑડિયો અને વિડિયો ફાઇલો પણ પ્રક્રિયા કરી શકાય છે.
- **Google Drive સપોર્ટ:** ફાઇલો સીધી અપલોડ કરો અથવા Google Drive માંથી વાંચો; આઉટપુટ ZIP ને ઇચ્છા મુજબ Drive પર સાચવી શકાય છે.
- **ઘણા આઉટપુટ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest અને ZIP.

## ઉપયોગ

1. **1. Settings** માં `INPUT_MODE` પસંદ કરો અને જરૂર હોય તો અન્ય સેટિંગ્સ સમાયોજિત કરો.
2. **Runtime → Run all** પસંદ કરો.
3. `INPUT_MODE = "upload"` સાથે **2. File selection / Google Drive mount** માં ફાઇલો પસંદ કરો.
4. પ્રક્રિયા પૂર્ણ થયા પછી આઉટપુટ ZIP આપમેળે ડાઉનલોડ થાય છે.

## ટાઇમસ્ટેમ્પ મોડ

- `none`: સમય સંબંધિત કોઈ માહિતી નહીં.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## ડિકોડર

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## લાંબી ફાઇલો

`CHUNK_SECONDS` લાંબી ફાઇલો માટે ઉપયોગમાં લેવાતા આંતરિક chunk ની અવધિ નિયંત્રિત કરે છે. મોટા મૂલ્યો સીમાઓ ઘટાડે છે અને વધુ context જાળવે છે, પરંતુ દરેક inference ભારે બને છે અને GPU memory નો વધુ ઉપયોગ કરી શકે છે. નાના મૂલ્યો દરેક inference ને હળવો બનાવે છે, પરંતુ વધુ સીમાઓ બનાવે છે, જે તે બિંદુઓની આસપાસ ઓળખ પર અસર કરી શકે છે. મોટા ભાગના કિસ્સામાં ડિફૉલ્ટ મૂલ્યની ભલામણ થાય છે.

## સ્થાનિકીકૃત UI

ASR મોડેલ પોતે **ફક્ત જાપાની માટે** છે. README અને Colab UI નું સ્થાનિકીકરણ **ISO 639 Set 1 ની તમામ 183 સક્રિય ભાષાઓ** આવરી લે છે (deprecated `sh` સિવાય).

અંગ્રેજી (`en`) canonical અનુવાદ સ્ત્રોત છે. જાપાની (`ja`) સમીક્ષિત અનુવાદ છે અને ડિફૉલ્ટ `README.md` પ્રસ્તુતિ તરીકે repository root પર નકલ થાય છે. root પરનો જાપાની README **અનુવાદ સ્ત્રોત તરીકે ઉપયોગમાં લેવાતો નથી**. બાકીના 181 locale અંગ્રેજીમાંથી machine translation થાય છે.

## નોંધો

- GPU ઉપલબ્ધ ન હોય તો notebook ટ્રાન્સક્રિપ્શન પહેલાં બંધ થઈ જાય છે.
- પ્રક્રિયા સમય input ની લંબાઈ, settings અને Colab દ્વારા ફાળવેલા GPU પર આધારિત છે. પ્રથમ run માં NeMo અને અંદાજે 1.23 GB નું મોડેલ પણ ડાઉનલોડ થાય છે.
- લાંબો ઑડિયો આંતરિક chunks માં પ્રક્રિયા થાય છે, તેથી chunk સીમાઓની આસપાસ ઓળખ પર અસર થઈ શકે છે.

## Canonical સ્ત્રોત અને generation

Canonical અનુવાદયોગ્ય સ્ત્રોત:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot છે. જાપાની `locales/ja.json` માં reviewed translation તરીકે જાળવવામાં આવે છે, અને તેનો README snapshot root `README.md` પર નકલ થાય છે.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

અનુવાદ જાળવણી સામાન્ય CI થી અલગ છે. સામાન્ય users અને CI ને translation credentials ની જરૂર નથી.

## લાઇસન્સ

Notebook scaffolding અને build/check scripts MIT લાઇસન્સ હેઠળ છે. Third Intelligence મોડેલ અહીં ફરી વહેંચાતું નથી અને **Apache-2.0** હેઠળ સંચાલિત થાય છે. Third-party dependencies પોતાના લાઇસન્સ જાળવે છે.
