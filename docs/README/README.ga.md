# Haas Japanese Colab

Leabhar nótaí Google Colab chun fuaim agus físeán Seapánach a thras-scríobh le Third Intelligence **Haas-ja-v1.0**.

[![Oscail in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ga.ipynb)

## Gnéithe

- **Saor in aisce:** Ritheann sé ar runtime GPU saor in aisce Google Colab.
- **ASR Seapánach:** Úsáideann sé [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), samhail thart ar 0.6B paraiméadar le haghaidh aithint cainte Seapánaí.
- **Tapa:** Is féidir an tras-scríobh a phróiseáil go tapa.
- **Poncaíocht:** Aschuireann an tsamhail poncaíocht mheasta Seapánach.
- **Stampaí ama agus fotheidil:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Próiseáil comhad fada:** Is féidir comhaid fhada fuaime agus físe a phróiseáil freisin.
- **Tacaíocht Google Drive:** Uaslódáil comhaid go díreach nó léigh iad ó Google Drive; is féidir an ZIP aschuir a shábháil go Drive más mian leat.
- **Aschuir iolracha:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest agus ZIP.

## Úsáid

1. Roghnaigh `INPUT_MODE` in **1. Settings** agus coigeartaigh socruithe eile más gá.
2. Roghnaigh **Runtime → Run all**.
3. Le `INPUT_MODE = "upload"`, roghnaigh comhaid in **2. File selection / mount Google Drive**.
4. Íoslódáiltear an ZIP aschuir go huathoibríoch tar éis na próiseála.

## Módanna stampa ama

- `none`: gan aon fhaisnéis ama.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Díchódóir

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Comhaid fhada

Rialaíonn `CHUNK_SECONDS` fad inmheánach an chunk a úsáidtear do chomhaid fhada. Laghdaíonn luachanna níos mó teorainneacha agus coinníonn siad níos mó comhthéacs, ach déanann siad gach inference níos troime agus d’fhéadfadh siad níos mó cuimhne GPU a úsáid. Déanann luachanna níos lú gach inference níos éadroime ach cruthaíonn siad níos mó teorainneacha, rud a d’fhéadfadh tionchar a imirt ar aithint timpeall na bpointí sin. Moltar an luach réamhshocraithe i bhformhór na gcásanna.

## Comhéadan logánaithe

Tá an tsamhail ASR féin **don tSeapáinis amháin**. Clúdaíonn logánú README agus UI Colab na **183 teanga ghníomhacha ISO 639 Set 1** ar fad (`sh` atá as feidhm eisiata).

Is é an Béarla (`en`) an fhoinse chanónach aistriúcháin. Is aistriúchán athbhreithnithe í an tSeapáinis (`ja`) agus cóipeáiltear í chuig fréamh an stóir mar an cur i láthair réamhshocraithe `README.md`. Ní úsáidtear README Seapánach na fréimhe **mar fhoinse aistriúcháin**. Aistrítear na 181 locale eile go huathoibríoch ón mBéarla.

## Nótaí

- Stopann an leabhar nótaí roimh an tras-scríobh mura bhfuil GPU ar fáil.
- Braitheann an t-am próiseála ar fhad an ionchuir, ar na socruithe agus ar an GPU a shannann Colab. Íoslódálann an chéad rith NeMo agus an tsamhail thart ar 1.23 GB freisin.
- Próiseáiltear fuaim fhada i chunks inmheánacha, mar sin d’fhéadfadh tionchar a bheith ar aithint timpeall teorainneacha chunk.

## Foinse chanónach agus giniúint

Foinsí canónacha is féidir a aistriú:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Is é `locales/en.json` an snapshot canónach sioncronaithe. Coinnítear an tSeapáinis mar aistriúchán athbhreithnithe in `locales/ja.json`, agus cóipeáiltear a snapshot README chuig `README.md` sa fhréamh.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Tá cothabháil aistriúcháin ar leithligh ó ghnáth-CI. Ní bhíonn dintiúir aistriúcháin de dhíth ar ghnáthúsáideoirí ná ar CI.

## Ceadúnas

Tá creat an leabhair nótaí agus na scripteanna build/check faoi cheadúnas MIT. Ní athdháiltear an tsamhail Third Intelligence anseo agus rialaítear í faoi **Apache-2.0**. Coinníonn spleáchais tríú páirtí a gceadúnais féin.
