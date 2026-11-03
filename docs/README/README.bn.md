# Haas Japanese Colab

Google Colab-এ Third Intelligence **Haas-ja-v1.0** ব্যবহার করে জাপানি অডিও ও ভিডিও ট্রান্সক্রাইব করার নোটবুক।

[![Colab-এ খুলুন](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_bn.ipynb)

## বৈশিষ্ট্য

- **বিনামূল্যে:** Google Colab-এর বিনামূল্যের GPU রানটাইমে চলে।
- **জাপানি ASR:** জাপানি কথ্য ভাষা শনাক্তকরণের জন্য প্রায় 0.6B-প্যারামিটারের মডেল [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ব্যবহার করে।
- **দ্রুত:** ট্রান্সক্রিপশন দ্রুত প্রক্রিয়া করা যায়।
- **যতিচিহ্ন:** মডেলটি অনুমান করা জাপানি যতিচিহ্ন আউটপুট করে।
- **টাইমস্ট্যাম্প ও সাবটাইটেল:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **দীর্ঘ ফাইল প্রক্রিয়াকরণ:** দীর্ঘ অডিও ও ভিডিও ফাইলও প্রক্রিয়া করা যায়।
- **Google Drive সমর্থন:** ফাইল সরাসরি আপলোড করুন অথবা Google Drive থেকে পড়ুন; আউটপুট ZIP ইচ্ছা করলে Drive-এ সংরক্ষণ করা যায়।
- **একাধিক আউটপুট:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest এবং ZIP।

## ব্যবহার

1. **1. Settings**-এ `INPUT_MODE` নির্বাচন করুন এবং প্রয়োজন হলে অন্য সেটিংস বদলান।
2. **Runtime → Run all** নির্বাচন করুন।
3. `INPUT_MODE = "upload"` হলে **2. File selection / Google Drive mount**-এ ফাইল নির্বাচন করুন।
4. প্রক্রিয়াকরণের পরে আউটপুট ZIP স্বয়ংক্রিয়ভাবে ডাউনলোড হয়।

## টাইমস্ট্যাম্প মোড

- `none`: কোনো সময়সংক্রান্ত তথ্য নেই।
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## ডিকোডার

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## দীর্ঘ ফাইল

`CHUNK_SECONDS` দীর্ঘ ফাইলের জন্য ব্যবহৃত অভ্যন্তরীণ chunk-এর দৈর্ঘ্য নিয়ন্ত্রণ করে। বড় মান boundary কমায় এবং বেশি context ধরে রাখে, কিন্তু প্রতিটি inference ভারী হয় এবং GPU মেমরি বেশি ব্যবহার করতে পারে। ছোট মান প্রতিটি inference হালকা করে, কিন্তু আরও boundary তৈরি করে, যা ঐ পয়েন্টগুলোর কাছাকাছি শনাক্তকরণে প্রভাব ফেলতে পারে। অধিকাংশ ক্ষেত্রে ডিফল্ট মানই সুপারিশকৃত।

## স্থানীয়কৃত UI

ASR মডেলটি নিজে **শুধু জাপানি**। README এবং Colab UI-এর স্থানীয়করণে **183টি সক্রিয় ISO 639 Set 1 ভাষা** অন্তর্ভুক্ত (অবসরপ্রাপ্ত `sh` বাদ)।

ইংরেজি (`en`) হলো canonical অনুবাদ উৎস। জাপানি (`ja`) একটি পর্যালোচিত অনুবাদ এবং ডিফল্ট `README.md` প্রদর্শন হিসেবে repository root-এ কপি করা হয়। root-এর জাপানি README **অনুবাদ উৎস হিসেবে ব্যবহৃত হয় না**। অন্য 181টি locale ইংরেজি থেকে machine translation করা।

## নোট

- GPU না থাকলে ট্রান্সক্রিপশন শুরু হওয়ার আগে নোটবুক থেমে যায়।
- প্রক্রিয়াকরণের সময় input-এর দৈর্ঘ্য, settings এবং Colab যে GPU দেয় তার ওপর নির্ভর করে। প্রথম run-এ NeMo এবং প্রায় 1.23 GB মডেলও ডাউনলোড হয়।
- দীর্ঘ অডিও অভ্যন্তরীণ chunk-এ প্রক্রিয়া করা হয়, তাই chunk boundary-র আশেপাশে শনাক্তকরণ প্রভাবিত হতে পারে।

## Canonical উৎস ও generation

Canonical অনুবাদযোগ্য উৎস:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` হলো synchronized canonical snapshot। জাপানি `locales/ja.json`-এ reviewed translation হিসেবে রক্ষণাবেক্ষণ করা হয়, এবং তার README snapshot root `README.md`-এ কপি করা হয়।

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

অনুবাদ রক্ষণাবেক্ষণ সাধারণ CI থেকে আলাদা। সাধারণ ব্যবহারকারী ও CI-এর translation credential দরকার হয় না।

## লাইসেন্স

Notebook scaffolding ও build/check script MIT লাইসেন্সের অধীনে। Third Intelligence মডেল এখানে পুনর্বিতরণ করা হয় না এবং এটি **Apache-2.0**-এর অধীন। তৃতীয়-পক্ষ dependency তাদের নিজস্ব লাইসেন্স বহাল রাখে।
