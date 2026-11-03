# ローカライズ保守

## 基本方針

翻訳sourceは **英語 (`en`)** です。

- 正本README: `source/README.en.md`
- 正本Notebook: `notebooks/Haas_Japanese_Colab_en.ipynb`
- canonical locale snapshot: `locales/en.json`
- 日本語表示: `locales/ja.json` (`reviewed`) → root `README.md`

root `README.md` は日本語の既定表示ですが、翻訳sourceではありません。

公開対象は `localization/set1_languages.json` のactive ISO 639 Set 1全183言語です。翻訳helperや翻訳サービスの対応範囲は公開scopeを変更しません。

## 状態

最終完成状態:

- `en`: `canonical`
- `ja`: `reviewed`
- その他181言語: `machine-translated`
- `pending` / stale: **0**

機械翻訳版はレビュー推奨であり、レビューしていない言語を `reviewed` と表示しません。

## 英語正本を変更した場合

1. `source/README.en.md` または英語Notebookを編集する。
2. `python scripts/sync_from_english.py` を実行する。
3. staleになった英語以外の翻訳を保守作業として更新する。
4. 日本語reviewed localeがfreshであることを確認する。
5. `python scripts/build_languages.py`、`build_notebooks.py`、`build_readmes.py` を実行する。
6. `python scripts/check_repository.py` とテストを実行する。

freshnessは `canonical_source_sha256` でfail-closedに検証します。

## 181言語の英語正本再翻訳と最終化

英語正本への移行後、旧ja-canonical構成に基づく181言語の翻訳は、hashだけを付け替えて再利用してはいけません。旧翻訳本文も保持せず、再翻訳前は `pending` + 空payloadとします。各localeは実際に英語 (`en`) から再翻訳し、成功したlocaleだけを `machine-translated` かつ現在の `canonical_source_sha256` に更新します。失敗したlocaleは `pending` のまま残し、公開成果物を生成しません。

最終化は `scripts/finalize_localization.py` を入口にします。通常の使い方は次の2段階です。

```bash
python scripts/finalize_localization.py --plan
python scripts/finalize_localization.py --translate
```

`--plan` はネットワークや翻訳依存パッケージを使わず、現在の再翻訳対象数を表示します。`--translate` は未完了localeを再開可能な形で翻訳し、その後に生成物再build、全テスト、repository checkerを順に実行します。途中で一部localeが失敗した場合はfail-closedで終了し、最終ZIPは作成しません。成功済みlocaleは保存済みなので、同じコマンドを再実行して続行できます。全gateがGREENになった場合だけ、repositoryの親ディレクトリへ `haas-ja-colab-v1.0.0-set1-183-en-canonical-final.zip` を決定的に生成し、SHA-256を表示します。

最終完成条件は、`en=canonical`、`ja=reviewed`、その他181言語=`machine-translated`、stale/pending=0、Notebook=183、localized README=182、全テストとcheckerがPASSすることです。旧ja-canonical構成由来の翻訳を互換層として残すことはしません。


## 全文翻訳契約

英語canonicalから各localeへの翻訳は**全文翻訳**です。要約、短縮、段落統合、説明項目の削除、低資源言語を理由とした英語自然文の代替残置を行いません。

翻訳時には次を1対1で保持します。

- `source/README.en.md` の全見出し、全段落、全箇条書き、全番号付き手順、全注意書き
- 英語canonical Notebookの `intro_markdown` 全文
- `locales/en.json` の53 placeholder全項目
- Markdownの見出しレベル、箇条書き、番号付きリスト、code fence
- URL、モデルID、変数名、設定値、コマンド、ファイル形式名など翻訳してはいけない技術識別子

自然言語は対象言語へ翻訳し、英語原文の自然言語をそのまま残して「翻訳済み」と扱いません。技術識別子を保持することは未翻訳とは扱いません。翻訳は現在の英語canonicalだけを入力とし、旧183言語版の訳文、translation memory、旧canonical payloadは入力に使用しません。

各localized READMEのColabリンクは、そのlocale自身の `notebooks/Haas_Japanese_Colab_<code>.ipynb` を指します。したがって英語READMEの `_en.ipynb` URLを他localeへ固定コピーしません。Colab badge asset URL、repository path、および対象locale codeの対応をlocale JSONのpayload段階と生成成果物の両方で検証します。build時のlink正規化だけで誤payloadを隠しません。

Notebook code cellへ直接挿入するplaceholderは、英語canonicalが持つPython構文上の役割を保持します。canonical値が `#` で始まるplaceholderは、翻訳後も対応するコメント接頭辞（`#`、`# @markdown`、`# @title` など）を維持します。completed localeは生成Notebookの全code cellが `ast.parse` 相当のsyntax検証を通過しなければなりません。

完成版の各 `machine-translated` localeは `translation_source` を `Full translation machine-generated from English canonical source; review recommended.` に統一し、英語canonicalからの全文機械翻訳であることとレビュー推奨であることを明記します。旧表現との互換・aliasは持ちません。

## 通常CI

通常CIでは翻訳を行いません。完成版では次を検証します。

- active Set 1 = 183
- locale = 183
- `en` canonical = 1 / `ja` reviewed = 1 / その他 machine-translated = 181
- pending / stale = 0
- root `README.md` = freshな `ja` localeのREADME
- Notebook = 183
- localized README = 182 + root日本語README = 183
- 全locale freshness
- notebook syntax / Colab form metadata / empty outputs
- 生成物の決定性
- privacy / secret / local-path invariants
