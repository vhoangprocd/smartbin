# 📋 CHECKLIST CÀI ĐẶT SMARTBIN

## 🔧 PRE-REQUISITES (CẦN CÓ SẴN)

- [ ] Python 3.8+ đã cài
- [ ] Internet kết nối
- [ ] 5GB dung lượng ổ cứng trống

### Kiểm tra:
```bash
python --version
# Kết quả: Python 3.8.x hoặc cao hơn ✅
```

---

## 📦 PHƯƠNG PHÁP CÀI ĐẶT (CHỌN 1)

### Phương pháp 1️⃣: Tự động (KHUYẾN NGHỊ) - Windows
- [ ] Chạy file `install_modules.bat`
- [ ] Đợi hoàn tất (~10 phút)
- [ ] Kiểm tra thông báo "SUCCESS"

### Phương pháp 2️⃣: Tự động - Linux/Mac
```bash
bash install_modules.sh
```
- [ ] Hoàn tất cài đặt

### Phương pháp 3️⃣: Python (Mọi OS)
```bash
python install_modules.py
```
- [ ] Hoàn tất cài đặt

### Phương pháp 4️⃣: Thủ công
```bash
pip install -r requirements.txt
```
- [ ] Hoàn tất cài đặt

---

## ✅ KIỂM CHỨNG CÀI ĐẶT

### Bước 1: Kiểm tra PyTorch
```bash
python -c "import torch; print('Torch:', torch.__version__)"
```
- [ ] Hiển thị phiên bản torch (VD: 2.0.1)

### Bước 2: Kiểm tra Transformers
```bash
python -c "import transformers; print('Transformers:', transformers.__version__)"
```
- [ ] Hiển thị phiên bản transformers (VD: 4.30.2)

### Bước 3: Kiểm tra Pillow
```bash
python -c "from PIL import Image; print('Pillow OK')"
```
- [ ] Hiển thị "Pillow OK"

### Bước 4: Kiểm tra PySerial
```bash
python -c "import serial; print('PySerial OK')"
```
- [ ] Hiển thị "PySerial OK"

### Bước 5: Kiểm tra GPU (tùy chọn)
```bash
python -c "import torch; print('GPU:', 'Yes' if torch.cuda.is_available() else 'No')"
```
- [ ] Hiển thị "GPU: Yes" (nếu có GPU) hoặc "GPU: No" (CPU)

---

## 🧪 TEST CHƯƠNG TRÌNH

### Test 1: Demo Menu
```bash
python demo.py
```
- [ ] Mở menu interactive ✅
- [ ] Có các ví dụ để chạy ✅

### Test 2: Phân loại ảnh
```bash
python waste_classifier.py images/sample.jpg
# Hoặc dùng ảnh của bạn
python waste_classifier.py path/to/your/image.jpg
```
- [ ] Mô hình tải thành công (~30s lần đầu) ✅
- [ ] Ảnh được nhận diện ✅
- [ ] Hiển thị kết quả phân loại ✅
- [ ] Độ tự tin được in ra ✅

### Test 3: Liệt kê cổng COM (cho servo)
```bash
python servo_controller.py
```
- [ ] Danh sách các cổng COM hiển thị ✅
- [ ] Tìm thấy ESP32 (chứa "CH340" hoặc "CP210x") ✅

---

## 🔌 CHUẨN BỊ SERVO (NẾU CÓ)

- [ ] ESP32 Dev Module kết nối USB
- [ ] Servo motor nối vào GPIO 23
- [ ] Code Arduino đã nạp: `esp32_servo_controller.ino`
- [ ] Baud rate: 115200

### Test servo:
```bash
python -c "from servo_controller import test_servo_connection; test_servo_connection('COM3')"
```
- [ ] Servo xoay thành công ✅

---

## 🚀 CHẠY ỨNG DỤNG CHÍNH

### Lựa chọn 1: Chỉ phân loại ảnh
```bash
python waste_classifier.py images/trash.jpg
```

### Lựa chọn 2: Phân loại + Servo
```bash
python waste_classifier_servo.py images/trash.jpg COM3
# Thay COM3 bằng cổng ESP32 của bạn
```

### Lựa chọn 3: Chạy demo
```bash
python demo.py
```

---

## 📚 TÀI LIỆU THAM KHẢO

- [ ] Đã đọc `00_INSTALL_FIRST.md`
- [ ] Đã đọc `QUICK_START.md`
- [ ] Đã đọc `README.md`
- [ ] Đã đọc `INSTALL.md` (chi tiết)
- [ ] Đã đọc `SERVO_SETUP.md` (nếu dùng servo)

---

## ⚠️ TROUBLESHOOT

### Gặp lỗi "ModuleNotFoundError"?
- [ ] Chạy lại `install_modules.bat` hoặc `pip install -r requirements.txt`
- [ ] Kiểm tra `INSTALL.md` phần Troubleshooting

### Servo không xoay?
- [ ] Kiểm tra cổng COM đúng không
- [ ] Chạy `python servo_controller.py` để liệt kê
- [ ] Xem `SERVO_SETUP.md` để debug

### Yêu cầu thêm module?
```bash
pip install <package_name>
```

---

## ✨ HOÀN TẤT

- [ ] Toàn bộ checklist đã hoàn tất ✅
- [ ] Có thể chạy `python waste_classifier.py` ✅
- [ ] Nếu có servo: `python waste_classifier_servo.py` ✅
- [ ] Sẵn sàng sử dụng SmartBin 🎉

---

**📝 Ghi chú:**
- Lần đầu tải mô hình AI mất 30-60 giây
- Lần sau sẽ nhanh hơn (sử dụng cache)
- Nếu máy chỉ có CPU, tốc độ sẽ chậm hơn máy có GPU

**🆘 Cần giúp?**
Xem file `INSTALL.md` hoặc `SERVO_SETUP.md`

---

**🎉 Chúc bạn cài đặt thành công! 🚀**
