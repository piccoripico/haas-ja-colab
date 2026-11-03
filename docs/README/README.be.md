# Haas Japanese Colab

Нататнік Google Colab для транскрибирования японскіх аудио- и видеофайлов с помощью Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_be.ipynb)

## Магчымасці

- **Бясплатна:** Працуе в бесплатной среде GPU Google Colab.
- **Японскі ASR:** Использует [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), модель примерно с 0.6B параметров для распознавания японскай речи.
- **Хутка:** Транскрипция может выполняться быстро.
- **Пунктуацыя:** Модель выводит оценочную японскую пунктуацию.
- **Часавыя пазнакі і субтытры:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Апрацоўка доўгіх файлаў:** Можно обрабатывать и длинные аудио- и видеофайлы.
- **Падтрымка Google Drive:** Загружайте файлы напрямую или читайте их из Google Drive; выходной ZIP при необходимости можно сохранить на Drive.
- **Некалькі фарматаў вываду:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest и ZIP.

## Выкарыстанне

1. Выберите `INPUT_MODE` в **1. Settings** и при необходимости измените другие настройки.
2. Выберите **Runtime → Run all**.
3. При `INPUT_MODE = "upload"` выберите файлы в **2. File selection / Google Drive mount**.
4. Выходной ZIP автоматически загружается после завершения обработки.

## Рэжымы часавых пазнак

- `none`: без временной информации.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Декодер

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Доўгія файлы

`CHUNK_SECONDS` задаёт внутреннюю длительность фрагмента для длинных файлов. Большие значения уменьшают число границ и сохраняют больше контекста, но делают каждый вывод тяжелее и могут увеличить использование памяти GPU. Меньшие значения облегчают каждый вывод, но создают больше границ, что может повлиять на распознавание рядом с ними. В большинстве случаев рекомендуется значение по умолчанию.

## Лакалізаваны інтэрфейс

Сама модель ASR предназначена **только для японского языка**. Локализация README и интерфейса Colab охватывает все **183 активных языка ISO 639 Set 1** (устаревший `sh` исключён).

Английский (`en`) является каноническим источником перевода. Японскі (`ja`) — проверенный перевод, который копируется в корень репозитория как представление `README.md` по умолчанию. Корневой японский README **не** используется как источник перевода. Остальные 181 локаль машинно переводятся с английского.

## Заўвагі

- Нататнік останавливается до транскрипции, если GPU недоступен.
- Время обработки зависит от длины входных данных, настроек и GPU, назначенного Colab. При первом запуске также загружаются NeMo и модель размером около 1.23 GB.
- Длинное аудио обрабатывается внутренними фрагментами, поэтому распознавание может ухудшаться возле границ фрагментов.

## Кананічная крыніца і генерацыя

Канонические переводимые источники:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` — синхронизированный канонический snapshot. Японскі поддерживается как проверенный перевод в `locales/ja.json`, а его snapshot README копируется в корень как `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Падтрымка переводов отделена от обычного CI. Обычным пользователям и CI не нужны учётные данные для перевода.

## Ліцэнзія

Каркас блокнота и скрипты сборки/проверки лицензированы по MIT. Модель Third Intelligence здесь не распространяется и регулируется **Apache-2.0**. Сторонние зависимости сохраняют собственные лицензии.
