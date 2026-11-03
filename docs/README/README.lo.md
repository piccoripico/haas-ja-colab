# Haas Japanese Colab

Notebook Google Colab ສຳລັບຖອດສຽງແລະວິດີໂອພາສາຍີ່ປຸ່ນດ້ວຍ Third Intelligence **Haas-ja-v1.0**.

[![ເປີດໃນ Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_lo.ipynb)

## ຄຸນສົມບັດ

- **ຟຣີ:** ເຮັດວຽກເທິງ GPU runtime ຟຣີຂອງ Google Colab.
- **ASR ພາສາຍີ່ປຸ່ນ:** ໃຊ້ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model ປະມານ 0.6B parameters ສຳລັບຮັບຮູ້ສຽງພາສາຍີ່ປຸ່ນ.
- **ໄວ:** ສາມາດ process transcription ໄດ້ຢ່າງໄວ.
- **ເຄື່ອງໝາຍວັກຕອນ:** Model ສົ່ງອອກເຄື່ອງໝາຍວັກຕອນພາສາຍີ່ປຸ່ນທີ່ຄາດຄະເນ.
- **Timestamps ແລະ subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ປະມວນຜົນໄຟລ໌ຍາວ:** ສາມາດ process audio ແລະ video ໄຟລ໌ຍາວໄດ້.
- **ຮອງຮັບ Google Drive:** Upload ໄຟລ໌ໂດຍກົງ ຫຼືອ່ານຈາກ Google Drive; output ZIP ສາມາດ save ໄປ Drive ໄດ້ຕາມຕ້ອງການ.
- **Output ຫຼາຍຮູບແບບ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ແລະ ZIP.

## ວິທີໃຊ້

1. ເລືອກ `INPUT_MODE` ໃນ **1. Settings** ແລະປັບ settings ອື່ນຖ້າຈຳເປັນ.
2. ເລືອກ **Runtime → Run all**.
3. ເມື່ອ `INPUT_MODE = "upload"`, ເລືອກໄຟລ໌ໃນ **2. File selection / Google Drive mount**.
4. Output ZIP ຈະ download ອັດຕະໂນມັດຫຼັງ process ສຳເລັດ.

## Timestamp modes

- `none`: ບໍ່ມີຂໍ້ມູນເວລາ.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ໄຟລ໌ຍາວ

`CHUNK_SECONDS` ຄວບຄຸມໄລຍະ internal chunk ສຳລັບໄຟລ໌ຍາວ. ຄ່າໃຫຍ່ຂຶ້ນຫຼຸດ boundaries ແລະຮັກສາ context ໄດ້ຫຼາຍ, ແຕ່ແຕ່ລະ inference ໜັກຂຶ້ນ ແລະອາດໃຊ້ GPU memory ຫຼາຍ. ຄ່ານ້ອຍລົງເຮັດ inference ເບົາລົງ ແຕ່ສ້າງ boundaries ຫຼາຍ, ຊຶ່ງອາດກະທົບ recognition ບໍລິເວນນັ້ນ. ແນະນຳ default value ໃນກໍລະນີສ່ວນໃຫຍ່.

## UI ທີ່ແປເປັນພາສາທ້ອງຖິ່ນ

ASR model ຕົວມັນເອງແມ່ນ **ພາສາຍີ່ປຸ່ນເທົ່ານັ້ນ**. README ແລະ Colab UI localization ຄອບຄຸມທັງ **183 active ISO 639 Set 1 languages** (`sh` deprecated ຖືກຕັດອອກ).

English (`en`) ແມ່ນ canonical translation source. Japanese (`ja`) ແມ່ນ reviewed translation ແລະຖືກ copy ໄປ repository root ເປັນ default `README.md` presentation. Root Japanese README **ບໍ່ໃຊ້ເປັນ translation source**. ອີກ 181 locales ແມ່ນ machine-translated ຈາກ English.

## ໝາຍເຫດ

- Notebook ຢຸດກ່ອນ transcription ຖ້າ GPU ບໍ່ມີ.
- Processing time ຂຶ້ນກັບ input length, settings, ແລະ GPU ທີ່ Colab ຈັດໃຫ້. ຮອບທຳອິດຍັງ download NeMo ແລະ model ປະມານ 1.23 GB.
- Audio ຍາວ process ເປັນ internal chunks, ດັ່ງນັ້ນ recognition ອາດຖືກກະທົບໃກ້ chunk boundaries.

## Canonical source ແລະ generation

Canonical sources ທີ່ແປໄດ້:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ແມ່ນ synchronized canonical snapshot. Japanese ຖືກຮັກສາເປັນ reviewed translation ໃນ `locales/ja.json`, ແລະ README snapshot ຂອງມັນຖືກ copy ໄປ root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ແຍກຈາກ CI ປົກກະຕິ. Users ປົກກະຕິ ແລະ CI ບໍ່ຕ້ອງມີ translation credentials.

## License

Notebook scaffolding ແລະ build/check scripts ແມ່ນ MIT licensed. Third Intelligence model ບໍ່ redistribute ຢູ່ນີ້ ແລະຢູ່ພາຍໃຕ້ **Apache-2.0**. Third-party dependencies ຮັກສາ licenses ຂອງຕົນ.
