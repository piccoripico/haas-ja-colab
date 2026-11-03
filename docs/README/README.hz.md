# Haas Japanese Colab

Google Colab notebook yokutjanga ombepo na video yOrujapani mombapira nomurungu Third Intelligence **Haas-ja-v1.0**.

[![Tjita mOColab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_hz.ipynb)

## Ovitjitwa

- **Pehe omuriro:** I tjita moGPU runtime ya Google Colab i ri free.
- **ASR yOrujapani:** I rihonga [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model i na 0.6B parameters pupepi, yokuzuva orutjanga rOrujapani.
- **Ombangu:** Transcription i tjitwa nombangu.
- **Ovimanyise vyokutjanga:** Model i raisa ovimanyise vyOrujapani mbi i panga.
- **Timestamps na subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Omafile mare:** Audio na video file mare mavi tjitwa wo.
- **Google Drive:** Upload omafile pehi, poo u lese okuza moGoogle Drive; output ZIP i vanga okuserurwa moDrive.
- **Output ozondjuwo:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Okurihonga okutjita

1. Tora `INPUT_MODE` mo **1. Settings** nu handja ozondunge zarwe nge ziri muhimu.
2. Tora **Runtime → Run all**.
3. Nge `INPUT_MODE = "upload"`, tora omafile mo **2. File selection / Google Drive mount**.
4. Output ZIP i download-ewa yovene kombunda yokutjita.

## Timestamp modes

- `none`: kape na timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Omafile mare

`CHUNK_SECONDS` i pangura oure wointernal chunk u tjitwa koma file mare. Oma value mare mapeza boundaries nu mavi kara na context ondji, nungwari inference imwe na imwe i vara nu i vanga GPU memory ondji. Oma value matiti mavi tjita inference i rire pehi, nungwari mavi tjita boundaries ozondji, mbi mavi tjita recognition i handjuke popezu nombanda. Default i ri mbi tjipura kovitjitwa ovindji.

## UI yoviperendero

ASR model yovene eye **Orujapani uriri**. README na Colab UI localization i komba **ozondimi 183 active ISO 639 Set 1** (`sh` yakara omukuru kai ri mo).

Oruingirisi (`en`) eye canonical translation source. Orujapani (`ja`) eye reviewed translation nu i kopiwa koroot ya repository nga default `README.md`. Root Japanese README **kai tjitwa** translation source. Ozolocale 181 zarwe mavi machine-translate okuza mOruingirisi.

## Omatjangwa

- Notebook i yema kutenga transcription nge GPU kai ri po.
- Processing time i ri koure woinput, settings, na GPU ya Colab i kupa. Mo run yotenga, NeMo na model ya 1.23 GB pupepi i download-ewa wo.
- Audio ire i tjitwa mointernal chunks, okutja recognition i handjuke pupepi na chunk boundaries.

## Canonical source na generation

Ovinyakurwa vyokutja mbi mavi tjindjwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` eye synchronized canonical snapshot. Orujapani ru serurwa nga reviewed translation mo `locales/ja.json`, nu README snapshot yarwo i kopiwa koroot `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance i ri oruveze rwarwo okuza koordinary CI. Ordinary users na CI kave vanga translation credentials.

## License

Notebook scaffolding na build/check scripts ziri MIT licensed. Third Intelligence model kai redistributewa mba nu i ri mongamburiro ya **Apache-2.0**. Third-party dependencies mavi kara na licenses zawo.
