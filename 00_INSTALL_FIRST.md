# 📦 CÀI ĐẶT MODULES

## ⚡ Cách nhanh nhất

### Windows
```bash
# Chạy file này (double-click hoặc qua CMD)
install_modules.bat
```

### Linux / Mac
```bash
bash install_modules.sh
```

### Hoặc dùng Python (mọi hệ điều hành)
```bash
python install_modules.py
```

---

## 📝 Cài thủ công

```bash
# Cách 1: Cài toàn bộ
pip install -r requirements.txt

# Cách 2: Cài từng cái
pip install torch
pip install transformers
pip install Pillow
pip install requests
pip install pyserial
```

---

## ✅ Kiểm tra cài đặt

```bash
# Chạy một trong các file này
python install_modules.py    # Hoặc
python setup.py              # Hoặc
python demo.py
```

---

## 📦 Cài thêm (phát triển - tùy chọn)

```bash
pip install -r requirements-dev.txt
```

---

## 🆘 Gặp vấn đề?

Xem **INSTALL.md** để khắc phục chi tiết

---

**⏱️ Thời gian cài:** 5-10 phút (lần đầu)  
**📊 Dung lượng:** ~2GB  
**🔌 Yêu cầu Internet:** Có

👉 Sau khi cài xong, chạy: `python demo.py`
