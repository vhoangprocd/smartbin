# 🚀 HƯỚNG DẪN NHANH - QUICK START

## ⚡ Bắt đầu trong 5 phút

### 1️⃣ Cài đặt (Lần đầu tiên)

```bash
# Cài đặt tự động (Khuyến nghị)
python setup.py
```

Hoặc cài đặt thủ công:

```bash
# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 2️⃣ Kiểm tra cài đặt

```bash
# Kiểm tra Python
python --version

# Kiểm tra các package
python -c "import torch; import transformers; print('✅ OK!')"
```

### 3️⃣ Phân loại ảnh đầu tiên

```bash
# Thay 'your_image.jpg' bằng tệp ảnh của bạn
python waste_classifier.py your_image.jpg
```

---

## 📋 Menu lệnh

```bash
# Phân loại một ảnh
python waste_classifier.py path/to/image.jpg

# Xem các ví dụ
python example_usage.py

# Cài đặt lại/cập nhật
python setup.py
```

---

## 🎯 Các ví dụ sử dụng

### Ví dụ 1: Phân loại ảnh từ thư mục hiện tại

```bash
python waste_classifier.py img.png
```

### Ví dụ 2: Phân loại ảnh từ tệp cụ thể

```bash
python waste_classifier.py C:\Users\Admin\Pictures\trash.jpg
```

### Ví dụ 3: Phân loại ảnh từ thư mục images

```bash
python waste_classifier.py images/plastic_bottle.jpg
```

---

## ❓ Khắc phục sự cố

### ❌ Lỗi: "No module named 'transformers'"

**Giải pháp:**
```bash
pip install transformers torch
```

### ❌ Lỗi: "File not found"

**Giải pháp:**
- Kiểm tra tên file có chính xác không
- Kiểm tra file ảnh tồn tại không
- Sử dụng đường dẫn tuyệt đối nếu cần

### ❌ Lỗi: "CUDA out of memory"

**Giải pháp:**
```bash
# Dùng CPU thay vì GPU
# Sửa trong config.py: USE_GPU = False
```

### ⚠️ Cảnh báo: Tải mô hình lâu lần đầu

**Bình thường:**
- Lần đầu tiên: 30-60 giây (tải mô hình ~100MB từ internet)
- Lần sau: <5 giây (sử dụng cache máy tính)

---

## 📊 Kết quả đầu ra

```
============================================================
🏆 PHÂN LOẠI CUỐI CÙNG: VÔ CƠ (RÁC TÁI CHẾ - NHỰA)
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

---

## 🔄 Quy trình hoạt động

```
Ảnh đầu vào
    ↓
[Xử lý ảnh] → Chuyển sang RGB, kiểm tra kích thước
    ↓
[Tải mô hình] → Load từ Hugging Face (lần đầu tiên)
    ↓
[Dự đoán] → AI phân tích ảnh, tính xác suất
    ↓
[Mapping] → Chuyển 6 nhãn thành 2 nhóm (Hữu cơ/Vô cơ)
    ↓
Kết quả phân loại + Độ tự tin
```

---

## 📁 Cấu trúc thư mục

```
smartbin/
├── waste_classifier.py      # 🔴 File chính - Chạy đây!
├── config.py                # ⚙️ Cấu hình
├── requirements.txt         # 📦 Danh sách thư viện
├── setup.py                 # 🔧 Cài đặt tự động
├── example_usage.py         # 📖 Ví dụ sử dụng
├── README.md                # 📚 Tài liệu đầy đủ
├── QUICK_START.md           # ⚡ Hướng dẫn này
├── images/                  # 📷 Đặt ảnh ở đây
├── output/                  # 💾 Kết quả đầu ra
├── models/                  # 🤖 Mô hình (tự động tải)
└── logs/                    # 📝 Nhật ký hoạt động
```

---

## 💡 Mẹo hay

### Tạo ảnh shortcut trên Windows

```batch
@echo off
python waste_classifier.py %1
pause
```

Lưu thành `run.bat`, sau đó kéo thả ảnh vào để phân loại!

### Xử lý nhiều ảnh

```bash
# Tạo vòng lặp (PowerShell)
Get-ChildItem "images" -Include *.jpg, *.png | ForEach-Object {
    python waste_classifier.py $_
}
```

---

## 🆘 Hỗ trợ

- **Tài liệu:** Xem `README.md`
- **Ví dụ:** Chạy `python example_usage.py`
- **Lỗi:** Kiểm tra phần "Khắc phục sự cố" ở trên

---

**🎉 Sẵn sàng? Chạy lệnh này:**

```bash
python waste_classifier.py images/sample.jpg
```

Chúc bạn thành công! 🚀
