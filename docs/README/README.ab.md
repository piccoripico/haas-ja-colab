# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ахархәарала аиапон аудиои видеои ртранскрипциазы Google Colab notebook.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ab.ipynb)

## Алшарақәа

- **Хәыда-ԥсадатәи:** Google Colab хәыда-ԥсадатәи GPU runtime аҟны аус ауеит.
- **Иапон ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ахархәара ауеит, уи аиапон абжьы аилкааразы 0.6B параметр змоу модельуп.
- **Иццакуеит:** Атранскрипциа ирласны иҟаҵазар ауеит.
- **Ариашара:** Амодель аиапон ариашаратә дыргақәа аԥнагоит.
- **Аамҭа дыргақәеи асубтитрқәеи:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Афайл дуқәа аус рыдулара:** Аудиои видеои афайл дуқәагьы аус рыдулара ауеит.
- **Google Drive адгыларա:** Афайлқәа ишиашоу иҭажәгал, мамзаргьы Google Drive аҟынтә шәрыԥхьала; алҵшәатә ZIP Drive аҟны иҵәахзар ауеит.
- **Алҵшәақәа жәпакы:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## Ахархәара

1. **1. Settings** аҟны `INPUT_MODE` алышәх, pisariaqartхаргьы дара settings шәаԥсах.
2. **Runtime → Run all** алышәх.
3. `INPUT_MODE = "upload"` акәзар, **2. File selection / Google Drive mount** аҟны афайлқәа алышәх.
4. Аус адулара анынҵәалак, алҵшәатә ZIP автоматла download ҟалоит.

## Timestamp режимқәа

- `none`: аԥхынатә адыррақәа ыҟаӡам.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Афайл дуқәа

`CHUNK_SECONDS` афайл дуқәа рзы internal chunk-иамҭа шьақәнаргылоит. Ахә дуқәа boundary-қәа еиҵартәуеит, context еиҳагьы ихьчоит, аха inference бжаӡа еиҳагьы ицәгьоуп, GPU memory ахархәарагьы иазҳауеит. Ахә маҷқәа inference иарманшәалоит, аха boundary-қәа еиҳаны иаԥыргоит, уи урҭ аҭыҧқәа рҿы recognition ианырыр алшо. Ирацәаны default ахә лҵшәаны еиӷьуп.

## Алокализациа зызу UI

ASR амодель ахаҭа **аиапон бызшәазы мацара** ауп. READMEи Colab UIи рлокализациа **ISO 639 Set 1 актив 183 бызшәак** зегьы аҵанакуеит (`sh` аныжьуп).

Англыз (`en`) — canonical translation source. Аиапон (`ja`) — reviewed translation, default `README.md` рәԥшра аҳасабала repository root ахь икопиахоит. Root аҿы аиапон README **translation source аҳасабала ахархәара аҭам**. Егьырҭ 181 locale англыз аҟынтә machine-translate ҟалоит.

## Азгәаҭақәа

- GPU ыҟазарым, notebook атранскрипциа иалагаанӡа иаанхоит.
- Аус адулара иамҭа input аҭбаара, settings, Colab иҟанаҵаз GPU ирыдҳәалоуп. Аԥхьатәи run NeMoи 1.23 GB амодельигьы download ҟанагоит.
- Аудио ду internal chunk-қәа рыла аус адулара амоуп, уи азы chunk boundary-қәа рааигәара recognition ианырыр алшо.

## Canonical sourceи generationи

Canonical а翻訳 зылшо sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot ауп. Аиапон `locales/ja.json` аҟны reviewed translation аҳасабала иҵәахуп, уи README snapshot root `README.md` ахь икопиахоит.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI аҟынтә хазыуп. Ordinary usersи CIи translation credentials рҭахым.

## License

Notebook scaffoldingи build/check scriptsи MIT license рымоуп. Third Intelligence амодель араҟа ирыладырҵәом, **Apache-2.0** аҵаҟа ауп. Third-party dependencies дара рлицензиақәа рыхьчоит.
