# Haas Japanese Colab

Ko ha Google Colab notebook ke liliu ʻa e Japanese audio mo e video ki he text ʻaki ʻa e Third Intelligence **Haas-ja-v1.0**.

[![Fakaava ʻi Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_to.ipynb)

## Ngaahi meʻa ʻoku malava

- **Taʻetotongi:** ʻOku lele ʻi he GPU runtime taʻetotongi ʻa Google Colab.
- **Japanese ASR:** ʻOku ngāue ʻaki ʻa e [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), ko ha model ʻoku meimei 0.6B-parameter ki he Japanese speech recognition.
- **Vave:** ʻE lava ke process vave ʻa e transcription.
- **Punctuation:** ʻOku output ʻe he Model ʻa e Japanese punctuation ʻoku fakafuofuaʻi.
- **Timestamp mo subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** ʻE lava foki ke process ʻa e audio mo e video file lōloa.
- **Google Drive support:** Upload fakahangatonu ʻa e file pe lau mei Google Drive; ʻe lava ke save ʻa e output ZIP ki Drive kapau ʻe fili.
- **Output kehekehe:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, mo ZIP.

## Founga ngāue

1. Fili ʻa e `INPUT_MODE` ʻi he **1. Settings** pea liliu ʻa e setting kehe kapau ʻoku fie maʻu.
2. Fili ʻa e **Runtime → Run all**.
3. Kapau `INPUT_MODE = "upload"`, fili ʻa e file ʻi he **2. File selection / Google Drive mount**.
4. ʻI he ʻosi ʻa e processing, ʻe download fakangāue pē ʻa e output ZIP.

## Timestamp modes

- `none`: ʻoku ʻikai ha timing information.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File lōloa

ʻOku puleʻi ʻe `CHUNK_SECONDS` ʻa e lōloa ʻo e internal chunk ʻoku ngāue ʻaki ki he file lōloa. ʻOku fakasiʻisiʻi ʻe he value lalahi ʻa e boundary pea tauhi ʻa e context lahi ange, ka ʻoku mamafa ange ʻa e inference takitaha pea ʻe lava ke lahi ange ʻa e GPU memory. ʻOku maʻamaʻa ange ʻa e inference ʻi he value siʻisiʻi, ka ʻoku faʻu boundary lahi ange, ʻa ia ʻe lava ke uesia ʻa e recognition ʻi he ngaahi feituʻu ko iá. ʻOku fokotuʻu ʻa e default ʻi he ngaahi tuʻunga lahi.

## UI kuo fakaliliu

Ko e ASR model pē ʻoku **Japanese-only**. ʻOku kāpui ʻe he README mo e Colab UI localization ʻa e **183 active ISO 639 Set 1 languages** kotoa (ʻikai kau ʻa e deprecated `sh`).

Ko English (`en`) ʻa e canonical translation source. Ko Japanese (`ja`) ko ha reviewed translation pea ʻoku copy ki he repository root ko e default `README.md` presentation. Ko e root Japanese README ʻoku **ʻikai ngāue ʻaki** ko ha translation source. Ko e 181 locale kehe ʻoku machine-translated mei English.

## Ngaahi fakatokanga

- ʻOku tuʻu ʻa e notebook kimuʻa ʻi he transcription kapau ʻoku ʻikai ha GPU.
- ʻOku fakafalala ʻa e processing time ki he lōloa ʻo e input, setting, mo e GPU ʻoku ʻoatu ʻe Colab. ʻI he run ʻuluaki ʻoku download foki ʻa e NeMo mo e model ʻoku meimei 1.23 GB.
- ʻOku process ʻa e audio lōloa ʻi he internal chunks, ko ia ʻe lava ke uesia ʻa e recognition ʻi he chunk boundaries.

## Canonical source mo generation

Maʻuʻanga fakavae ʻe lava ke liliu lea:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Ko `locales/en.json` ʻa e synchronized canonical snapshot. ʻOku tauhi ʻa e Japanese ko ha reviewed translation ʻi he `locales/ja.json`, pea ʻoku copy hono README snapshot ki he root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

ʻOku kehe ʻa e translation maintenance mei he ordinary CI. ʻOku ʻikai fie maʻu ʻe he ordinary users mo CI ha translation credentials.

## License

Ko e notebook scaffolding mo e build/check scripts ʻoku MIT licensed. ʻOku ʻikai redistributed heni ʻa e Third Intelligence model pea ʻoku puleʻi ʻe he **Apache-2.0**. ʻOku tauhi ʻe he third-party dependencies honau licenses.
