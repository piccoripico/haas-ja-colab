# Haas Japanese Colab

Wan Google Colab notebook blong transkribem Japanees audio mo video wetem Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_bi.ipynb)

## Ol fetsa

- **Fri:** I ron long fri GPU runtime blong Google Colab.
- **Japanees ASR:** I yusum [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), wan model blong raon 0.6B parameter blong luksave Japanees toktok.
- **Fast:** Transkripsen i save prosese kwiktaem.
- **Punctuation:** Model i givim estimated Japanees punctuation.
- **Timestamp mo subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Prosese longfala fael:** Longfala audio mo video fael tu oli save prosese.
- **Google Drive sapot:** Uploadem fael stret o ridim olgeta long Google Drive; yu save sevem output ZIP long Drive sapos yu wantem.
- **Plante output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, mo ZIP.

## Hao blong yusum

1. Jusum `INPUT_MODE` long **1. Settings** mo jenisim narafala setting sapos i nid.
2. Jusum **Runtime → Run all**.
3. Sapos `INPUT_MODE = "upload"`, jusum ol fael long **2. File selection / Google Drive mount**.
4. Output ZIP bae i download otomatik afta processing i finis.

## Ol timestamp mode

- `none`: no gat timing infomesen.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Longfala fael

`CHUNK_SECONDS` i kontrolem internal chunk duration blong longfala fael. Bigfala value i katemdaon ol boundary mo i holem moa context, be i mekem wanwan inference i hevi moa mo i save yusum moa GPU memory. Smol value i mekem inference i laet moa be i mekem moa boundary, we i save afektem recognition klosap long ol point ia. Long plante kes default hemi best.

## UI long lokol lanwis

ASR model hem wan i **blong Japanees nomo**. README mo Colab UI localization i kavremap olgeta **183 active ISO 639 Set 1 lanwis** (oli no inkludum deprecated `sh`).

Inglis (`en`) hemi canonical translation source. Japanees (`ja`) hemi wan reviewed translation mo oli kopi i go long root blong repository olsem default `README.md` presentation. Root Japanees README **oli no yusum olsem translation source**. Ol narafala 181 locale oli machine-translate olgeta long Inglis.

## Ol not

- Notebook i stop bifo transcription sapos GPU i no stap.
- Processing taem i dipen long input length, setting, mo GPU we Colab i givim. Fas run tu i downloadem NeMo mo model blong raon 1.23 GB.
- Longfala audio oli prosese long internal chunk, mekem se recognition i save afek klosap long chunk boundary.

## Canonical source mo generation

Ol canonical source we oli save translate:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` hemi synchronized canonical snapshot. Japanees oli maintainem olsem reviewed translation long `locales/ja.json`, mo README snapshot blong hem oli kopi i go long root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance i seperet long ordinary CI. Ordinary user mo CI oli no nidim translation credential.

## License

Notebook scaffolding mo build/check script oli MIT licensed. Third Intelligence model oli no redistribute long ples ia mo hemi stap aninit long **Apache-2.0**. Third-party dependency oli holem own license blong olgeta.
