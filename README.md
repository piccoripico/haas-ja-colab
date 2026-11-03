# Haas Japanese Colab

Third Intelligenceの **Haas-ja-v1.0** をGoogle Colabで実行し、日本語の音声・動画ファイルを文字起こしするためのノートブックです。

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ja.ipynb)

## 特長

- **無料:** Google Colabの無料GPUランタイムで実行できます。
- **日本語向け音声認識モデル:** [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) を使用します。日本語音声を文字に変換するための約0.6Bパラメータのモデルです。
- **高速:** 高速に文字起こしの処理ができます。
- **句読点を出力:** 認識結果には、モデルが推定した「、」「。」などの句読点が含まれます。
- **時刻情報・字幕:** `subtitle` では音声分割区間の概算時刻に基づくSRTを出力します。文字・単語単位の正確なタイムスタンプは出力できません。`none` では時刻情報を付けません。
- **長時間ファイル対応:** 長い音声・動画ファイルも処理できます。
- **Google Drive対応:** 直接アップロードまたはGoogle Drive内のファイルを処理できます。
- **複数形式:** TXT / Markdown / JSON / CSV / XLSX / SRTを出力し、最後にZIPへまとめます。

## 使い方

1. Colabで **1. 設定** の `INPUT_MODE` を選び、必要に応じてその他の設定を変更します。
2. **Runtime → Run all** を選択します。
3. `INPUT_MODE = "upload"` の場合は、**2. ファイル選択 / Google Driveマウント** でファイルを選択します。
4. 処理終了後、出力ZIPが自動ダウンロードされます。

## タイムスタンプ

- `none`: 時刻情報を付けません。
- `subtitle`: 音声分割区間に基づく概算時刻でSRTを生成します（単語時刻ではありません）。

## デコーダー

Haas-ja-v1.0はTDT専用で、CTC方式には切り替えられません。

## 長時間ファイル

`CHUNK_SECONDS` は、長時間ファイルを内部で何秒ずつに分けて処理するかを指定します。値を大きくすると分割回数が減って前後の文脈を保ちやすくなる一方、1回の処理が重くなり、GPUメモリ使用量も増えやすくなります。値を小さくすると1回の処理は軽くなりますが、分割位置が増えるため、その前後で認識が途切れる可能性があります。通常は既定値のままで構いません。

## 多言語UI

音声認識モデル自体は**日本語専用**です。READMEとColabの操作UIは、廃止済みの `sh` を除くactive ISO 639 Set 1 **全183言語**を公開対象とします。

翻訳sourceは英語 (`en`) です。日本語 (`ja`) はレビュー済み翻訳で、このroot `README.md` は `ja` localeの表示用コピーです。root README自体を他言語翻訳のsourceにはしません。その他181言語は英語正本から機械翻訳します。対応状況は [`docs/LANGUAGES.md`](docs/LANGUAGES.md) を参照してください。

## 備考

- GPUが利用できない場合、文字起こし開始前に停止します。
- 処理時間は、ファイルの長さ、設定、Colabで割り当てられるGPUなどによって異なります。初回実行時はNeMoと約1.23GBのモデルをColab上で取得するため、文字起こし開始まで時間がかかる場合があります。
- 長時間音声は内部で分割して処理するため、分割位置の前後で文脈が途切れ、認識結果に影響する場合があります。

## レポジトリ構成

```text
README.md                                  # 日本語の既定表示（ja localeから生成）
source/
  README.en.md                             # 英語README正本
notebooks/
  Haas_Japanese_Colab_en.ipynb         # 英語Notebook正本
  Haas_Japanese_Colab_ja.ipynb         # 日本語レビュー済み生成物
  Haas_Japanese_Colab_<lang>.ipynb
notebook_template/
  Haas_Japanese_Colab.template.ipynb
locales/
  <ISO-639-1-code>.json
localization/
  set1_languages.json                      # active ISO 639 Set 1全183言語
scripts/
  sync_from_english.py
  build_notebooks.py
  build_readmes.py
  translate_full_locales.py
  check_repository.py
docs/
  LANGUAGES.md
  ARCHITECTURE.md
  README/
    README.<lang>.md
```

## 正本と生成

翻訳対象テキストの正本は、英語の `source/README.en.md` と `notebooks/Haas_Japanese_Colab_en.ipynb` です。

日本語は `locales/ja.json` で `reviewed` として管理し、freshな日本語READMEスナップショットをroot `README.md`へコピーします。

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

翻訳の更新は通常CIとは分離します。通常CIとColab利用者には翻訳APIキーを要求しません。

## ライセンス

このレポジトリのNotebook scaffoldingおよびbuild/check scriptsはMIT Licenseです。Third Intelligenceモデル自体は再配布せず、モデルには **Apache-2.0** が適用されます。その他の依存関係にはそれぞれのライセンスが適用されます。
