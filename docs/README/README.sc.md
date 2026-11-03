# Haas Japanese Colab

Notebook Google Colab pro trascrìere àudio e vìdeo giaponesos cun Third Intelligence **Haas-ja-v1.0**.

[![Aberi in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sc.ipynb)

## Caraterìsticas

- **Gràtzis:** Funtzionat in su runtime GPU gràtuis de Google Colab.
- **ASR giaponesu:** Imprea [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), unu modellu de circa 0.6B paràmetros pro su reconnoschimentu de sa boghe giaponesa.
- **Lestru:** Sa trascritzione podet èssere elaborada lestru.
- **Puntegiadura:** Su modellu produet puntegiadura giaponesa istimada.
- **Marcas de tempus e sutatìtulos:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Elaboratzione de archìvios longos:** Si podent elaborare fintzas archìvios àudio e vìdeo longos.
- **Suportu Google Drive:** Carrigade archìvios diretamente o legìdelos dae Google Drive; su ZIP de essida podet èssere sarvadu in Drive a isseberu.
- **Prus essidas:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Impreu

1. Isseberade `INPUT_MODE` in **1. Impostatziones** e acomodade àteras impostatziones si faghet mestieri.
2. Isseberade **Runtime → Run all**.
3. Cun `INPUT_MODE = "upload"`, isseberade archìvios in **2. Isseberu de archìvios / montàgiu Google Drive**.
4. Su ZIP de essida est iscarrigadu automaticamente a pustis chi s’elaboratzione est acabada.

## Modos de marcas de tempus

- `none`: peruna informatzione de tempus.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificadore

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Archìvios longos

`CHUNK_SECONDS` controllat sa durada de sos truncones internos impreaos pro archìvios longos. Balores prus mannos disminuint sos làcanos e mantenent prus cuntestu, ma onni inferèntzia est prus pesada e podet impreare prus memòria GPU. Balores prus piticos faghent onni inferèntzia prus lèbia ma creant prus làcanos, chi podent influentare su reconnoschimentu in giru a cussos puntos. Su balore predefinidu est cussigiadu in sa majoria de sos casos.

## Interfache localizada

Su modellu ASR in issoro est **isceti giaponesu**. Sa localizatzione de README e de s’interfache Colab coberrit totu sas **183 limbas ativas ISO 639 Set 1** (`sh` obsoletu escludidu).

S’inglesu (`en`) est sa fonte canònica de tradutzione. Su giaponesu (`ja`) est una tradutzione revisionada e est copiadu a sa ràdighe de su repositoriu comente presentatzione predefinida `README.md`. Su README giaponesu de ràdighe **no est** impreau comente fonte de tradutzione. Sos àteros 181 locales sunt tradùidos automaticamente dae s’inglesu.

## Notas

- Su notebook si firmat in antis de sa trascritzione si no b’at una GPU a disponimentu.
- Su tempus de elaboratzione dipendet dae sa longària de s’input, sas impostatziones e sa GPU assignada dae Colab. Sa prima esecutzione iscarrigat fintzas NeMo e su modellu de circa 1.23 GB.
- S’àudio longu est elaboradu in truncones internos, duncas su reconnoschimentu podet èssere influentzadu in giru a sos làcanos de truncone.

## Fonte canònica e generatzione

Fontes canònicas chi si podent tradùere:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` est su snapshot canònicu sincronizadu. Su giaponesu est mantènnidu comente tradutzione revisionada in `locales/ja.json`, e su snapshot README suo est copiadu a `README.md` in sa ràdighe.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Sa manutentzione de sas tradutziones est separada dae su CI ordinàriu. Utentes ordinàrios e CI no ant bisòngiu de credentziales de tradutzione.

## Lissèntzia

S’istrutura de su notebook e sos scripts build/check sunt sut a lissèntzia MIT. Su modellu Third Intelligence no est torra-distribuidu inoghe e est reguladu dae **Apache-2.0**. Sas dipendèntzias de tertzas partes mantenent sas lissèntzias issoro.
