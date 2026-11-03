# Haas Japanese Colab

Google Colab zvezek za prepisovanje japońskiego dźwięku i wideo za pomocą Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_sl.ipynb)

## Funkcije

- **Brezplačno:** Działa w bezpłatnym środowisku GPU Google Colab.
- **Japoński ASR:** Używa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), modelu o około 0.6B parametrów do rozpoznawania japońskiej mowy.
- **Hitro:** Transkrypcja może być przetwarzana szybko.
- **Ločila:** Model generuje szacowaną japońską interpunkcję.
- **Časovne oznake in podnapisi:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Obdelava dolgih datotek:** Można również przetwarzać długie pliki audio i wideo.
- **Podpora za Google Drive:** Przesyłaj pliki bezpośrednio lub odczytuj je z Google Drive; wynikowy ZIP może być opcjonalnie zapisany na Drive.
- **Več izhodnih formatov:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest i ZIP.

## Uporaba

1. Wybierz `INPUT_MODE` w **1. Settings** i w razie potrzeby dostosuj inne ustawienia.
2. Wybierz **Runtime → Run all**.
3. Przy `INPUT_MODE = "upload"` wybierz pliki w **2. File selection / Google Drive mount**.
4. Wynikowy ZIP zostanie automatycznie pobrany po zakończeniu przetwarzania.

## Načini časovnih oznak

- `none`: bez informacji o czasie.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Dekoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Dolge datoteke

`CHUNK_SECONDS` steruje wewnętrznym czasem trwania fragmentu używanym dla długich plików. Większe wartości zmniejszają liczbę granic i zachowują więcej kontekstu, ale każda inferencja jest cięższa i może zwiększać użycie pamięci GPU. Mniejsze wartości odciążają każdą inferencję, ale tworzą więcej granic, co może wpływać na rozpoznawanie w ich pobliżu. W większości przypadków zalecana jest wartość domyślna.

## Lokaliziran vmesnik

Sam model ASR jest **tylko dla języka japońskiego**. Lokalizacja README i interfejsu Colab obejmuje wszystkie **183 aktywne języki ISO 639 Set 1** (przestarzały `sh` jest wykluczony).

Angielski (`en`) jest kanonicznym źródłem tłumaczenia. Japoński (`ja`) jest przejrzanym tłumaczeniem i jest kopiowany do katalogu głównego repozytorium jako domyślna prezentacja `README.md`. Japoński README w katalogu głównym **nie** jest używany jako źródło tłumaczenia. Pozostałe 181 lokalizacji są tłumaczone maszynowo z angielskiego.

## Opombe

- Notatnik zatrzymuje się przed transkrypcją, jeśli GPU nie jest dostępne.
- Czas przetwarzania zależy od długości wejścia, ustawień i GPU przydzielonego przez Colab. Przy pierwszym uruchomieniu pobierane są również NeMo i model o rozmiarze około 1.23 GB.
- Długie audio jest przetwarzane w wewnętrznych fragmentach, więc rozpoznawanie może być mniej dokładne w pobliżu granic fragmentów.

## Kanonični vir in generiranje

Kanoniczne źródła przeznaczone do tłumaczenia:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` jest zsynchronizowanym kanonicznym snapshotem. Japoński jest utrzymywany jako przejrzane tłumaczenie w `locales/ja.json`, a jego snapshot README jest kopiowany do katalogu głównego jako `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Utrzymanie tłumaczeń jest oddzielone od zwykłego CI. Zwykli użytkownicy i CI nie potrzebują poświadczeń do tłumaczeń.

## Licenca

Szkielet notatnika oraz skrypty budowania/sprawdzania są objęte licencją MIT. Model Third Intelligence nie jest tutaj redystrybuowany i podlega **Apache-2.0**. Zależności firm trzecich zachowują własne licencje.
