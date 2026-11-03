# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** nissāya Jāpāna-sadda-rūpa-file lipiṃ kātuṃ Google Colab notebook.

[![Colab majjhe vivaratha](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_pi.ipynb)

## Guṇā

- **Nissulkaṃ:** Google Colab nissulka-GPU-runtime majjhe pavattati.
- **Jāpāna ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) nāma, pamāṇena 0.6B-parameter-yuttaṃ Jāpāna-vācā-parijānana-model, upayujjati.
- **Sīghaṃ:** Transcription sīghaṃ saṅkhārituṃ sakkā.
- **Lekhacchinnāni:** Model anumānitāni Jāpāna-lekhacchinnāni nikkhāmeti.
- **Kālamuddā ca subtitles ca:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Dīgha-file-saṅkhāra:** Dīghā audio-video-file pi saṅkhārituṃ sakkā.
- **Google Drive upatthambho:** File sakkhiṃ upload karotha vā Google Drive tato paṭhatha; output ZIP icchāya Drive majjhe ṭhapetuṃ sakkā.
- **Anekāni output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP ca.

## Upayogavidhi

1. **1. Settings** majjhe `INPUT_MODE` gaṇhatha, aññā settings payojane sati parivattetha.
2. **Runtime → Run all** gaṇhatha.
3. `INPUT_MODE = "upload"` sati, **2. File selection / Google Drive mount** majjhe file gaṇhatha.
4. Saṅkhārassa pacchā output ZIP sayameva download hoti.

## Timestamp modes

- `none`: kāla-sūcanā natthi.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Dīghā file

`CHUNK_SECONDS` dīgha-file atthaṃ upayutta-internal-chunk dīghattaṃ niyameti. Mahantā values boundaries appaṃ karonti, bahu context dhārenti, atha kho ekaṃ ekaṃ inference garutaraṃ hoti, bahu GPU memory gaṇhituṃ sakkoti. Khuddakā values inference lahukaṃ karonti, atha kho bahu boundaries janenti; tesu ṭhānesu recognition pīḷetuṃ sakkā. Bahūsu kālesu default seṭṭho.

## Lokalīkato UI

ASR model sayaṃ **Jāpāna-bhāsāya eva**. README ca Colab UI ca localization sabbā **183 active ISO 639 Set 1 languages** āvarati (`sh` purāṇaṃ apanetvā).

Aṅgila-bhāsā (`en`) canonical translation source hoti. Jāpāna-bhāsā (`ja`) reviewed translation hoti, repository-mūle default `README.md` dassanatthaṃ likhīyati. Mūla-Japanese README **translation source na hoti**. Aññā 181 locales Aṅgila-bhāsāto machine-translate honti.

## Sallakkhaṇā

- GPU abhāve notebook transcription pubbe tiṭṭhati.
- Processing time input-dīghatta, settings, Colab-dinna GPU ca nissāya hoti. Paṭhama-run majjhe NeMo ca pamāṇena 1.23 GB model ca download honti.
- Dīgha-audio internal chunks majjhe saṅkhāriyati, tasmā chunk boundaries samīpe recognition pīḷetuṃ sakkā.

## Canonical source ca generation ca

Anuvādetabbā canonical sources:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot hoti. Jāpāna reviewed translation rūpena `locales/ja.json` majjhe rakkhīyati, tassa README snapshot mūla `README.md` majjhe likhīyati.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance sāmañña-CI tato visuṃ hoti. Sāmañña-users ca CI ca translation credentials na icchanti.

## License

Notebook scaffolding ca build/check scripts ca MIT license yuttā. Third Intelligence model idha puna na vitariyati, **Apache-2.0** anugataṃ. Third-party dependencies attano licenses dhārenti.
