# Haas Japanese Colab

Google Colab notebook япон кывъя аудио да видео текстӧ гижӧм вылӧ Third Intelligence **Haas-ja-v1.0** отсӧгӧн.

[![Colab-ын восьтыны](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_kv.ipynb)

## Позянлунъяс

- **Донӧсьтӧм:** Google Colab-лӧн донӧсьтӧм GPU runtime-ын уджалӧ.
- **Япон ASR:** Вӧчӧ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), 0.6B parameter гӧгӧр япон сёрни тӧдмалан model.
- **Регыд:** Transcription позьӧ вӧчны регыд.
- **Пунктуация:** Model петкӧдлӧ япон пунктуацияыслысь виччысьӧм пасъяс.
- **Timestamps да subtitles:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Кузь файлъяс:** Кузь аудио да видео файлъяссӧ сідзжӧ позьӧ обработайтны.
- **Google Drive:** Файлъяссӧ загрузитны веськыда либӧ лыддьыны Google Drive-ысь; output ZIP позьӧ колана ногӧн видзны Drive-ын.
- **Уна output:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest да ZIP.

## Кыдз вӧчны

1. **1. Settings**-ын бӧрйы `INPUT_MODE` да колӧкӧ веж settings-ъяссӧ.
2. Бӧрйы **Runtime → Run all**.
3. `INPUT_MODE = "upload"` дырйи бӧрйы файлъяс **2. File selection / Google Drive mount**-ын.
4. Обработка бӧрын output ZIP аслыс download-сьӧ.

## Timestamp mode-ъяс

- `none`: кад йылысь юӧр абу.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Кузь файлъяс

`CHUNK_SECONDS` веськӧдлӧ кузь файлъясын internal chunk-лӧн кадӧн. Ыджыдджык value-ъяс чинтӧны boundaries да видзӧны унджык context, но быд inference лоӧ сьӧкыдджык да вермӧ вӧдитны унджык GPU memory. Ичӧтджык value-ъяс вӧчӧны inference кокниджык, но лӧсьӧдӧны унджык boundaries, мый вермӧ вӧзйыны recognition сэтчӧ матын. Уна случайын default бурджык.

## Локализируйтӧм UI

ASR model ачыс **сӧмын япон кыв вылӧ**. README да Colab UI localization шымыртӧ став **183 active ISO 639 Set 1 кыв** (`sh` важӧн вӧлі, но абу пыртӧма).

Англискӧй (`en`) — canonical translation source. Япон (`ja`) — reviewed translation, кодӧс repository root-ӧ копируйтӧма default `README.md` пыдди. Root Japanese README **оз вӧдитсьы** translation source пыдди. Мукӧд 181 locale-ыс machine-translate-сьӧны англискӧйысь.

## Пасйӧдъяс

- GPU абу кежлӧ notebook сувтӧдӧ transcription водзын.
- Processing time зависита input кузьтаысь, settings-ысь да Colab-ӧн сетӧм GPU-ысь. Медводдза run дырйи NeMo да 1.23 GB гӧгӧр model сідзжӧ download-сьӧны.
- Кузь аудио обработайтсьӧ internal chunks-ын, сӧмын chunk boundaries бердын recognition вермӧ вежсьыны.

## Canonical source да generation

Вуджӧдны позян каноническӧй источникъяс:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` — synchronized canonical snapshot. Япон кыв видзсьӧ reviewed translation пыдди `locales/ja.json`-ын, а сылӧн README snapshot копируйтсьӧ root `README.md`-ӧ.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance торъя обычнӧй CI-ысь. Обычнӧй users да CI оз ков translation credentials.

## License

Notebook scaffolding да build/check scripts MIT license улын. Third Intelligence model тайӧ проектын оз redistributer-сьы да веськӧдлӧ **Apache-2.0**. Third-party dependencies видзӧны ассьыныс licenses.
