# Haas Japanese Colab

د Third Intelligence په کارولو د جاپاني غږ او ویډیو د متن کولو لپاره Google Colab کتابچه: Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ps.ipynb)

## ځانګړنې

- **وړیا:** يعمل على بيئة GPU الوړیاة في Google Colab.
- **ASR لليابانية:** يستخدم [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0)، وهو نموذج بحوالي 0.6B معلمة للتعرّف على الكلام الياباني.
- **چټک:** يمكن معالجة النسخ بسرعة.
- **نښانونه:** ينتج النموذج علامات ترقيم يابانية مقدّرة.
- **وخت نښې او فرعي سرلیکونه:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **د اوږدو فایلونو پروسس:** يمكن أيضًا معالجة ملفات الصوت والفيديو الطويلة.
- **د Google Drive ملاتړ:** ارفع الملفات مباشرة أو اقرأها من Google Drive؛ ويمكن حفظ ملف ZIP الناتج في Drive اختياريًا.
- **ډېرې پایلې:** TXT وMarkdown وJSON وCSV وXLSX وSRT وmanifest وZIP.

## کارول

1. اختر `INPUT_MODE` في **1. Settings** واضبط الإعدادات الأخرى عند الحاجة.
2. اختر **Runtime → Run all**.
3. عند `INPUT_MODE = "upload"`، اختر الملفات في **2. File selection / Google Drive mount**.
4. يتم تنزيل ملف ZIP الناتج تلقائيًا بعد انتهاء المعالجة.

## د وخت نښو حالتونه

- `none`: بدون معلومات زمنية.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## ډیکوډر

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## اوږده فایلونه

يتحكم `CHUNK_SECONDS` في مدة الجزء الداخلي المستخدمة للملفات الطويلة. تقلل القيم الأكبر عدد الحدود وتحافظ على سياق أكبر، لكنها تجعل كل استدلال أثقل وقد تزيد استخدام ذاكرة GPU. تجعل القيم الأصغر كل استدلال أخف لكنها تنشئ حدودًا أكثر، مما قد يؤثر في التعرّف حول تلك النقاط. يوصى بالقيمة الافتراضية في معظم الحالات.

## ځایي شوی انټرفیس

نموذج ASR نفسه **مخصص لليابانية فقط**. تغطي ترجمة README وواجهة Colab جميع **اللغات النشطة الـ183 في ISO 639 Set 1** (مع استبعاد `sh` المهجورة).

الإنجليزية (`en`) هي مصدر الترجمة القانوني. اليابانية (`ja`) ترجمة مراجعة وتُنسخ إلى جذر المستودع كعرض `README.md` الافتراضي. ملف README الياباني في الجذر **لا** يُستخدم كمصدر للترجمة. تتم ترجمة اللغات الـ181 الأخرى آليًا من الإنجليزية.

## یادښتونه

- يتوقف الدفتر قبل النسخ إذا لم تكن GPU متاحة.
- يعتمد وقت المعالجة على طول الإدخال والإعدادات وGPU التي يخصصها Colab. كما يقوم التشغيل الأول بتنزيل NeMo والنموذج بحجم يقارب 1.23 GB.
- تتم معالجة الصوت الطويل في أجزاء داخلية، لذلك قد يتأثر التعرّف قرب حدود الأجزاء.

## کانوني سرچینه او تولید

المصادر القانونية القابلة للترجمة:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` هو snapshot القانوني المتزامن. تتم صيانة اليابانية كترجمة مراجعة في `locales/ja.json`، وتُنسخ لقطة README الخاصة بها إلى الجذر باسم `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

صيانة الترجمات منفصلة عن CI العادي. لا يحتاج المستخدمون العاديون ولا CI إلى بيانات اعتماد للترجمة.

## جواز

هيكل الدفتر ونصوص build/check مرخّصة بموجب MIT. لا تتم إعادة توزيع نموذج Third Intelligence هنا ويخضع لـ **Apache-2.0**. تحتفظ تبعيات الأطراف الثالثة بتراخيصها الخاصة.
