# アーキテクチャ

## 正本

翻訳対象テキストの正本言語は **英語 (`en`)** です。

人間が編集する正本は次の2つです。

- `source/README.en.md`
- `notebooks/Haas_Japanese_Colab_en.ipynb`

`scripts/sync_from_english.py` は、これらの英語正本からローカライズ用Notebook templateと `locales/en.json` のcanonical snapshotを同期します。

日本語 (`ja`) はレビュー済み翻訳です。`locales/ja.json` のREADMEスナップショットを root `README.md` にコピーして、日本語をrepositoryの既定表示にします。したがって **root `README.md` は表示用であり、翻訳sourceではありません**。

## ローカライズ対象

公開対象は、廃止済みの `sh` を除くactive ISO 639 Set 1 **全183言語**です。`localization/set1_languages.json` を唯一の言語一覧として、build/check処理はこの一覧から直接公開対象を導出します。

- `en`: 英語正本 (`canonical`)
- `ja`: 英語正本から作成しレビューした日本語 (`reviewed`)。root README表示にも使用
- その他181言語: 英語正本から作成する機械翻訳 (`machine-translated`、レビュー推奨)
- 公開locale総数: **183**

音声認識モデル自体は日本語専用で、ローカライズ対象はREADMEとColab操作UIです。

## 翻訳保守の境界

翻訳は**通常CIとは分離した保守作業**です。通常利用者や通常CIへ翻訳API key、クラウドアカウント、ネットワーク接続を要求しません。翻訳済みテキストを `locales/*.json` に保存し、通常buildはコミット済みlocaleから決定的に生成します。

英語正本を更新すると、英語以外のlocaleはfreshness hashによりfail-closedでstale化します。レビュー済み日本語を自動上書きしてはいけません。

## 移行時の真正性

英語正本へ移行する際、旧ja-canonical構成由来の181翻訳を「英語由来」としてhashだけ更新することは禁止します。旧翻訳payload自体も現行treeには保持せず、対象localeは `pending` + 空payloadへ正規化します。localeが現在の英語canonical hashへ昇格できるのは、英語sourceから実際に再翻訳が成功した場合だけです。これにより、旧翻訳を後方互換として温存する経路は持ちません。


## 全文翻訳の構造不変条件

locale生成では英語canonicalの意味内容を省略しません。READMEとNotebook UIは、自然言語だけを対象言語へ置換し、Markdown構造と技術識別子を保持する1対1変換として扱います。翻訳器が文章を要約・短縮・再構成して公開用localeを生成する経路は持ちません。

Notebookのplaceholderは自然言語だけでなくPython構文上の役割も保持します。英語canonical値が `#` で始まり、code cellへ直接挿入されるplaceholderは、翻訳後も同じコメント接頭辞（`#`、`# @markdown`、`# @title` など）を保持しなければなりません。翻訳済みplaceholderによって生成NotebookがPython syntax errorになる状態はpublishableと扱いません。

また、短い専門ラベル・固有名・技術識別子そのもの（例: `Decoder`, `TDT`, `CTC`, `ZIP`, project title）は対象言語で慣用的に同形となる場合があるため、英語との文字列一致だけでは欠陥としません。一方、設定見出し、helper/load/file-selection/save-download操作、filename filter説明、音声・字幕の説明、状態メッセージ、canonical source説明等の **UI自然言語** は、英語canonicalの文・句を完全一致のまま残すfallbackを禁止します。これらは対象言語へ翻訳し、技術トークンだけを保持します。

各localized READMEのColabリンクはlocale JSONのpayload段階から自身の `Haas_Japanese_Colab_<code>.ipynb` を指さなければなりません。build時のlink正規化は決定的生成の補助であり、誤った翻訳payloadを正しいものとして隠すためには使いません。

旧翻訳からのrebase、translation memory、互換fallbackは禁止します。各 `machine-translated` localeは現在の英語canonicalのみから生成し、全文翻訳完全性・placeholder構文・locale固有linkの各gateを通過した場合にだけpublishableになります。

## 決定的buildの境界

Notebook templateはruntime構造を保持する言語非依存骨格です。localized notebookは、templateと各localeのplaceholderから生成します。英語正本Notebookの同期時だけtemplateを更新します。

locale status:

- `canonical`: 英語正本
- `reviewed`: 人間レビュー済み翻訳（現在は日本語）
- `machine-translated`: 英語正本からの機械翻訳
- `pending`: 未翻訳
- `stale-reviewed`: 現在より古い英語正本に基づくreviewed翻訳
- `stale-machine-translated`: 現在より古い英語正本に基づく機械翻訳

公開用成果物を生成するのは `canonical`、`reviewed`、`machine-translated` のlocaleだけです。完成版では183言語すべてがpublishableかつ現在の英語正本SHA-256と一致していなければなりません。

## freshness

各localeの `canonical_source_sha256` は、同期済みの英語placeholder群と英語README正本から計算したSHA-256です。

- `en`: canonical hashそのもの
- `ja`: review済み日本語がどの英語正本に対応するかを示す
- その他: 機械翻訳がどの英語正本に対応するかを示す

## 後方互換

公開前のため、旧source構成との後方互換は持ちません。旧sync helper、旧sourceを示すcompatibility alias、旧canonical metadataは残しません。

## runtime不変条件（Haas-ja-v1.0）

- モデル: `third-intelligence/Haas-ja-v1.0`
- 公式推論ライブラリ: `haas_asr`（公式コミット `acc614f68769dcbfae9dba96b48439c4a66295af`）
- NeMo: `nemo-toolkit[asr]>=2.7.3,<2.8`、Transformers: `4.57.6`、FLA: `0.5.2`
- `USE_TF=0` をTransformers import前に設定する。TensorFlow / Protobufの不整合を避ける。
- T4はfloat16、compute capability 8以上ではbfloat16でモデルロードする。
- 内部音声: 16 kHz mono PCM WAV。長時間音声は公式 `split_at_quiet_points` を使用する。
- デコーダ: TDTのみ。ParakeetのCTCおよびCUDA graph切替は流用しない。
- `TIMESTAMP_MODE`: `none` / `subtitle`。Haasには元のnative word/char timestampsをそのまま要求できないため、SRTの時間は **分割区間を利用した概算** とし、原生タイムスタンプと称さない。
- TXT / Markdown / JSON / CSV / XLSX / SRT / ZIP、入力方法、Driveへの保存とダウンロードは維持。
- `SAVE_OUTPUTS_TO_GOOGLE_DRIVE = False` が既定値。
- 開発は仕様・テスト・最小実装の順。従来版への互換レイヤーは追加しない。

## ローカライズ変更の境界

既存の183言語の翻訳・言語管理・生成プログラム・検査を維持する。モデル固有で事実関係が変わる説明のみ、虚偽のCTC/word timestampサポート表記が残らないよう置換する。翻訳済み一般UIはそのまま維持する。モデル固有の短い英語技術注記は181言語では訳文精査前の暫定表示であり、翻訳完了と同一視しない。

## 生成物の改行コードと決定的ビルド

`.gitattributes` は Notebook・Python・Markdown・JSON の改行を LF に統一する。生成スクリプトでは `Path.write_text(..., newline="\n")` を明示し、Windows の既定 CRLF 変換を回避する。これにより、Windows と Linux のどちらで再生成しても公開済み生成物がバイト単位で一致する。
