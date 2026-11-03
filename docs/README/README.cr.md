# Haas Japanese Colab

Google Colab masinahikan kā-āpacihcikātēk ta-masinahikātēk Japan pīkiskwēwin audio ēkwa video, Third Intelligence **Haas-ja-v1.0** ē-āpacihcikātēk.

[![Pōni Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_cr.ipynb)

## Kēkwāna ē-isi-wīcihikoyan

- **Mōniyāw-wīcihiwēwin namōya pakitinikēwin:** Google Colab free GPU runtime ohci pimipahtāw.
- **Japan ASR:** Āpacihcikātēw [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), nīkān 0.6B parameter model Japan pīkiskwēwin ta-masinahikātēk.
- **Kīskwē:** Masinahikēwin kīskwē pimipahtāw.
- **Punctuation:** Model kīhtwām Japan masinahikan-pīkonāna pakitinam.
- **Timestamps ēkwa subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Kinwēs file:** Kinwēs audio ēkwa video files wīhkāc pimipahtāwak.
- **Google Drive:** Files pakitinam ēkwa Google Drive ohci ayamiha; output ZIP kīspin nawac kici-wīcihikoyan Drive itē kanawēyihcikātēw.
- **Mīna output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ēkwa ZIP.

## Tānisī ta-āpacihcikātēk

1. Wiyasiwe `INPUT_MODE` **1. Settings** itē, ēkwa kotaka settings mīna māci-kiskinwahamākēwin ispihk.
2. Wiyasiwe **Runtime → Run all**.
3. Kīspin `INPUT_MODE = "upload"`, wiyasiwe files **2. File selection / Google Drive mount** itē.
4. Ē-isi-kīsi-pimipahtāk, output ZIP piko download-ikātēw.

## Timestamp modes

- `none`: namōya timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Kinwēs files

`CHUNK_SECONDS` wiyasiwe tānisi kinwēs internal chunk ta-ispayik. Isko values kiciwāw boundaries wanawēyihcikātēwa ēkwa context nawac kanawēyihcikātēw, māka papēyak inference nawac kici ēkwa GPU memory nawac āpacihcikātēw. Apisis values papēyak inference wāwīcihiwēw, māka nawac boundaries osihcikātēwa ēkwa recognition piko ta-isi-mācihōw anima itē. Default miywāsin mistahi ispihk.

## Pīkiskwēwin UI

ASR model **Japan pīkiskwēwin piko** kiskinwahamākēw. README ēkwa Colab UI pīkiskwēwina kiskinwahamākēwin misiwē **183 active ISO 639 Set 1 languages** (`sh` kā-deprecated namōya pīhtokwēw).

English (`en`) canonical translation source. Japanese (`ja`) reviewed translation ēkwa repository root itē iskwēw default `README.md`. Root Japanese README **namōya** translation source. Kotaka 181 locales machine-translated English ohci.

## Kiskinwahamākēwina

- Notebook pōniw transcription oskāci kīspin GPU namōya ihtakon.
- Processing time takwām input kinwēs, settings, ēkwa GPU kā-miyikowisiw Google Colab ohci. Nistam run ispihk, NeMo ēkwa nīkān 1.23 GB model download-ikātēwa.
- Kinwēs audio internal chunks itē pimipahtāw, ēkwa recognition piko mācihōw chunk boundaries itē.

## Canonical source ēkwa generation

Kā-kīskimōcikātēki nistam-otinamākēwina:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot. Japanese reviewed translation `locales/ja.json` itē kanawēyihcikātēw, ēkwa README snapshot root `README.md` itē kopī-ikātēw.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance pākosīsiw ordinary CI ohci. Ordinary users ēkwa CI namōya translation credentials nitawēyimēwak.

## License

Notebook scaffolding ēkwa build/check scripts MIT licensed. Third Intelligence model namōya oma osihcikātēw ēkwa **Apache-2.0** ohci wiyasiwēwin. Third-party dependencies kanawēyimēwak tipēyimisowin licenses.
