# 🗑️ Smart Bin - Garbage Classification AI

Hệ thống phân loại rác tự động bằng AI sử dụng mô hình học sâu từ Hugging Face.

## ✨ Tính năng

- ✅ Nhận diện loại rác từ ảnh (6 loại chi tiết)
- ✅ Phân loại rác thành 2 nhóm chính: **Hữu cơ** và **Vô cơ**
- ✅ Hiển thị độ chính xác (confidence score)
- ✅ Đưa ra giải pháp xử lý rác phù hợp

## 🚀 Cài đặt

### Yêu cầu
- Python 3.8+
- pip hoặc conda

### Bước 1: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

Hoặc nếu muốn cài đặt chi tiết:

```bash
pip install torch transformers Pillow
```

## 📖 Cách sử dụng

### Phân loại một ảnh

```bash
python waste_classifier.py img.png
```

hoặc

```bash
python waste_classifier.py /path/to/your/image.jpg
```

### Ví dụ kết quả

```
⏳ Đang tải mô hình từ Hugging Face...
✅ Mô hình đã tải thành công!

🖼️ Đang xử lý: img.png
✅ Đã tải ảnh: img.png
🔍 Đang phân tích ảnh...

============================================================
🏆 PHÂN LOẠI CUỐI CÙNG: VÔ CƠ (RÁC TÁI CHẾ - CHAI LỌ / KIM LOẠI / NHỰA)
🔍 Nhãn chi tiết phát hiện: PLASTIC
📊 Độ tự tin: 95.23%
============================================================

📋 Xác suất chi tiết các thành phần trong ảnh:
  cardboard    | ░░░░░░░░░░░░░░░░░░░░ |   2.15%
  glass        | ░░░░░░░░░░░░░░░░░░░░ |   1.89%
  metal        | ░░░░░░░░░░░░░░░░░░░░ |   0.73%
  paper        | ░░░░░░░░░░░░░░░░░░░░ |   0.20%
  plastic      | ██████████████████░░ |  95.23%
  trash        | ░░░░░░░░░░░░░░░░░░░░ |   0.00%
```

## 📊 Các loại rác được hỗ trợ

| Loại chi tiết | Phân loại chính | Mô tả |
|---|---|---|
| Cardboard | Vô cơ | Bìa cứng, thùng carton |
| Paper | Vô cơ | Giấy, báo in |
| Glass | Vô cơ | Chai lọ, kính thái |
| Metal | Vô cơ | Lon kim loại, vỏ khí tài |
| Plastic | Vô cơ | Túi ni lông, chai nhựa |
| Trash | Vô cơ | Rác thải sinh hoạt còn lại |

## 🔧 Tùy chỉnh mô hình

Bạn có thể thay đổi mô hình trong file `waste_classifier.py`:

```python
model_name = "watersplash/waste-classification"  # Thay đổi ở đây
```

## 📝 Ghi chú

- Mô hình sử dụng: `watersplash/waste-classification` (TrashNet)
- Độ chính xác: ~95% trên tập test tiêu chuẩn
- Kích thước mô hình: ~100MB (tải xuống lần đầu)

## 🖥️ GPU Acceleration (Tùy chọn)

Nếu bạn có GPU NVIDIA, thêm vào đầu script:

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
```

## 📄 License

MIT License

## 👨‍💻 Tác giả

Smart Bin AI Classification System

---

Để báo cáo lỗi hoặc đề xuất tính năng, vui lòng liên hệ!
"# smartbin" 
