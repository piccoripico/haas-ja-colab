# Haas Japanese Colab

Google Colab-notatbók til að umrita japanskt hljóð og myndskeið með Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_fo.ipynb)

## Eginleikar

- **Ókeypis:** Keyrir í ókeypis GPU-keyrsluumhverfi Google Colab.
- **Japanskt ASR:** Notar [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), líkan með um 0.6B færibreytum fyrir japanska talgreiningu.
- **Hratt:** Hægt er að vinna umritun hratt.
- **Greinarmerki:** Líkanið skilar áætluðum japönskum greinarmerkjum.
- **Tímastimplar og skjátextar:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Vinnsla langra skráa:** Einnig er hægt að vinna löng hljóð- og myndskeið.
- **Google Drive-stuðningur:** Hladdu skrám beint upp eða lestu þær úr Google Drive; hægt er að vista ZIP-úttak á Drive.
- **Mörg úttakssnið:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest og ZIP.

## Nýtsla

1. Veldu `INPUT_MODE` undir **1. Settings** og breyttu öðrum stillingum eftir þörfum.
2. Veldu **Runtime → Run all**.
3. Með `INPUT_MODE = "upload"` velurðu skrár undir **2. File selection / Google Drive mount**.
4. ZIP-úttakið er sjálfkrafa sótt þegar vinnslu lýkur.

## Tímastimplastillingar

- `none`: engar tímaupplýsingar.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Afkóðari

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Langar skrár

`CHUNK_SECONDS` stjórnar innri lengd bita fyrir langar skrár. Stærri gildi fækka mörkum og varðveita meira samhengi, en gera hverja ályktun þyngri og geta aukið GPU-minnisnotkun. Minni gildi létta hverja ályktun en búa til fleiri mörk sem geta haft áhrif á greiningu í kringum þau. Sjálfgefna gildið er mælt með í flestum tilvikum.

## Staðfært viðmót

ASR-líkanið sjálft er **eingöngu fyrir japönsku**. Staðfærsla README og Colab-viðmótsins nær yfir öll **183 virk ISO 639 Set 1 tungumál** (úrelt `sh` er undanskilið).

Enska (`en`) er kanóníski þýðingargjafinn. Japanska (`ja`) er yfirfarin þýðing og er afrituð í rót geymslunnar sem sjálfgefin `README.md` framsetning. Japanska README í rótinni er **ekki** notuð sem þýðingargjafi. Hin 181 locale eru vélþýdd úr ensku.

## Viðmerkingar

- Vinnubókin stöðvast fyrir umritun ef GPU er ekki tiltækt.
- Vinnslutími fer eftir lengd inntaks, stillingum og GPU sem Colab úthlutar. Fyrsta keyrsla sækir einnig NeMo og um 1.23 GB líkanið.
- Langt hljóð er unnið í innri bitum og því getur greining orðið fyrir áhrifum við bitamörk.

## Kanonisk kelda og gerð

Kanónískir þýðanlegir gjafar:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` er samstillta kanóníska snapshotið. Japanska er viðhaldið sem yfirfarin þýðing í `locales/ja.json`, og README-snapshot hennar er afritað í rótina sem `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Viðhald þýðinga er aðskilið frá venjulegu CI. Venjulegir notendur og CI þurfa ekki þýðingarskilríki.

## Leyfi

Uppbygging vinnubókarinnar og build-/athugunarskriftur eru MIT-leyfðar. Third Intelligence-líkanið er ekki endurdreift hér og lýtur **Apache-2.0**. Þriðju aðila háðir hlutir halda sínum eigin leyfum.
