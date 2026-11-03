# Haas Japanese Colab

Google Colab notebook si wɔa Japanese audio kple video ŋu transcription yi text me kple Third Intelligence **Haas-ja-v1.0**.

[![ʋu le Colab me](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ee.ipynb)

## Nusiwo wòte ŋu wɔ

- **Fame:** Eƒoa du le Google Colab ƒe GPU runtime fame dzi.
- **Japanese ASR:** Eza [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), model si le abe 0.6B-parameter ene hena Japanese speech recognition.
- **Kabã:** Woate ŋu aprocess transcription kabã.
- **Punctuation:** Model la doa Japanese punctuation si wòbu be wòle eteƒe la ɖa.
- **Timestamp kple subtitle:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Long-file processing:** Woate ŋu aprocess audio kple video file didi hã.
- **Google Drive support:** Upload file tẽe alo xle wo tso Google Drive; woate ŋu asave output ZIP ɖe Drive me ne èdi.
- **Output vovovowo:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, kple ZIP.

## Ale si woazãe

1. Tia `INPUT_MODE` le **1. Settings** me eye nàtrɔ setting bubuwo ne ehiã.
2. Tia **Runtime → Run all**.
3. Ne `INPUT_MODE = "upload"` la, tia file le **2. File selection / Google Drive mount** me.
4. Ne processing vɔ la, output ZIP adownload eɖokui.

## Timestamp modes

- `none`: timing information aɖeke mele o.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File didiwo

`CHUNK_SECONDS` ɖoa internal chunk ƒe didime hena file didiwo. Value gãwo na boundarywo sue eye woɖoa context geɖe ŋu, gake inference ɖesiaɖe zu kpekpeɖeŋu eye ate ŋu aza GPU memory geɖe. Value suewo na inference ɖesiaɖe bɔbɔe gake woɖoa boundary geɖe, si ate ŋu awɔ recognition ŋu dɔ le teƒeawo gbɔ. Le go bubuwo katã me la, default la wòle nyuie.

## UI si wotrɔ gbe me

ASR model la ŋutɔ nye **Japanese-only**. README kple Colab UI localization ɖoa **183 active ISO 639 Set 1 languages** katã (deprecated `sh` mede eme o).

English (`en`) nye canonical translation source. Japanese (`ja`) nye reviewed translation eye wocopye yi repository root abe default `README.md` presentation ene. Root Japanese README la **meɖoa** abe translation source o. Locale 181 bubuawo nye machine-translated tso English me.

## Nusiwo woanya

- Notebook la dzia tɔtrɔ hafi transcription adze egɔme ne GPU mele o.
- Processing time ɖoa input ƒe didime, setting, kple GPU si Colab na dzi. Le run gbãtɔ me la, NeMo kple model si le abe 1.23 GB ene hã adownload.
- Audio didiwo wɔa processing le internal chunks me, eyata recognition ate ŋu atrɔ le chunk boundaries gbɔ.

## Canonical source kple generation

Nukpɔkpɔ gã siwo wòate ŋu aɖe gbe me:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` nye synchronized canonical snapshot. Wotsɔ Japanese ɖo `locales/ja.json` me abe reviewed translation ene, eye wocopy eƒe README snapshot yi root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance le vovome tso ordinary CI gbɔ. Ordinary users kple CI mehiã translation credentials o.

## License

Notebook scaffolding kple build/check scripts le MIT license te. Third Intelligence model la womagãe le afisia o eye **Apache-2.0** ye ɖoa eŋu. Third-party dependencies ɖea woawo ŋutɔ ƒe licenses dzi.
