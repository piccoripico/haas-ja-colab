# Haas Japanese Colab

Google Colab-notebooka mii čállá japánalaš jiena ja video teavsttasin Third Intelligence **Haas-ja-v1.0** bokte.

[![Raba Colab:s](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_se.ipynb)

## Iešvuođat

- **Nuvttá:** Doaibmá Google Colab nuvttá GPU-runtime:s.
- **Japánalaš ASR:** Geavaha [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), sullii 0.6B-paramihterat modealla japánalaš sáhkavuorru dovdama várás.
- **Jođán:** Transkripšuvdna sáhttá gieđahallojuvvot jođánit.
- **Čállinmearkkat:** Modealla addá árvvoštallon japánalaš čállinmearkkaid.
- **Áigemearkkat ja vuolleteavsttat:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Guhkes fiillaid gieđahallan:** Guhkes jietna- ja videofiillat sáhttet maid gieđahallojuvvot.
- **Google Drive doarjja:** Sádde fiillaid njuolga dahje loga daid Google Drive:s; bohtosa ZIP sáhttá háliidettiin vurkejuvvot Drive:i.
- **Máŋggalágan bohtosat:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest ja ZIP.

## Geavaheapmi

1. Vállje `INPUT_MODE` oasis **1. Heivehusat** ja rievdat eará heivehusaid jos dárbbašuvvo.
2. Vállje **Runtime → Run all**.
3. Go `INPUT_MODE = "upload"`, vállje fiillaid oasis **2. Fiilaválljen / Google Drive čatnan**.
4. Bohtosa ZIP láddejuvvo automáhtalaččat gieđahallama maŋŋá.

## Áigemearkka modusat

- `none`: ii atte áigedieđu.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Guhkes fiillat

`CHUNK_SECONDS` mearrida guhkes fiillaid siskkáldas chunk-guhkkodaga. Stuorát árvvut unnit čuohpadusaid ja seailluhit eanet konteavstta, muhto juohke inference šaddá lossat ja sáhttá geavahit eanet GPU-muittu. Unnit árvvut dahket juohke inference geahppaset, muhto ráhkadit eanet čuohpadusaid, mii sáhttá váikkuhit dovdamii daid báikkiid birra. Vuođđoárvu lea ávžžuhuvvon eanaš dilálašvuođain.

## Lokaliserrejuvvon geavaheaddjilakta

ASR-modealla ieš lea **dušše japánalaš**. README ja Colab UI lokaliseren gokčá buot **183 aktiivvalaš ISO 639 Set 1 giela** (boares `sh` ii leat mielde).

Eŋgelasgiella (`en`) lea kanonalaš jorgaluvvon gáldu. Japánagiella (`ja`) lea dárkkistuvvon jorgalus ja kopiijahttojuvvo repository ruhtii vuođđo `README.md`-ovdanbuktin. Ruhta japánalaš README **ii** geavahuvvo jorgalusa gáldun. Eará 181 locale jorgaluvvojit mašiinnalaččat eŋgelasgielas.

## Fuomášumit

- Notebooka bisseha ovdal transkripšuvnna jos GPU ii leat olámuttus.
- Gieđahallanáigi sorjá inputa guhkkodagas, heivehusain ja Colab:a juohkin GPU:s. Vuosttaš geardde láddejuvvojit maiddái NeMo ja sullii 1.23 GB modealla.
- Guhkes jietna gieđahallojuvvo siskkáldas chunk:in, nu ahte dovdan sáhttá váikkuhuvvot chunk-rájáid lahka.

## Kanonalaš gáldu ja ráhkadeapmi

Kanonalaš jorgaluvvon gáldut:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` lea synkroniserejuvvon kanonalaš snapshot. Japánagiella bajásdoallojuvvo dárkkistuvvon jorgalussan `locales/ja.json`:s, ja dan README-snapshot kopiijahttojuvvo ruhta `README.md`:i.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Jorgalusaid bajásdoallan lea sierra dábálaš CI:s. Dábálaš geavaheaddjit ja CI eai dárbbaš jorgalusa credentials.

## Liseansa

Notebooka scaffold ja build/check-skriptat leat MIT-liseanssain. Third Intelligence-modealla ii leat dáppe mielde juhkojuvvon ja dan hálddaša **Apache-2.0**. Goalmmát beali dependenssat seailluhit iežaset liseanssaid.
