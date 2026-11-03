# Haas Japanese Colab

សៀវភៅកត់ត្រា Google Colab សម្រាប់បម្លែងសំឡេង និងវីដេអូជប៉ុនទៅជាអត្ថបទ ដោយប្រើ Third Intelligence **Haas-ja-v1.0**។

[![បើកក្នុង Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_km.ipynb)

## លក្ខណៈពិសេស

- **ឥតគិតថ្លៃ:** ដំណើរការលើ runtime GPU ឥតគិតថ្លៃរបស់ Google Colab។
- **ASR ភាសាជប៉ុន:** ប្រើ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ដែលជាម៉ូដែលប្រហែល 0.6B ប៉ារ៉ាម៉ែត្រ សម្រាប់ស្គាល់សុន្ទរកថាភាសាជប៉ុន។
- **លឿន:** អាចដំណើរការការបម្លែងសំឡេងទៅអត្ថបទបានលឿន។
- **សញ្ញាវណ្ណយុត្ត:** ម៉ូដែលបញ្ចេញសញ្ញាវណ្ណយុត្តជប៉ុនដែលបានប៉ាន់ស្មាន។
- **ត្រាពេលវេលា និងចំណងជើងរង:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ដំណើរការឯកសារវែង:** អាចដំណើរការឯកសារសំឡេង និងវីដេអូវែងបានផងដែរ។
- **គាំទ្រ Google Drive:** ផ្ទុកឯកសារឡើងដោយផ្ទាល់ ឬអានពី Google Drive; ZIP លទ្ធផលអាចរក្សាទុកទៅ Drive ជាជម្រើស។
- **លទ្ធផលច្រើនប្រភេទ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest និង ZIP។

## របៀបប្រើ

1. ជ្រើស `INPUT_MODE` ក្នុង **1. Settings** ហើយកែសម្រួលការកំណត់ផ្សេងទៀតបើចាំបាច់។
2. ជ្រើស **Runtime → Run all**។
3. ជាមួយ `INPUT_MODE = "upload"` ជ្រើសឯកសារនៅ **2. File selection / mount Google Drive**។
4. ZIP លទ្ធផលត្រូវបានទាញយកដោយស្វ័យប្រវត្តិបន្ទាប់ពីដំណើរការ។

## របៀបត្រាពេលវេលា

- `none`: គ្មានព័ត៌មានពេលវេលា។
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ឯកសារវែង

`CHUNK_SECONDS` គ្រប់គ្រងរយៈពេល chunk ខាងក្នុងសម្រាប់ឯកសារវែង។ តម្លៃធំជាងកាត់បន្ថយព្រំដែន និងរក្សា context ច្រើនជាង ប៉ុន្តែធ្វើឱ្យ inference នីមួយៗធ្ងន់ជាង និងអាចប្រើអង្គចងចាំ GPU ច្រើនជាង។ តម្លៃតូចជាងធ្វើឱ្យ inference នីមួយៗស្រាលជាង ប៉ុន្តែបង្កើតព្រំដែនច្រើនជាង ដែលអាចប៉ះពាល់ដល់ការស្គាល់នៅជុំវិញចំណុចទាំងនោះ។ ជាទូទៅណែនាំឱ្យប្រើតម្លៃលំនាំដើម។

## UI បានបកប្រែ

ម៉ូដែល ASR ខ្លួនវា **សម្រាប់ភាសាជប៉ុនប៉ុណ្ណោះ**។ ការបកប្រែ README និង Colab UI គ្របដណ្តប់ **ភាសាសកម្ម ISO 639 Set 1 ទាំង 183** (មិនរាប់បញ្ចូល `sh` ដែលលែងប្រើ)។

ភាសាអង់គ្លេស (`en`) គឺជាប្រភពបកប្រែ canonical។ ភាសាជប៉ុន (`ja`) គឺជាការបកប្រែដែលបានពិនិត្យ និងត្រូវបានចម្លងទៅ root របស់ repository ជាការបង្ហាញ `README.md` លំនាំដើម។ README ភាសាជប៉ុននៅ root **មិនត្រូវបានប្រើជាប្រភពបកប្រែទេ**។ locale 181 ផ្សេងទៀតត្រូវបានបកប្រែដោយម៉ាស៊ីនពីភាសាអង់គ្លេស។

## ចំណាំ

- Notebook ឈប់មុនចាប់ផ្តើម transcription ប្រសិនបើ GPU មិនមាន។
- ពេលវេលាដំណើរការអាស្រ័យលើប្រវែង input ការកំណត់ និង GPU ដែល Colab ផ្តល់។ ការរត់លើកដំបូងក៏ទាញយក NeMo និងម៉ូដែលប្រហែល 1.23 GB ផងដែរ។
- អូឌីយ៉ូវែងត្រូវបានដំណើរការជា chunks ខាងក្នុង ដូច្នេះការស្គាល់អាចត្រូវប៉ះពាល់នៅជុំវិញព្រំដែន chunk។

## ប្រភព canonical និង generation

ប្រភព canonical ដែលអាចបកប្រែ:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` គឺជា synchronized canonical snapshot។ ភាសាជប៉ុនត្រូវបានថែរក្សាជា reviewed translation នៅ `locales/ja.json` ហើយ snapshot README របស់វាត្រូវបានចម្លងទៅ root `README.md`។

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

ការថែរក្សាការបកប្រែបំបែកពី CI ធម្មតា។ អ្នកប្រើធម្មតា និង CI មិនត្រូវការ translation credentials ទេ។

## អាជ្ញាបណ្ណ

Notebook scaffolding និង build/check scripts មានអាជ្ញាបណ្ណ MIT។ ម៉ូដែល Third Intelligence មិនត្រូវបានចែកចាយឡើងវិញនៅទីនេះទេ ហើយស្ថិតក្រោម **Apache-2.0**។ Third-party dependencies រក្សាអាជ្ញាបណ្ណរបស់ខ្លួន។
