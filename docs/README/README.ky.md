# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0** ilə yapon audio və video fayllarını transkripsiya etmək üçün Google Colab дәптері.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ky.ipynb)

## Мүмкүнчүлүктөр

- **Акысыз:** Google Colab-ın pulsuz GPU mühitində işləyir.
- **Yapon ASR:** Yapon nitqinin tanınması üçün təxminən 0.6B parametrli [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) modelindən istifadə edir.
- **Тез:** Transkripsiya sürətlə emal edilə bilər.
- **Тыныш белгилери:** Model təxmini yapon durğu işarələri çıxarır.
- **Убакыт белгилери жана субтитрлер:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Узун файлдарды иштетүү:** Uzun audio və video faylları da emal edilə bilər.
- **Google Drive колдоосу:** Faylları birbaşa yükləyin və ya Google Drive-dan oxuyun; çıxış ZIP-i istəyə görə Drive-a saxlanıla bilər.
- **Çoxsaylı çıxışlar:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest və ZIP.

## Колдонуу

1. **1. Settings** bölməsində `INPUT_MODE` seçin və lazım olduqda digər parametrləri tənzimləyin.
2. **Runtime → Run all** seçin.
3. `INPUT_MODE = "upload"` olduqda **2. File selection / Google Drive mount** bölməsində faylları seçin.
4. Emal bitdikdən sonra çıxış ZIP avtomatik endirilir.

## Убакыт белгилеринин режимдери

- `none`: vaxt məlumatı yoxdur.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Декодер

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Узун файлдар

`CHUNK_SECONDS` uzun fayllar üçün daxili hissənin müddətini idarə edir. Böyük dəyərlər sərhədləri azaldır və daha çox kontekst saxlayır, lakin hər inferensiyanı ağırlaşdırır və GPU yaddaş istifadəsini artıra bilər. Kiçik dəyərlər hər inferensiyanı yüngülləşdirir, lakin daha çox sərhəd yaradır və bu nöqtələr ətrafında tanımaya təsir edə bilər. Əksər hallarda standart dəyər tövsiyə olunur.

## Локалдаштырылган интерфейс

ASR modelinin özü **yalnız yapon dili üçündür**. README və Colab interfeysinin lokallaşdırılması bütün **183 aktiv ISO 639 Set 1 dilini** əhatə edir (köhnəlmiş `sh` istisnadır).

İngilis dili (`en`) kanonik tərcümə mənbəyidir. Yapon dili (`ja`) yoxlanılmış tərcümədir və standart `README.md` təqdimatı kimi repository kökünə kopyalanır. Kökdəki yapon README-si **tərcümə mənbəyi kimi istifadə edilmir**. Qalan 181 locale ingilis dilindən maşın tərcüməsi olunur.

## Эскертүүлөр

- GPU mövcud deyilsə, notebook transkripsiyadan əvvəl dayanır.
- Emal müddəti giriş uzunluğundan, parametrlərdən və Colab tərəfindən ayrılan GPU-dan asılıdır. İlk işə salınmada NeMo və təxminən 1.23 GB model də endirilir.
- Uzun audio daxili hissələrdə emal olunur, buna görə hissə sərhədləri yaxınlığında tanıma təsirlənə bilər.

## Канондук булак жана түзүү

Kanonik tərcümə olunan mənbələr:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` sinxronlaşdırılmış kanonik snapshot-dır. Yapon dili `locales/ja.json` daxilində yoxlanılmış tərcümə kimi saxlanılır və onun README snapshot-u `README.md` kimi kökə kopyalanır.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Tərcümə baxımı adi CI-dən ayrıdır. Adi istifadəçilər və CI üçün tərcümə etimadnamələri tələb olunmur.

## Лицензия

Notebook skeleti və build/check skriptləri MIT lisenziyalıdır. Third Intelligence modeli burada yenidən paylanmır və **Apache-2.0** ilə tənzimlənir. Üçüncü tərəf asılılıqları öz lisenziyalarını saxlayır.
