# Haas Japanese Colab

Littafin aiki na Google Colab don rubuta sautin da bidiyon Jafananci zuwa rubutu da Third Intelligence **Haas-ja-v1.0**.

[![Buɗe a Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ha.ipynb)

## Fasali

- **Kyauta:** Yana aiki a kan runtime na GPU kyauta na Google Colab.
- **ASR na Jafananci:** Yana amfani da [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), samfurin kusan 0.6B parameters don gane maganar Jafananci.
- **Mai sauri:** Ana iya sarrafa transkripsan cikin sauri.
- **Alamomin rubutu:** Samfurin yana fitar da alamomin rubutun Jafananci da aka kiyasta.
- **Lokuta da subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Sarrafa dogayen fayiloli:** Hakanan ana iya sarrafa dogayen fayilolin sauti da bidiyo.
- **Taimakon Google Drive:** Loda fayiloli kai tsaye ko karanta su daga Google Drive; ana iya ajiye ZIP na fitarwa zuwa Drive idan ana so.
- **Fitarwa iri-iri:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest da ZIP.

## Amfani

1. Zaɓi `INPUT_MODE` a **1. Settings** sannan ka daidaita sauran saituna idan ya cancanta.
2. Zaɓi **Runtime → Run all**.
3. Idan `INPUT_MODE = "upload"` ne, zaɓi fayiloli a **2. File selection / mount na Google Drive**.
4. Ana sauke ZIP na fitarwa kai tsaye bayan sarrafawa.

## Yanayin lokuta

- `none`: babu bayanin lokaci.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Dogayen fayiloli

`CHUNK_SECONDS` yana sarrafa tsawon chunk na ciki da ake amfani da shi don dogayen fayiloli. Manyan ƙimomi suna rage iyakoki kuma suna kiyaye ƙarin context, amma suna sa kowace inference ta fi nauyi kuma suna iya ƙara amfani da ƙwaƙwalwar GPU. Ƙananan ƙimomi suna sa kowace inference ta fi sauƙi amma suna ƙirƙirar ƙarin iyakoki, wanda zai iya shafar gane magana kusa da waɗannan wurare. A mafi yawan lokuta ana ba da shawarar ƙimar tsoho.

## UI da aka fassara

Samfurin ASR kansa **na Jafananci ne kawai**. Fassarar README da Colab UI tana rufe **dukkan harsuna 183 masu aiki na ISO 639 Set 1** (ba a haɗa `sh` da aka daina amfani da shi ba).

Turanci (`en`) shi ne tushen fassara na canonical. Jafananci (`ja`) fassara ce da aka duba kuma ana kwafarta zuwa tushen repository a matsayin gabatarwar `README.md` ta tsoho. README na Jafananci da ke tushen **ba a amfani da shi a matsayin tushen fassara**. Sauran locale 181 ana fassara su ta na’ura daga Turanci.

## Bayanan kula

- Littafin aiki yana tsayawa kafin transkripsan idan babu GPU.
- Lokacin sarrafawa ya danganta da tsawon input, saituna da GPU da Colab ya ware. A farkon run ana kuma sauke NeMo da samfurin kusan 1.23 GB.
- Ana sarrafa dogon sauti a cikin chunks na ciki, don haka gane magana na iya shafuwa a kusa da iyakokin chunk.

## Tushen canonical da generation

Tushen canonical da za a iya fassara:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` shi ne synchronized canonical snapshot. Ana kula da Jafananci a matsayin fassara da aka duba a `locales/ja.json`, kuma ana kwafar snapshot ɗin README zuwa root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Kula da fassara ya bambanta da CI na yau da kullum. Masu amfani na yau da kullum da CI ba sa buƙatar translation credentials.

## Lasisi

Tsarin notebook da build/check scripts suna ƙarƙashin lasisin MIT. Ba a sake rarraba samfurin Third Intelligence a nan kuma yana ƙarƙashin **Apache-2.0**. Third-party dependencies suna riƙe lasisinsu na kansu.
