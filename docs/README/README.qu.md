# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** nisqawan Japonés audio video-ta qillqaman tikraypaq Google Colab notebook.

[![Colab-pi kichay](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_qu.ipynb)

## Imakunata ruwan

- **Mana qullqipaq:** Google Colab-pa mana qullqiyuq GPU runtime-ninpi purin.
- **Japonés ASR:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) nisqata llamk'achin; Japonés rimayta riqsiyapaq 0.6B-parameter hina model-mi.
- **Utqay:** Transcription utqaylla process-kuyta atin.
- **Punctuation:** Model Japonés punctuation nisqata yuyasqanman hina output-rin.
- **Timestamp subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Unay file processing:** Unay audio video file-kunatapas process-kuyta atin.
- **Google Drive support:** File-ta chiqap upload-y, utaq Google Drive-manta ñawiriy; output ZIP-ta munaspa Drive-pi save-yta atin.
- **Achka output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## Imayna llamk'achiy

1. **1. Settings** nisqapi `INPUT_MODE` akllay, hinaspa munaspa huk setting-kunata tikray.
2. **Runtime → Run all** akllay.
3. `INPUT_MODE = "upload"` kaptin, **2. File selection / Google Drive mount** nisqapi file-ta akllay.
4. Processing tukukuptin output ZIP kikinmanta download-kun.

## Timestamp modes

- `none`: mana timing information kanchu.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Unay file-kuna

`CHUNK_SECONDS` unay file-kunapaq internal chunk-paq hayk'a unay kayninta kamachin. Hatun value-kuna boundary-ta pisiyachinku, aswan context-ta waqaychanku, ichaqa sapa inference aswan llasaqmi, GPU memory-ta aswan llamk'achinman. Huch'uy value-kuna sapa inference-ta pisiyachinku, ichaqa achka boundary-ta ruwanku, chayqa chay chiqakunapi recognition-ta wakllichinman. Achka kutipi default nisqa allinmi.

## Simi-man tikrasqa UI

ASR model kikinqa **Japanese-only**. README Colab UI localization tukuy **183 active ISO 639 Set 1 languages**-ta qarin (deprecated `sh` mana yupasqa).

English (`en`) canonical translation source-mi. Japanese (`ja`) reviewed translation-mi, repository root-man default `README.md` presentation hina copy-kun. Root Japanese README-ta translation source hina **mana llamk'achinchikchu**. Huk 181 locale-kuna English-manta machine-translated kanku.

## Yuyachiykuna

- GPU mana kaptin notebook transcription manaraq qallarispa sayan.
- Processing time input-pa unaynin, setting, Colab-pa GPU qusqanman hina tikrakun. Ñawpaq run-pi NeMo-ta, 1.23 GB hina model-tapas download-n.
- Unay audio internal chunks-pi process-kun, chayrayku chunk boundary-kuna qayllapi recognition wakllinman.

## Canonical source generation

Tikray atina ñawpaq pukyukuna:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` synchronized canonical snapshot-mi. Japanese `locales/ja.json` ukupi reviewed translation hina waqaychasqa, README snapshot-nin root `README.md`-man copy-kun.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance ordinary CI-manta sapanmi. Ordinary user-kuna CI-pas mana translation credentials-ta munankuchu.

## License

Notebook scaffolding build/check scripts MIT licensed kanku. Third Intelligence model kaypi mana redistributed-chu, **Apache-2.0** kamachisqanman hina. Third-party dependencies kikin licenses-ninkuta waqaychanku.
