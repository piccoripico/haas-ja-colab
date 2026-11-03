# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ব্যৱহাৰ কৰি জাপানী অডিঅ’ আৰু ভিডিঅ’ প্ৰতিলিপি কৰাৰ বাবে Google Colab notebook।

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_as.ipynb)

## বৈশিষ্ট্যসমূহ

- **বিনামূলীয়া:** Google Colab-ৰ বিনামূলীয়া GPU runtime-ত চলে।
- **জাপানী ASR:** জাপানী বাক্-স্বীকৃতিৰ বাবে প্ৰায় 0.6B-পেৰামিটাৰ মডেল [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ব্যৱহাৰ কৰে।
- **দ্ৰুত:** প্ৰতিলিপি দ্ৰুতভাৱে প্ৰক্ৰিয়াকৰণ কৰিব পাৰি।
- **যতি-চিহ্ন:** মডেলে অনুমান কৰা জাপানী যতি-চিহ্ন আউটপুট কৰে।
- **সময়চিহ্ন আৰু subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **দীঘল ফাইল প্ৰক্ৰিয়াকৰণ:** দীঘল অডিঅ’ আৰু ভিডিঅ’ ফাইলো প্ৰক্ৰিয়াকৰণ কৰিব পাৰি।
- **Google Drive সমৰ্থন:** ফাইল পোনপটীয়াকৈ আপল’ড কৰক বা Google Drive-ৰ পৰা পঢ়ক; আউটপুট ZIP ইচ্ছামতে Drive-ত সংৰক্ষণ কৰিব পাৰি।
- **একাধিক আউটপুট:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest আৰু ZIP।

## ব্যৱহাৰ

1. **1. Settings**-ত `INPUT_MODE` বাছক আৰু প্ৰয়োজন হ’লে অন্য settings সলনি কৰক।
2. **Runtime → Run all** বাছক।
3. `INPUT_MODE = "upload"` হ’লে **2. File selection / Google Drive mount**-ত ফাইল বাছক।
4. প্ৰক্ৰিয়াকৰণ শেষ হোৱাৰ পিছত আউটপুট ZIP স্বয়ংক্ৰিয়ভাৱে ডাউনল’ড হয়।

## সময়চিহ্ন mode

- `none`: কোনো সময়ৰ তথ্য নাই।
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## দীঘল ফাইল

`CHUNK_SECONDS`-এ দীঘল ফাইলৰ বাবে ব্যৱহৃত ভিতৰুৱা chunk-ৰ সময়কাল নিয়ন্ত্ৰণ কৰে। ডাঙৰ মানে সীমা কমায় আৰু অধিক context ৰাখে, কিন্তু প্ৰতিটো inference গধুৰ কৰে আৰু GPU memory ব্যৱহাৰ বঢ়াব পাৰে। সৰু মানে প্ৰতিটো inference পাতল কৰে কিন্তু অধিক সীমা সৃষ্টি কৰে, যিয়ে সেই স্থানবোৰৰ ওচৰত স্বীকৃতিক প্ৰভাৱিত কৰিব পাৰে। অধিকাংশ ক্ষেত্ৰত default মান ব্যৱহাৰ কৰাটো পৰামৰ্শযোগ্য।

## স্থানীয়কৃত UI

ASR মডেলটো নিজে **কেৱল জাপানীৰ বাবে**। README আৰু Colab UI স্থানীয়কৰণে **ISO 639 Set 1-ৰ সকলো 183টা সক্ৰিয় ভাষা** (`sh` বাদ দি) সামৰি লয়।

ইংৰাজী (`en`) canonical অনুবাদ উৎস। জাপানী (`ja`) পৰ্যালোচিত অনুবাদ আৰু default `README.md` প্ৰদৰ্শন হিচাপে repository root-লৈ copy কৰা হয়। root-ৰ জাপানী README **অনুবাদ উৎস হিচাপে ব্যৱহাৰ কৰা নহয়**। আন 181টা locale ইংৰাজীৰ পৰা machine translation কৰা হয়।

## টোকা

- GPU উপলব্ধ নহ’লে notebook-এ প্ৰতিলিপিৰ আগতে বন্ধ হয়।
- প্ৰক্ৰিয়াকৰণ সময় input-ৰ দৈৰ্ঘ্য, settings আৰু Colab-এ দিয়া GPU-ৰ ওপৰত নিৰ্ভৰ কৰে। প্ৰথম run-এ NeMo আৰু প্ৰায় 1.23 GB মডেলটোও ডাউনল’ড কৰে।
- দীঘল অডিঅ’ ভিতৰুৱা chunk-ত প্ৰক্ৰিয়াকৰণ হয়, সেয়ে chunk boundary-ৰ ওচৰত স্বীকৃতি প্ৰভাৱিত হ’ব পাৰে।

## Canonical উৎস আৰু generation

Canonical অনুবাদযোগ্য উৎস:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot। জাপানী `locales/ja.json`-ত পৰ্যালোচিত অনুবাদ হিচাপে ৰখা হয়, আৰু তাৰ README snapshot root `README.md`-লৈ copy কৰা হয়।

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

অনুবাদ maintenance সাধাৰণ CI-ৰ পৰা পৃথক। সাধাৰণ ব্যৱহাৰকাৰী আৰু CI-ৰ অনুবাদ credential নালাগে।

## লাইচেন্স

Notebook scaffolding আৰু build/check scripts MIT licensed। Third Intelligence মডেল ইয়াত পুনৰ বিতৰণ কৰা নহয় আৰু **Apache-2.0**-ৰ অধীন। Third-party dependencies-এ নিজৰ লাইচেন্স বজাই ৰাখে।
