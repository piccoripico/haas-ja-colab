# Haas Japanese Colab

Third Intelligence **Haas-ja-v1.0**를 사용해 일본어 오디오와 비디오를 전사하는 Google Colab 노트북입니다.

[![Colab에서 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_ko.ipynb)

## 기능

- **무료:** Google Colab의 무료 GPU 런타임에서 실행됩니다.
- **일본어 ASR:** 일본어 음성 인식을 위한 약 6억 매개변수 모델인 [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0)를 사용합니다.
- **빠름:** 전사를 빠르게 처리할 수 있습니다.
- **문장부호:** 모델이 추정한 일본어 문장부호를 출력합니다.
- **타임스탬프와 자막:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **긴 파일 처리:** 긴 오디오 및 비디오 파일도 처리할 수 있습니다.
- **Google Drive 지원:** 파일을 직접 업로드하거나 Google Drive에서 읽을 수 있으며, 출력 ZIP을 선택적으로 Drive에 저장할 수 있습니다.
- **다양한 출력:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest, ZIP.

## 사용법

1. **1. 설정**에서 `INPUT_MODE`를 선택하고 필요하면 다른 설정을 조정합니다.
2. **Runtime → Run all**을 선택합니다.
3. `INPUT_MODE = "upload"`인 경우 **2. 파일 선택 / Google Drive 마운트**에서 파일을 선택합니다.
4. 처리가 끝나면 출력 ZIP이 자동으로 다운로드됩니다.

## 타임스탬프 모드

- `none`: 시간 정보 없음.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## 디코더

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## 긴 파일

`CHUNK_SECONDS`는 긴 파일에 사용하는 내부 청크 길이를 제어합니다. 큰 값은 경계를 줄이고 더 많은 문맥을 보존하지만 각 추론이 더 무거워지고 GPU 메모리를 더 사용할 수 있습니다. 작은 값은 각 추론을 가볍게 하지만 경계를 더 많이 만들어 그 지점 주변의 인식에 영향을 줄 수 있습니다. 대부분의 경우 기본값을 권장합니다.

## 현지화된 UI

ASR 모델 자체는 **일본어 전용**입니다. README와 Colab UI 현지화는 **183개의 활성 ISO 639 Set 1 언어**를 모두 지원합니다(폐기된 `sh` 제외).

영어 (`en`)가 정식 번역 원본입니다. 일본어 (`ja`)는 검토된 번역이며 기본 `README.md` 표시로 저장소 루트에 복사됩니다. 루트의 일본어 README는 번역 원본으로 **사용되지 않습니다**. 나머지 181개 locale은 영어에서 기계 번역됩니다.

## 참고 사항

- GPU를 사용할 수 없으면 노트북은 전사 전에 중지됩니다.
- 처리 시간은 입력 길이, 설정, Colab에서 할당된 GPU에 따라 달라집니다. 첫 실행에서는 NeMo와 약 1.23 GB 모델도 다운로드합니다.
- 긴 오디오는 내부 청크로 처리하므로 청크 경계 주변에서 인식에 영향을 받을 수 있습니다.

## 정식 원본과 생성

번역 가능한 정식 원본:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json`은 동기화된 정식 스냅샷입니다. 일본어는 `locales/ja.json`에서 검토된 번역으로 유지되며 README 스냅샷이 루트 `README.md`에 복사됩니다.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

번역 유지 관리는 일반 CI와 분리됩니다. 일반 사용자와 CI에는 번역 자격 증명이 필요하지 않습니다.

## 라이선스

노트북 스캐폴딩과 빌드/검사 스크립트는 MIT 라이선스입니다. Third Intelligence 모델은 여기에서 재배포되지 않으며 **Apache-2.0**의 적용을 받습니다. 서드파티 종속성은 각자의 라이선스를 유지합니다.
