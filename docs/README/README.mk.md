# Haas Japanese Colab

Google Colab тетратка за транскрипция јапонски аудио и видео садржаја помоћу Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_mk.ipynb)

## Функции

- **Бесплатно:** Работи у бесплатном GPU окружењу Google Colab-а.
- **Јапонски ASR:** Користи [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), модел са приближно 0.6B параметара за препознавање јапонски говора.
- **Брзо:** Транскрипција може брзо да се обради.
- **Интерпункција:** Модел даје процењену јапанску интерпункцију.
- **Временски ознаки и преводи:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Обработка на долги датотеки:** Могу се обрадити и дуге аудио и видео датотеке.
- **Поддршка за Google Drive:** Отпремите датотеке директно или их читајте са Google Drive-а; излазни ZIP се по жељи може сачувати на Drive-у.
- **Повеќе излезни формати:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest и ZIP.

## Употреба

1. Изаберите `INPUT_MODE` у **1. Settings** и по потреби прилагодите друга подешавања.
2. Изаберите **Runtime → Run all**.
3. Са `INPUT_MODE = "upload"`, изаберите датотеке у **2. File selection / Google Drive mount**.
4. Излазни ZIP се аутоматски преузима када се обрада заврши.

## Режими на временски ознаки

- `none`: без временских информација.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Декодер

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Долги датотеки

`CHUNK_SECONDS` контролише унутрашње трајање фрагмента за дуге датотеке. Веће вредности смањују број граница и чувају више контекста, али чине сваку инференцију тежом и могу повећати употребу GPU меморије. Мање вредности олакшавају сваку инференцију, али стварају више граница, што може утицати на препознавање око тих тачака. Подразумевана вредност се препоручује у већини случајева.

## Локализиран интерфејс

Сам ASR модел је **само за јапански**. Локализација README-а и Colab интерфејса обухвата свих **183 активна ISO 639 Set 1 језика** (застарели `sh` је изузет).

Енглески (`en`) је канонски извор превода. Јапонски (`ja`) је прегледан превод и копира се у корен репозиторијума као подразумевани `README.md` приказ. Јапонски README у корену се **не** користи као извор превода. Преосталих 181 locale-а машински се преводи са енглеског.

## Забелешки

- Свеска се зауставља пре транскрипције ако GPU није доступан.
- Време обраде зависи од дужине улаза, подешавања и GPU-а који Colab додели. Прво покретање такође преузима NeMo и модел од приближно 1.23 GB.
- Дуги аудио се обрађује у унутрашњим фрагментима, па препознавање може бити погођено око граница фрагмената.

## Канонски извор и генерирање

Канонски извори за превод:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` је синхронизовани канонски snapshot. Јапонски се одржава као прегледан превод у `locales/ja.json`, а његов README snapshot се копира у корен као `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Одржавање превода је одвојено од обичног CI-а. Обичним корисницима и CI-ју нису потребни акредитиви за превођење.

## Лиценца

Структура свеске и build/check скрипте су под MIT лиценцом. Third Intelligence модел се овде не редистрибуира и регулисан је лиценцом **Apache-2.0**. Зависности трећих страна задржавају своје лиценце.
