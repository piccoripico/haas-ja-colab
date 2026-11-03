# Haas Japanese Colab

Akwụkwọ Google Colab maka ịtụgharị ọdịyo na vidiyo Japanese gaa ederede site na Third Intelligence **Haas-ja-v1.0**.

[![Mepee na Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ig.ipynb)

## Njirimara

- **N’efu:** Ọ na-agba na runtime GPU n’efu nke Google Colab.
- **ASR Japanese:** Ọ na-eji [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model nwere ihe dị ka 0.6B parameters maka ịmata okwu Japanese.
- **Ngwa ngwa:** Enwere ike ịhazi transcription ngwa ngwa.
- **Akara edemede:** Model na-ewepụta akara edemede Japanese a tụrụ anya ya.
- **Timestamps na subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Nhazi faịlụ ogologo:** A pụkwara ịhazi faịlụ ọdịyo na vidiyo ogologo.
- **Nkwado Google Drive:** Bulite faịlụ ozugbo ma ọ bụ gụọ ha site na Google Drive; enwere ike ịchekwa output ZIP na Drive ma ọ bụrụ na achọrọ.
- **Outputs ọtụtụ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest na ZIP.

## Ojiji

1. Họrọ `INPUT_MODE` na **1. Settings** ma gbanwee settings ndị ọzọ ma ọ bụrụ na ọ dị mkpa.
2. Họrọ **Runtime → Run all**.
3. Mgbe `INPUT_MODE = "upload"`, họrọ faịlụ na **2. File selection / mount Google Drive**.
4. A na-ebudata output ZIP n’onwe ya mgbe nhazi gasịrị.

## Ụdị timestamp

- `none`: enweghị ozi oge.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Faịlụ ogologo

`CHUNK_SECONDS` na-achịkwa ogologo internal chunk eji maka faịlụ ogologo. Values ka ukwuu na-ebelata boundaries ma na-edobe context karịa, mana inference ọ bụla na-adị arọ karị ma nwee ike iji memory GPU karịa. Values pere mpe na-eme inference ọ bụla mfe karị mana na-emepụta boundaries karịa, nke nwere ike imetụta recognition n’akụkụ ebe ndị ahụ. A na-atụ aro default value n’ọtụtụ ọnọdụ.

## UI e mere ka ọ dabara asụsụ

Model ASR n’onwe ya bụ **naanị Japanese**. Localization nke README na Colab UI na-ekpuchi **asụsụ 183 niile dị ndụ nke ISO 639 Set 1** (`sh` ochie ewepụla).

Bekee (`en`) bụ canonical translation source. Japanese (`ja`) bụ translation a nyochachara ma a na-edetuo ya na repository root dị ka default presentation `README.md`. Japanese README dị na root **anaghị eji ya dị ka translation source**. Locale 181 ndị ọzọ bụ machine translation sitere na Bekee.

## Nkọwa

- Notebook na-akwụsị tupu transcription ma ọ bụrụ na GPU adịghị.
- Oge nhazi dabere na ogologo input, settings na GPU Colab kenyere. First run na-ebudata NeMo na model ihe dị ka 1.23 GB kwa.
- A na-ahazi audio ogologo n’ime internal chunks, ya mere recognition nwere ike imetụta n’akụkụ chunk boundaries.

## Canonical source na generation

Canonical sources enwere ike ịtụgharị:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` bụ synchronized canonical snapshot. A na-elekọta Japanese dị ka reviewed translation na `locales/ja.json`, a na-edetuo snapshot README ya na root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Nlekọta translation dị iche na CI nkịtị. Ndị ọrụ nkịtị na CI achọghị translation credentials.

## License

Notebook scaffolding na build/check scripts dị n’okpuru license MIT. Model Third Intelligence anaghị ekesa ọzọ ebe a ma nọ n’okpuru **Apache-2.0**. Third-party dependencies na-edobe licenses nke ha.
