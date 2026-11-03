# Haas Japanese Colab

Notebook Google Colab สำหรับถอดเสียงและวิดีโอภาษาญี่ปุ่นด้วย Third Intelligence **Haas-ja-v1.0**.

[![เปิดใน Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_th.ipynb)

## คุณสมบัติ

- **ฟรี:** ทำงานบน GPU runtime ฟรีของ Google Colab.
- **ASR ภาษาญี่ปุ่น:** ใช้ [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0) ซึ่งเป็นโมเดลประมาณ 0.6B พารามิเตอร์สำหรับรู้จำเสียงภาษาญี่ปุ่น.
- **รวดเร็ว:** สามารถประมวลผลการถอดเสียงได้อย่างรวดเร็ว.
- **เครื่องหมายวรรคตอน:** โมเดลส่งออกเครื่องหมายวรรคตอนภาษาญี่ปุ่นที่คาดคะเน.
- **Timestamp และคำบรรยาย:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **ประมวลผลไฟล์ยาว:** สามารถประมวลผลไฟล์เสียงและวิดีโอที่ยาวได้ด้วย.
- **รองรับ Google Drive:** อัปโหลดไฟล์โดยตรงหรืออ่านจาก Google Drive; สามารถเลือกบันทึก output ZIP ไปยัง Drive ได้.
- **Output หลายรูปแบบ:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest และ ZIP.

## การใช้งาน

1. เลือก `INPUT_MODE` ใน **1. การตั้งค่า** และปรับการตั้งค่าอื่นตามต้องการ.
2. เลือก **Runtime → Run all**.
3. เมื่อ `INPUT_MODE = "upload"` ให้เลือกไฟล์ใน **2. เลือกไฟล์ / mount Google Drive**.
4. Output ZIP จะดาวน์โหลดอัตโนมัติเมื่อประมวลผลเสร็จ.

## โหมด Timestamp

- `none`: ไม่มีข้อมูลเวลา.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## ไฟล์ยาว

`CHUNK_SECONDS` ควบคุมระยะเวลาของ internal chunk ที่ใช้กับไฟล์ยาว. ค่าที่ใหญ่ขึ้นลด boundaries และเก็บ context ได้มากขึ้น แต่แต่ละ inference หนักขึ้นและอาจใช้ GPU memory มากขึ้น. ค่าที่เล็กลงทำให้ inference เบาลงแต่สร้าง boundaries มากขึ้น ซึ่งอาจกระทบการรู้จำบริเวณนั้น. โดยทั่วไปแนะนำค่า default.

## UI ที่แปลแล้ว

ตัวโมเดล ASR เองรองรับ **ภาษาญี่ปุ่นเท่านั้น**. การแปล README และ Colab UI ครอบคลุม **183 active ISO 639 Set 1 languages** ทั้งหมด (ไม่รวม `sh` ที่เลิกใช้).

English (`en`) เป็น canonical translation source. Japanese (`ja`) เป็น reviewed translation และถูก copy ไปยัง repository root เป็น default `README.md` presentation. Root Japanese README **ไม่ถูกใช้เป็น translation source**. อีก 181 locales ถูก machine translation จาก English.

## หมายเหตุ

- Notebook จะหยุดก่อน transcription หากไม่มี GPU.
- เวลาประมวลผลขึ้นอยู่กับความยาว input, settings และ GPU ที่ Colab จัดสรร. Run แรกจะดาวน์โหลด NeMo และโมเดลประมาณ 1.23 GB ด้วย.
- Audio ยาวถูกประมวลผลเป็น internal chunks ดังนั้น recognition อาจได้รับผลกระทบบริเวณ chunk boundaries.

## Canonical source และ generation

Canonical sources ที่แปลได้:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` เป็น synchronized canonical snapshot. Japanese ถูกดูแลเป็น reviewed translation ใน `locales/ja.json` และ README snapshot ถูก copy ไปยัง root `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Translation maintenance แยกจาก CI ปกติ. ผู้ใช้ทั่วไปและ CI ไม่ต้องใช้ translation credentials.

## License

Notebook scaffolding และ build/check scripts ใช้ MIT license. โมเดล Third Intelligence ไม่ถูก redistribute ที่นี่และอยู่ภายใต้ **Apache-2.0**. Third-party dependencies คง license ของตนเอง.
