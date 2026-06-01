# 📥 HƯỚNG DẪN CÀI ĐẶT MODULES - TÓM TẮT

## 🎯 CHỌN CÁCH CÀI ĐẶT

| Tình huống | Cách làm | Lệnh/File |
|-----------|---------|---------|
| **Chỉ muốn cài nhanh** | Double-click file | `install_modules.bat` |
| **Windows (CMD)** | Chạy lệnh | `pip install -r requirements.txt` |
| **Linux/Mac** | Chạy script | `bash install_modules.sh` |
| **Hoặc Python** | Chạy script | `python install_modules.py` |
| **Cài từng cái một** | Menu interactive | `install_individual.bat` |
| **Chọn phương pháp** | Menu tổng hợp | `install.bat` |

---

## 🚀 CÁC CÁCH CÀI ĐẶT

### ✅ **Cách 1: Windows - Double-Click (DỄ NHẤT)**

```
Đi vào thư mục smartbin
↓
Double-click: install_modules.bat
↓
Chờ hoàn tất (~10 phút)
```

**Ưu điểm:** Tự động, chi tiết, dễ hiểu

---

### ✅ **Cách 2: Windows - Command Line**

```bash
# Mở Command Prompt ở thư mục smartbin
pip install -r requirements.txt
```

**Ưu điểm:** Nhanh, đơn giản

---

### ✅ **Cách 3: Linux/Mac - Bash**

```bash
cd smartbin
bash install_modules.sh
```

**Ưu điểm:** Toàn diện, kiểm tra GPU

---

### ✅ **Cách 4: Python (Mọi OS)**

```bash
python install_modules.py
```

**Ưu điểm:** Không phụ thuộc hệ điều hành

---

### ✅ **Cách 5: Cài từng module (Debug)**

```bash
# Windows
install_individual.bat

# Rồi chọn module muốn cài
```

---

### ✅ **Cách 6: Menu tổng hợp**

```bash
# Windows - Chọn phương pháp
install.bat

# Rồi chọn: 1, 2, 3, hoặc 4
```

---

## 📋 DANH SÁCH FILE CÀI ĐẶT

| File | Hệ điều hành | Dùng để | Chạy thế nào |
|------|-------------|--------|------------|
| `install_modules.bat` | Windows | Cài đầy đủ tự động | Double-click |
| `install_individual.bat` | Windows | Cài từng cái một | Double-click |
| `install.bat` | Windows | Menu chọn phương pháp | Double-click |
| `install_modules.sh` | Linux/Mac | Cài đầy đủ | `bash install_modules.sh` |
| `install_modules.py` | Mọi OS | Cài qua Python | `python install_modules.py` |
| `requirements.txt` | Mọi OS | Danh sách module | `pip install -r requirements.txt` |
| `requirements-dev.txt` | Mọi OS | Module phát triển (tùy) | `pip install -r requirements-dev.txt` |

---

## ✅ KIỂM TRA CÀI ĐẶT

### Sau cài xong, chạy một trong các cách:

```bash
# Cách 1: Chạy setup script
python setup.py

# Cách 2: Chạy install script lại
python install_modules.py

# Cách 3: Chạy demo
python demo.py

# Cách 4: Test từng module
python -c "import torch; print('OK')"
python -c "import transformers; print('OK')"
python -c "import serial; print('OK')"
```

---

## 🎯 QUỸ ĐẠO CÀI ĐẶT

```
1. CẤP QUYỀ (kiểm tra Python 3.8+) ✓
   ↓
2. CẬP NHẬT PIP ✓
   ↓
3. ĐỌC requirements.txt ✓
   ↓
4. CÀI CÁC MODULE:
   - torch (AI framework)
   - transformers (Hugging Face)
   - Pillow (xử lý ảnh)
   - requests (HTTP)
   - pyserial (ESP32) ✓
   ↓
5. KIỂM TRA CÀI ĐẶT ✓
   ↓
6. KIỂM TRA GPU (nếu có) ✓
   ↓
7. HOÀN TẤT! 🎉
```

---

## 📊 THÔNG TIN CÀI ĐẶT

| Metric | Giá trị |
|--------|--------|
| **Thời gian** | 5-10 phút (lần đầu) |
| **Dung lượng internet** | ~2GB |
| **Dung lượng ổ cứng** | ~5GB |
| **RAM cần** | 4GB (tối thiểu), 8GB (khuyến nghị) |
| **Tốc độ mạng cần** | ≥1Mbps |

---

## 🆘 GẶP LỖIQUÝ?

### Lỗi 1: "Python not found"
```bash
# Kiểm tra Python có cài không
python --version

# Nếu không có, tải từ python.org
# Nhớ tích chọn "Add Python to PATH"
```

### Lỗi 2: "pip not found"
```bash
# Thử cách này
python -m pip install -r requirements.txt

# Hoặc cài pip
python -m ensurepip --upgrade
```

### Lỗi 3: Timeout / Tải lâu
```bash
# Cài từng cái, không cài toàn bộ
pip install torch --default-timeout=1000
pip install transformers --default-timeout=1000
```

### Lỗi 4: CUDA error (GPU)
```bash
# Cài CPU version
pip install torch --force-reinstall
# Hoặc từ PyTorch.org
```

---

## 💡 LƯU Ý

- ✅ Lần đầu cài mất thời gian, lần sau nhanh hơn (cache)
- ✅ Mô hình AI lần đầu tải mất 30-60 giây
- ✅ Nếu máy chỉ CPU thì chạy chậm hơn máy GPU
- ✅ Không cần cài module "-dev" nếu chỉ dùng

---

## 🚀 SAU KHI CÀI XONG

```bash
# 1. Chạy demo
python demo.py

# 2. Phân loại ảnh
python waste_classifier.py images/trash.jpg

# 3. Với servo (nếu có)
python waste_classifier_servo.py images/trash.jpg COM3
```

---

## 📚 TÀI LIỆU THÊM

- `00_INSTALL_FIRST.md` - Quick start cài đặt
- `INSTALL.md` - Chi tiết đầy đủ
- `INSTALL_CHECKLIST.md` - Checklist kiểm tra
- `QUICK_START.md` - Hướng dẫn nhanh
- `SERVO_SETUP.md` - Setup servo (nếu cần)

---

**✨ Chúc bạn cài đặt thành công! 🎉**

**Hỗ trợ:** Xem file INSTALL.md nếu gặp vấn đề
