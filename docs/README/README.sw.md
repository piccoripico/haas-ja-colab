# Haas Japanese Colab

Daftari la Google Colab la kunukuu faili za sauti na video za Kijapani kwa kutumia Third Intelligence **Haas-ja-v1.0**.

[![Fungua katika Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sw.ipynb)

## Vipengele

- **Bure:** Hufanya kazi kwenye mazingira ya GPU ya bure ya Google Colab.
- **ASR ya Kijapani:** Hutumia [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modeli yenye takribani vigezo bilioni 0.6 kwa utambuzi wa usemi wa Kijapani.
- **Haraka:** Unukuzi unaweza kuchakatwa kwa haraka.
- **Alama za uandishi:** Modeli hutoa makadirio ya alama za uandishi za Kijapani.
- **Mihuri ya muda na manukuu:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Uchakataji wa faili ndefu:** Faili ndefu za sauti na video pia zinaweza kuchakatwa.
- **Usaidizi wa Google Drive:** Pakia faili moja kwa moja au zisome kutoka Google Drive; ZIP ya matokeo inaweza pia kuhifadhiwa kwenye Drive kwa hiari.
- **Matokeo ya aina nyingi:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, na ZIP.

## Matumizi

1. Chagua `INPUT_MODE` katika **1. Settings** na urekebishe mipangilio mingine ikihitajika.
2. Chagua **Runtime → Run all**.
3. Kwa `INPUT_MODE = "upload"`, chagua faili katika **2. File selection / Google Drive mount**.
4. ZIP ya matokeo inapakuliwa kiotomatiki baada ya uchakataji kukamilika.

## Hali za mihuri ya muda

- `none`: hakuna taarifa ya muda.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoda

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Faili ndefu

`CHUNK_SECONDS` hudhibiti muda wa kila kipande cha ndani kinachotumiwa kwa faili ndefu. Thamani kubwa hupunguza mipaka ya vipande na kuhifadhi muktadha zaidi, lakini hufanya kila inference kuwa nzito zaidi na inaweza kuongeza matumizi ya kumbukumbu ya GPU. Thamani ndogo hufanya kila inference kuwa nyepesi zaidi lakini huunda mipaka mingi zaidi, jambo ambalo linaweza kuathiri utambuzi karibu na maeneo hayo. Thamani chaguo-msingi inapendekezwa katika hali nyingi.

## Kiolesura kilichotafsiriwa

Modeli ya ASR yenyewe ni **ya Kijapani pekee**. Utafsiri wa README na kiolesura cha Colab unashughulikia lugha zote **183 zinazotumika katika ISO 639 Set 1** (`sh` ya zamani imeondolewa).

Kiingereza (`en`) ndicho chanzo kanoni cha tafsiri. Kijapani (`ja`) ni tafsiri iliyokaguliwa na hunakiliwa kwenye mzizi wa hazina kama mwonekano chaguo-msingi wa `README.md`. README ya Kijapani iliyo kwenye mzizi **haitumiki** kama chanzo cha tafsiri. Lugha nyingine 181 hutafsiriwa kwa mashine kutoka Kiingereza.

## Maelezo

- Daftari husimama kabla ya unukuzi ikiwa GPU haipatikani.
- Muda wa uchakataji hutegemea urefu wa ingizo, mipangilio, na GPU iliyotolewa na Colab. Uendeshaji wa kwanza pia hupakua NeMo na modeli yenye ukubwa wa takribani GB 2.5.
- Sauti ndefu huchakatwa kwa vipande vya ndani, hivyo utambuzi unaweza kuathiriwa karibu na mipaka ya vipande.

## Chanzo kanoni na uundaji

Vyanzo kanoni vinavyoweza kutafsiriwa:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ni nakala kanoni iliyosawazishwa. Kijapani hutunzwa kama tafsiri iliyokaguliwa katika `locales/ja.json`, na nakala yake ya README hunakiliwa kwenye `README.md` ya mzizi.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Utunzaji wa tafsiri umetenganishwa na CI ya kawaida. Watumiaji wa kawaida na CI hawahitaji vitambulisho vya huduma za tafsiri.

## Leseni

Muundo wa daftari na hati za build/check zina leseni ya MIT. Modeli ya Third Intelligence haisambazwi hapa na inasimamiwa na **Apache-2.0**. Vitegemezi vya wahusika wengine vinaendelea kutumia leseni zao wenyewe.
