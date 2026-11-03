# Haas Japanese Colab

Notebook Google Colab no te papa’i i te reo Tapone no roto mai i te audio e te video ma te Third Intelligence **Haas-ja-v1.0**.

[![Tatara i Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ty.ipynb)

## Te mau aravihi

- **Aita e aufau:** E tere i nia i te GPU runtime tamoni ore a Google Colab.
- **ASR reo Tapone:** E faaohipa i [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), e model e fatata 0.6B parameter no te ite i te reo Tapone.
- **Vitiviti:** E nehenehe te transcription e rave vitiviti.
- **Mau tapao papa’i:** E horoa te model i te mau tapao papa’i reo Tapone i mana’ohia.
- **Mau taime e subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Raveraa file roa:** E nehenehe atoa e rave i te mau file audio e video roa.
- **Tauturu Google Drive:** Upload tia i te mau file e aore ra taio mai roto mai i Google Drive; e nehenehe te ZIP hopea e haaputu i Drive ia hinaarohia.
- **Mau output rau:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Te faaohiparaa

1. Ma’iti `INPUT_MODE` i roto i **1. Mau faanahoraa** e taui i te tahi atu mau faanahoraa ia titauhia.
2. Ma’iti **Runtime → Run all**.
3. Ia `INPUT_MODE = "upload"`, ma’iti i te mau file i roto i **2. Ma’itiraa file / faatira Google Drive**.
4. E download aunoa te ZIP hopea i muri a’e i te raveraa.

## Mau mode taime

- `none`: aita e parau no te taime.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Mau file roa

`CHUNK_SECONDS` e faatere i te roaraa o te chunk o roto no te mau file roa. Te mau faito rahi e faaiti i te mau otia e e tape’a rahi atu i te context, tera râ e teimaha atu te inference tataitahi e e nehenehe e faaohipa rahi atu i te GPU memory. Te mau faito iti e mama ai te inference tataitahi tera râ e faatupu rahi atu i te mau otia, e nehenehe hoi e haafifi i te iteraa i reira. E maitai te default i te rahiraa o te taime.

## UI i hurihia

Te model ASR iho **no te reo Tapone ana’e**. Te huriraa o README e te UI Colab e tapo'i i te **183 reo ISO 639 Set 1 e faaohipahia nei** (`sh` tahito aita e tapirihia).

Te reo Beretane (`en`) te puna canonical no te huriraa. Te reo Tapone (`ja`) e huriraa tei hi'opo'ahia e e kopi i te tumu repository ei `README.md` default. Te README Tapone i te tumu **aita** e faaohipahia ei puna huriraa. Te tahi atu 181 locale e hurihia e te matini mai te reo Beretane.

## Mau nota

- E faaea te notebook hou te transcription mai te mea aita e GPU.
- Te taime raveraa e ti'a i te roaraa o te input, te mau faanahoraa e te GPU ta Colab e horoa. I te hororaa matamua e download atoa i NeMo e te model fatata 1.23 GB.
- Te audio roa e ravehia i roto i te mau chunk o roto, no reira e nehenehe te iteraa e haafifihia i pihai iho i te mau otia chunk.

## Puna canonical e te hamaniraa

Mau puna canonical e hurihia:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` te snapshot canonical i faatanohia. Te reo Tapone e faatiahia ei huriraa tei hi'opo'ahia i `locales/ja.json`, e e kopi te snapshot README i te tumu `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Te atuaturaa huriraa e taa ê ïa i te CI matauhia. Aita te feia faaohipa matauhia e te CI e hinaaro i te credentials huriraa.

## Raihana

Te scaffold notebook e te mau script build/check e raihana MIT. Aita te model Third Intelligence e opere-faahou-hia i ô nei e e faaterehia e **Apache-2.0**. Te mau dependency no te tahi atu mau pae e tape’a i ta ratou iho raihana.
