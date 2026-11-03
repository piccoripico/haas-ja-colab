# Haas Japanese Colab

Google Colab notebook-ŋa Japanimiut nipaa video-lu allaguanŋortinniarlugu Third Intelligence **Haas-ja-v1.0** atorlugu.

[![Colab-mi aŋmaq](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ik.ipynb)

## Suliarisinnaġai

- **Akiqanngitchuq:** Google Colab free GPU runtime-mi suliuruq.
- **Japanimiut ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) aturuq, 0.6B parameter model-mik Japanimiut uqausiat allaguanŋortinniarlugit.
- **Sukattuq:** Transcription sukkasuumik suliarisinnaġaa.
- **Punctuation:** Model-ŋa Japanimiut allagvianni nalunaaqutait nalautchillugu saqqummersittagai.
- **Timestamps subtitles-lu:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Aŋisuut files:** Sivisuut audio video-lu files suliarisinnaġai.
- **Google Drive:** Files toqqaannartumik upload-giñ imaluunniit Google Drive-miittut atuġin; output ZIP piumaguvich Drive-mut tutquqsinnaġaat.
- **Output assigiinngitsut:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP-lu.

## Atuqtuġniq

1. `INPUT_MODE` **1. Settings**-mi toqqaruk, pisariaqpat settings allat allanngortikkit.
2. **Runtime → Run all** toqqaruk.
3. `INPUT_MODE = "upload"`-uppat, files **2. File selection / Google Drive mount**-mi toqqakkit.
4. Suliap naammassippat output ZIP nammineq download-giñiġaqtuq.

## Timestamp modes

- `none`: piffissamik paasissutissaqanngilaq.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Aŋisuut files

`CHUNK_SECONDS` aŋisuup file-ŋa internal chunk-ni qanuq sivisutigisumik suliarineqassanersoq aquppaa. Value aŋiniqsaq boundaries ikilisaġai context-ilu amerlanerusumik tutquġaa, kisiannili inference atausiq oqimaanneruvoq GPU memory-lu amerlanerusumik atorsinnaġaa. Value mikiniqsaq inference-mik oqilisaaqtuq, kisiannili boundaries amerlanerusut suliarivai, taakkualu eqqaanni recognition allanngorsinnaġaa. Default amerlanerni atussallugu piuŋneruvoq.

## Uqausiq lokal-giñiq

ASR model **Japanimiut uqausiannut kisimi** suliaruq. README Colab UI-lu lokal-giñiq **183 active ISO 639 Set 1 languages** tamaasa atuġai (`sh` deprecated-iuŋmat ilanngunneqanngilaq).

English (`en`) canonical translation source-iuvoq. Japanese (`ja`) reviewed translation-iuvoq, repository root-mut default `README.md`-tut copy-giñiġaqtuq. Root Japanese README **translation source-ŋunngitchuq**. 181 locales allat English-miit machine-translated-iuput.

## Nalunaiqsuutit

- GPU pissarsiarinngippagu notebook transcription sioqqullugu unitsiġaqtuq.
- Processing time input-ip sivisussusianik, settings-nik, Google Colab-milu GPU-mik tunineqarnermik aallaaveqarpoq. Siullermik run-giñiġami NeMo 1.23 GB model-lu download-giñiġaqtut.
- Sivisuq audio internal chunks-ni suliarineqaqtuq, taimaattumik chunk boundaries eqqaanni recognition allanngorsinnaġaa.

## Canonical source generation-lu

Canonical source-t nutserneqarsinnaasut:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot-iuvoq. Japanese reviewed translation `locales/ja.json`-mi tutquġaqtuq, README snapshot-lu root `README.md`-mut copy-giñiġaqtuq.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI-miit ayrı suliassaavoq. Ordinary users CI-lu translation credentials pisariaqartinngilaat.

## License

Notebook scaffolding build/check scripts-lu MIT licensed-iuput. Third Intelligence model maani redistribute-giñiġanngilaq, **Apache-2.0**-lu malillugu aqunneqarluni. Third-party dependencies namminneq licenses pigaat.
