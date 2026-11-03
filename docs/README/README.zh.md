# Haas Japanese Colab

使用 Third Intelligence **Haas-ja-v1.0** 转写日语音频和视频的 Google Colab 笔记本。

[![在 Colab 中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_zh.ipynb)

## 功能

- **免费：** 可在 Google Colab 的免费 GPU 运行时中运行。
- **日语 ASR：** 使用 [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0)，这是一个约 6 亿参数的日语语音识别模型。
- **快速：** 可快速处理转写。
- **标点：** 模型会输出估计的日语标点。
- **时间戳与字幕：** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **长文件处理：** 也可以处理较长的音频和视频文件。
- **Google Drive 支持：** 可直接上传文件或从 Google Drive 读取文件；还可选择将输出 ZIP 保存到 Drive。
- **多种输出：** TXT、Markdown、JSON、CSV、XLSX、SRT、manifest 和 ZIP。

## 使用方法

1. 在 **1. 设置** 中选择 `INPUT_MODE`，并根据需要调整其他设置。
2. 选择 **Runtime → Run all**。
3. 当 `INPUT_MODE = "upload"` 时，在 **2. 文件选择 / 挂载 Google Drive** 中选择文件。
4. 处理完成后会自动下载输出 ZIP。

## 时间戳模式

- `none`：不添加时间信息。
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## 解码器

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## 长文件

`CHUNK_SECONDS` 控制处理长文件时使用的内部分块时长。较大的值会减少分块边界并保留更多上下文，但每次推理更重，也可能使用更多 GPU 内存。较小的值会减轻每次推理的负担，但会产生更多边界，可能影响这些位置附近的识别。大多数情况下建议使用默认值。

## 本地化界面

ASR 模型本身**仅支持日语**。README 和 Colab 界面的本地化覆盖全部 **183 种有效的 ISO 639 Set 1 语言**（不包括已废弃的 `sh`）。

英语 (`en`) 是规范翻译源。日语 (`ja`) 是经过审校的翻译，并复制到仓库根目录作为默认的 `README.md` 展示。根目录的日语 README **不会**作为翻译源使用。其余 181 个 locale 均从英语进行机器翻译。

## 注意事项

- 如果没有可用的 GPU，笔记本会在转写前停止。
- 处理时间取决于输入长度、设置以及 Colab 分配的 GPU。首次运行还会下载 NeMo 和约 1.23 GB 的模型。
- 长音频会按内部分块处理，因此在分块边界附近识别可能受到影响。

## 规范源与生成

可翻译的规范源：

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` 是同步后的规范快照。日语作为经过审校的翻译维护在 `locales/ja.json` 中，其 README 快照会复制到根目录的 `README.md`。

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

翻译维护与常规 CI 分离。普通用户和 CI 不需要翻译凭据。

## 许可证

笔记本框架以及构建/检查脚本采用 MIT 许可证。Third Intelligence 模型不会在此重新分发，并受 **Apache-2.0** 约束。第三方依赖保留各自的许可证。
