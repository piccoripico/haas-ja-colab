# Haas Japanese Colab

Сiя тетрадь Google Colab употребляетъ Third Intelligence **Haas-ja-v1.0**, да преложитъ японскыя аудио и видео файлы въ писаніе.

[![Отвори въ Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_cu.ipynb)

## Свойства

- **Безъ мзды:** Дѣйствуетъ на безмездномъ GPU runtime Google Colab.
- **Японское ASR:** Употребляетъ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), модель приблизительно 0.6B-parameter для распознанія японской рѣчи.
- **Скоро:** Преложеніе рѣчи въ писаніе можетъ творитися скоро.
- **Знаки писменныя:** Модель изводитъ предполагаемыя японскыя знаки препинанія.
- **Временная знаменія и подстрочія:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Дѣланіе долгихъ файловъ:** Долгія аудио и видео файлы такожде могутъ быти обработаны.
- **Помощь Google Drive:** Файлы можно вознести прямо или прочести изъ Google Drive; выходный ZIP по желанію можетъ сохранитися въ Drive.
- **Многія исходы:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest и ZIP.

## Употребленіе

1. Избери `INPUT_MODE` въ **1. Settings** и измѣни иныя устроенія, аще потребно.
2. Избери **Runtime → Run all**.
3. При `INPUT_MODE = "upload"` избери файлы въ **2. File selection / Google Drive mount**.
4. По скончаніи дѣланія выходный ZIP самъ нисходитъ.

## Образы timestamp

- `none`: нѣсть свѣдѣнія о времени.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Долгія файлы

`CHUNK_SECONDS` правитъ длительностію внутреннихъ chunk, употребляемыхъ для долгихъ файловъ. Большія значенія умаляютъ границы и сохраняютъ больше context, но всякое inference бываетъ тяжче и можетъ требовати больше GPU memory. Меньшія значенія облегчаютъ всякое inference, но творятъ больше границъ, что можетъ измѣнити распознаніе близъ тѣхъ мѣстъ. Въ большинствѣ случаевъ подобаетъ предуставленное значеніе.

## Локализованный UI

Самая ASR модель есть **токмо японская**. Локализація README и Colab UI обемлетъ вся **183 active ISO 639 Set 1 languages** (ветхій `sh` исключенъ).

English (`en`) есть каноническій источникъ перевода. Японскій (`ja`) есть просмотрѣнный переводъ и копируется въ корень repository яко обычное представленіе `README.md`. Корневой Japanese README **не употребляется** яко источникъ перевода. Прочія 181 locale машинно переводятся изъ English.

## Примѣчанія

- Тетрадь престаетъ прежде transcription, аще GPU недоступенъ.
- Время дѣланія зависитъ отъ долготы входа, устроеній и GPU, данного Colab. Въ первомъ теченіи такожде нисходятъ NeMo и модель приблизительно 1.23 GB.
- Долгое аудио дѣлается внутренними chunk, посему распознаніе можетъ измѣнитися близъ chunk boundaries.

## Каноническій источникъ и созданіе

Каноническія переводимыя источники:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` есть согласованный каноническій снимокъ. Японскій содержится яко просмотрѣнный переводъ въ `locales/ja.json`, и его README снимокъ копируется въ корневой `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Попеченіе о переводѣ отдѣльно отъ обычнаго CI. Обычнымъ пользователемъ и CI не потребны translation credentials.

## Лицензія

Notebook scaffolding и build/check scripts имѣютъ MIT лицензію. Third Intelligence модель здѣ не распространяется и управляется **Apache-2.0**. Стороннія зависимости сохраняютъ свои лицензіи.
