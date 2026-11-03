# Haas Japanese Colab

Commentarium Google Colab ad sonum et imagines moventes Iaponicas transcribendas cum Third Intelligence **Haas-ja-v1.0**.

[![Aperi in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_la.ipynb)

## Proprietates

- **Gratis:** In gratuito GPU runtime Google Colab currit.
- **ASR Iaponicum:** Utitur [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), exemplo circiter 0.6B parametrorum ad sermonem Iaponicum agnoscendum.
- **Celer:** Transscriptio celeriter tractari potest.
- **Interpunctio:** Exemplum interpunctuationem Iaponicam aestimatam producit.
- **Notae temporis et subtituli:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Tractatio fasciculorum longorum:** Fasciculi sonori et video longi quoque tractari possunt.
- **Google Drive adiumentum:** Fasciculos directe mitte aut eos ex Google Drive lege; ZIP exitus pro arbitrio in Drive servari potest.
- **Exitus multiplices:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, et ZIP.

## Usus

1. Elige `INPUT_MODE` in **1. Configurationes** et alias configurationes, si opus est, compone.
2. Elige **Runtime → Run all**.
3. Cum `INPUT_MODE = "upload"`, fasciculos in **2. Electio fasciculorum / coniunctio Google Drive** elige.
4. ZIP exitus post tractationem perfectam automatice deponitur.

## Modi notarum temporis

- `none`: nulla informatio temporis.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificator

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fasciculi longi

`CHUNK_SECONDS` durationem partium internarum pro fasciculis longis regit. Valores maiores fines partium minuunt et plus contextus servant, sed unaquaeque inferentia gravior est et plus memoriae GPU uti potest. Valores minores inferentiam leviorem faciunt sed plures fines creant, qui agnitionem circa eos locos afficere possunt. Valor praedefinitus in plurimis casibus commendatur.

## Interfacies localizata

Exemplum ASR ipsum **solum Iaponicum** est. Localizatio README et interfaciei Colab omnes **183 linguas activas ISO 639 Set 1** complectitur (`sh` obsoleta exclusa).

Anglica (`en`) est fons translationis canonicus. Iaponica (`ja`) est translatio recognita et ad radicem repositorii ut praesentatio praedefinita `README.md` copiatur. README Iaponicum radicis **non** ut fons translationis adhibetur. Reliquae 181 locales machinaliter ex Anglica transferuntur.

## Notae

- Commentarium ante transcriptionem subsistit si GPU praesto non est.
- Tempus tractationis a longitudine input, configurationibus, et GPU a Colab assignata pendet. Prima executio etiam NeMo et exemplum circiter 1.23 GB deponit.
- Sonus longus in partes internas tractatur, itaque agnitio circa fines partium affici potest.

## Fons canonicus et generatio

Fontes canonici transferibiles:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` est imago canonica synchronizata. Iaponica ut translatio recognita in `locales/ja.json` conservatur, eiusque imago README ad radicem `README.md` copiatur.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Conservatio translationum a CI ordinaria separata est. Usoribus ordinariis et CI documenta secreta translationis non opus sunt.

## Licentia

Structura commentarii et scripta build/check licentia MIT reguntur. Exemplum Third Intelligence hic non redistribuitur et **Apache-2.0** regitur. Dependentiae tertiarum partium suas licentias servant.
