# Haas Japanese Colab

Notebook Google Colab để chép lời âm thanh và video tiếng Nhật bằng Third Intelligence **Haas-ja-v1.0**.

[![Mở trong Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_vi.ipynb)

## Tính năng

- **Miễn phí:** Chạy trên môi trường GPU miễn phí của Google Colab.
- **ASR tiếng Nhật:** Sử dụng [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), mô hình khoảng 0,6 tỷ tham số cho nhận dạng giọng nói tiếng Nhật.
- **Nhanh:** Quá trình chép lời có thể được xử lý nhanh.
- **Dấu câu:** Mô hình xuất dấu câu tiếng Nhật được ước tính.
- **Mốc thời gian và phụ đề:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Xử lý tệp dài:** Cũng có thể xử lý các tệp âm thanh và video dài.
- **Hỗ trợ Google Drive:** Tải tệp lên trực tiếp hoặc đọc từ Google Drive; có thể tùy chọn lưu ZIP đầu ra vào Drive.
- **Nhiều đầu ra:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest và ZIP.

## Cách sử dụng

1. Chọn `INPUT_MODE` trong **1. Cài đặt** và điều chỉnh các cài đặt khác nếu cần.
2. Chọn **Runtime → Run all**.
3. Với `INPUT_MODE = "upload"`, chọn tệp trong **2. Chọn tệp / gắn Google Drive**.
4. ZIP đầu ra được tự động tải xuống sau khi xử lý xong.

## Chế độ mốc thời gian

- `none`: không có thông tin thời gian.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Bộ giải mã

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Tệp dài

`CHUNK_SECONDS` điều khiển thời lượng chunk nội bộ dùng cho tệp dài. Giá trị lớn hơn làm giảm ranh giới và giữ nhiều ngữ cảnh hơn, nhưng khiến mỗi lần suy luận nặng hơn và có thể dùng nhiều bộ nhớ GPU hơn. Giá trị nhỏ hơn làm mỗi lần suy luận nhẹ hơn nhưng tạo nhiều ranh giới hơn, có thể ảnh hưởng nhận dạng quanh các điểm đó. Giá trị mặc định được khuyến nghị trong hầu hết trường hợp.

## Giao diện được bản địa hóa

Bản thân mô hình ASR **chỉ dành cho tiếng Nhật**. Bản địa hóa README và giao diện Colab bao phủ tất cả **183 ngôn ngữ ISO 639 Set 1 đang hoạt động** (loại trừ `sh` đã lỗi thời).

Tiếng Anh (`en`) là nguồn dịch chuẩn. Tiếng Nhật (`ja`) là bản dịch đã được xem xét và được sao chép vào thư mục gốc của kho làm phần trình bày `README.md` mặc định. README tiếng Nhật ở thư mục gốc **không** được dùng làm nguồn dịch. 181 locale còn lại được dịch máy từ tiếng Anh.

## Ghi chú

- Notebook dừng trước khi chép lời nếu không có GPU.
- Thời gian xử lý phụ thuộc vào độ dài đầu vào, cài đặt và GPU được Colab cấp. Ở lần chạy đầu, NeMo và mô hình khoảng 1.23 GB cũng được tải xuống.
- Âm thanh dài được xử lý theo các chunk nội bộ, vì vậy nhận dạng có thể bị ảnh hưởng quanh ranh giới chunk.

## Nguồn chuẩn và tạo sinh

Các nguồn chuẩn có thể dịch:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` là snapshot chuẩn đã đồng bộ. Tiếng Nhật được duy trì như bản dịch đã xem xét trong `locales/ja.json`, và snapshot README của nó được sao chép vào `README.md` ở thư mục gốc.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Việc bảo trì bản dịch tách biệt khỏi CI thông thường. Người dùng thông thường và CI không cần thông tin xác thực dịch thuật.

## Giấy phép

Khung notebook và các script build/check được cấp phép MIT. Mô hình Third Intelligence không được phân phối lại ở đây và chịu **Apache-2.0**. Các phụ thuộc bên thứ ba giữ giấy phép riêng của chúng.
