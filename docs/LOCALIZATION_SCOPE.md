# ローカライズ対象範囲

## 選定基準

公開対象は、廃止済みの `sh` を除くactive ISO 639 Set 1 **全183言語**です。

- 正本: 英語 (`en`)
- レビュー済み翻訳: 日本語 (`ja`)
- 機械翻訳: その他181言語
- root README表示: 日本語 (`ja`)
- 公開対象総数: **183言語**
- 唯一の言語一覧: `localization/set1_languages.json`

root `README.md` を日本語にすることと、翻訳sourceを英語にすることは分離します。root READMEは `ja` localeから生成・同期されるpresentationです。

## 対象外

- 廃止済みISO 639-1コード `sh`
- ISO 639 Set 1そのものではない地域・script variant（例: `zh-CN`, `zh-TW`, `pt-BR`, `pt-PT`, `sr-Latn`）

## モデルとの関係

`third-intelligence/Haas-ja-v1.0` は日本語専用の音声認識モデルです。ローカライズされるのはREADMEとColab操作UIであり、文字起こし対象言語は日本語のままです。
