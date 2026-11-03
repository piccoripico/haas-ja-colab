# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** በመጠቀም የጃፓንኛ ድምፅና ቪዲዮ ፋይሎችን ለመገልበጥ የGoogle Colab ማስታወሻ ደብተር።

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_am.ipynb)

## ባህሪያት

- **ነጻ፦** በGoogle Colab ነጻ GPU runtime ላይ ይሰራል።
- **የጃፓንኛ ASR፦** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) የሚለውን፣ ለጃፓንኛ ንግግር ማወቂያ የተዘጋጀ በግምት 0.6B ፓራሜትር ያለው ሞዴል ይጠቀማል።
- **ፈጣን፦** ግልባጭ በፍጥነት ሊከናወን ይችላል።
- **ሥርዓተ ነጥብ፦** ሞዴሉ የተገመተ የጃፓንኛ ሥርዓተ ነጥብ ያወጣል።
- **የጊዜ ማህተሞችና ንዑስ ርዕሶች፦** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ረጅም ፋይል ማቀናበር፦** ረጅም የድምፅና የቪዲዮ ፋይሎችም ሊቀናበሩ ይችላሉ።
- **የGoogle Drive ድጋፍ፦** ፋይሎችን በቀጥታ ይስቀሉ ወይም ከGoogle Drive ያንብቡ፤ የውጤት ZIP ከፈለጉ ወደ Drive ሊቀመጥ ይችላል።
- **ብዙ ውጤቶች፦** TXT፣ Markdown፣ JSON፣ CSV፣ XLSX፣ SRT፣ manifest እና ZIP።

## አጠቃቀም

1. በ **1. Settings** ውስጥ `INPUT_MODE` ይምረጡ እና ካስፈለገ ሌሎች ቅንብሮችን ያስተካክሉ።
2. **Runtime → Run all** ይምረጡ።
3. `INPUT_MODE = "upload"` ከሆነ ፋይሎችን በ **2. File selection / Google Drive mount** ውስጥ ይምረጡ።
4. ሂደቱ ከተጠናቀቀ በኋላ የውጤት ZIP በራስ-ሰር ይወርዳል።

## የጊዜ ማህተም ሁነታዎች

- `none`: የጊዜ መረጃ የለም።
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## ዲኮደር

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ረጅም ፋይሎች

`CHUNK_SECONDS` ለረጅም ፋይሎች የሚጠቀመውን ውስጣዊ የክፍል ጊዜ ይቆጣጠራል። ትልቅ እሴቶች የክፍል ድንበሮችን ይቀንሳሉ እና ተጨማሪ አውድ ይጠብቃሉ፣ ነገር ግን እያንዳንዱን inference ከባድ ያደርጉታል እና የGPU ማህደረ ትውስታ አጠቃቀምን ሊጨምሩ ይችላሉ። ትንሽ እሴቶች እያንዳንዱን inference ቀላል ያደርጉታል ነገር ግን ተጨማሪ ድንበሮችን ይፈጥራሉ፣ ይህም በእነዚያ ነጥቦች ዙሪያ ያለውን ማወቂያ ሊጎዳ ይችላል። በአብዛኛው ነባሪው ይመከራል።

## የአካባቢ በይነገጽ

የASR ሞዴሉ ራሱ **ለጃፓንኛ ብቻ** ነው። የREADME እና Colab UI አካባቢያዊነት **183 ንቁ ISO 639 Set 1 ቋንቋዎችን** (`sh` የተተወውን ሳይጨምር) ይሸፍናል።

እንግሊዝኛ (`en`) ቀኖናዊ የትርጉም ምንጭ ነው። ጃፓንኛ (`ja`) የተገመገመ ትርጉም ነው እና እንደ ነባሪ `README.md` ማሳያ ወደ repository root ይቀዳል። የroot ጃፓንኛ README **እንደ ትርጉም ምንጭ አይጠቀምም**። ሌሎቹ 181 locale-ዎች ከእንግሊዝኛ በማሽን ይተረጎማሉ።

## ማስታወሻዎች

- GPU ከሌለ ማስታወሻ ደብተሩ ከግልባጭ በፊት ይቆማል።
- የማቀናበሪያ ጊዜ በግቤት ርዝመት፣ ቅንብሮች እና በColab በተመደበው GPU ላይ ይወሰናል። የመጀመሪያው ማስኬድ NeMo እና በግምት 1.23 GB ሞዴሉን ያወርዳል።
- ረጅም ድምፅ በውስጣዊ ክፍሎች ይቀናበራል፣ ስለዚህ በክፍል ድንበሮች ዙሪያ ማወቂያ ሊጎዳ ይችላል።

## ቀኖናዊ ምንጭ እና ማመንጨት

ቀኖናዊ ሊተረጎሙ የሚችሉ ምንጮች፦

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` የተመሳሰለ ቀኖናዊ snapshot ነው። ጃፓንኛ በ`locales/ja.json` ውስጥ እንደ የተገመገመ ትርጉም ይጠበቃል፣ የREADME snapshot-ውም ወደ root `README.md` ይቀዳል።

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

የትርጉም ጥገና ከመደበኛ CI የተለየ ነው። መደበኛ ተጠቃሚዎችና CI የትርጉም credentials አያስፈልጋቸውም።

## ፈቃድ

የNotebook scaffolding እና build/check scripts በMIT ፈቃድ የተሰጡ ናቸው። የThird Intelligence ሞዴል እዚህ እንደገና አይሰራጭም እና በ **Apache-2.0** ይተዳደራል። የሶስተኛ ወገን dependencies የራሳቸውን ፈቃዶች ይጠብቃሉ።
