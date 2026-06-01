# 🔧 HƯỚNG DẪN CÀI ĐẶT MODULES

## 📋 Mục lục
1. [Cài đặt nhanh (Windows)](#cài-đặt-nhanh-windows)
2. [Cài đặt nhanh (Linux/Mac)](#cài-đặt-nhanh-linuxmac)
3. [Cài đặt thủ công](#cài-đặt-thủ-công)
4. [Các module cần thiết](#các-module-cần-thiết)
5. [Troubleshooting](#troubleshooting)

---

## 🚀 Cài đặt nhanh (Windows)

### Cách 1️⃣: Chạy file .bat (Khuyến nghị)

```bash
# Mở Command Prompt ở đây, chạy:
install_modules.bat
```

**Hoặc double-click file `install_modules.bat` trực tiếp**

✅ **Ưu điểm:**
- Tự động check Python & pip
- Hiển thị tiến trình chi tiết
- Kiểm tra GPU
- Thông báo khi hoàn tất

### Cách 2️⃣: Command Line

```bash
# Cách 1
pip install -r requirements.txt

# Cách 2 (toàn bộ)
pip install torch transformers Pillow requests pyserial

# Cách 3 (riêng từng module)
pip install torch
pip install transformers
pip install Pillow
pip install requests
pip install pyserial
```

---

## 🐧 Cài đặt nhanh (Linux/Mac)

### Cách 1️⃣: Chạy file .sh

```bash
# Cấp quyền chạy
chmod +x install_modules.sh

# Chạy
bash install_modules.sh

# Hoặc
./install_modules.sh
```

### Cách 2️⃣: Command Line

```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip
pip3 install -r requirements.txt

# Mac (Homebrew)
brew install python3
pip3 install -r requirements.txt

# Hoặc chỉ pip (không cần sudo)
python3 -m pip install --user -r requirements.txt
```

---

## 📝 Cài đặt thủ công

### 1. Kiểm tra Python

```bash
# Windows
python --version

# Linux/Mac
python3 --version
```

**Yêu cầu: Python 3.8+**

Nếu chưa cài: [Tải Python](https://www.python.org/downloads/)

### 2. Cập nhật pip

```bash
# Windows
python -m pip install --upgrade pip

# Linux/Mac
pip3 install --upgrade pip
```

### 3. Cài từng module

#### 3.1 **PyTorch** (AI framework)

```bash
# CPU only
pip install torch

# GPU (NVIDIA CUDA - nhanh hơn)
# Truy cập: https://pytorch.org/get-started/locally/
# Copy lệnh phù hợp với GPU của bạn
```

#### 3.2 **Transformers** (Hugging Face)

```bash
pip install transformers
```

#### 3.3 **Pillow** (Xử lý ảnh)

```bash
pip install Pillow
```

#### 3.4 **Requests** (HTTP)

```bash
pip install requests
```

#### 3.5 **PySerial** (Nối tiếp ESP32)

```bash
pip install pyserial
```

### 4. Cài toàn bộ từ file

```bash
pip install -r requirements.txt
```

---

## 📦 Các module cần thiết

### Bắt buộc (requirements.txt)

| Module | Phiên bản | Dùng để |
|--------|-----------|--------|
| `torch` | ≥2.0.0 | Deep learning framework |
| `transformers` | ≥4.30.0 | Mô hình AI từ Hugging Face |
| `Pillow` | ≥9.0.0 | Xử lý ảnh |
| `requests` | - | Tải xuống từ internet |
| `pyserial` | ≥3.5 | Kết nối ESP32 qua USB |

### Tùy chọn (requirements-dev.txt)

```bash
# Cài thêm cho phát triển
pip install -r requirements-dev.txt
```

| Module | Dùng để |
|--------|--------|
| `pytest` | Testing & kiểm thử |
| `black`, `flake8` | Code quality |
| `jupyter` | Notebook interActive |
| `flask`, `fastapi` | Web API |
| `opencv-python` | Xử lý ảnh nâng cao |

---

## ✅ Kiểm tra cài đặt

### Kiểm tra từng module

```bash
# Torch
python -c "import torch; print('Torch:', torch.__version__)"

# Transformers  
python -c "import transformers; print('Transformers:', transformers.__version__)"

# Pillow
python -c "from PIL import Image; print('Pillow:', Image.__version__)"

# Serial
python -c "import serial; print('PySerial:', serial.__version__)"

# GPU
python -c "import torch; print('GPU:', 'Có' if torch.cuda.is_available() else 'Không')"
```

### Kiểm tra toàn bộ

```bash
# Windows
python setup.py

# Linux/Mac
python3 setup.py
```

---

## ⚠️ Troubleshooting

### ❌ "Python not found"

**Giải pháp:**
1. Cài Python từ [python.org](https://www.python.org)
2. **Tích chọn: "Add Python to PATH"**
3. Restart Command Prompt

### ❌ "pip: command not found"

**Giải pháp:**
```bash
# Windows
python -m pip install -r requirements.txt

# Linux/Mac
python3 -m pip install -r requirements.txt
```

### ❌ "Could not find a version" (torch)

**Giải pháp:**
```bash
# Nếu torch rất lớn, cài từ PyTorch.org trực tiếp
# Truy cập: https://pytorch.org/get-started/locally/
```

### ❌ "CUDA error" (GPU)

**Giải pháp:**
```bash
# Cài CPU version
pip install torch -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

### ❌ "Timeout" (tải lâu)

```bash
# Tăng timeout
pip install --default-timeout=1000 -r requirements.txt

# Hoặc cài từ từng module
pip install torch
pip install transformers
# ... etc
```

### ❌ "Permission denied" (Linux/Mac)

```bash
# Cách 1: Dùng --user
pip install --user -r requirements.txt

# Cách 2: Dùng sudo (không khuyến nghị)
sudo pip install -r requirements.txt

# Cách 3: Virtual environment (tốt nhất)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ "ModuleNotFoundError" sau khi cài

```bash
# Restart Python interpreter
python
>>> import torch  # Nên hoạt động

# Hoặc restart terminal
```

---

## 🔄 Cập nhật modules

### Cập nhật toàn bộ

```bash
pip install --upgrade -r requirements.txt
```

### Cập nhật từng module

```bash
pip install --upgrade torch
pip install --upgrade transformers
# ... etc
```

---

## 🌐 Proxy (Công ty/Trường)

Nếu ở đằng sau proxy:

```bash
pip install -r requirements.txt \
    --proxy [user:passwd@]proxy.server:port
```

Hoặc tạo file `~/.pip/pip.conf`:

```ini
[global]
proxy = [user:passwd@]proxy.server:port
```

---

## 💡 Tips

### 1. Sử dụng Virtual Environment (khuyến nghị)

```bash
# Windows
python -m venv smartbin_env
smartbin_env\Scripts\activate

# Linux/Mac
python3 -m venv smartbin_env
source smartbin_env/bin/activate

# Sau đó cài
pip install -r requirements.txt
```

### 2. Lưu phiên bản hiện tại

```bash
pip freeze > requirements_lock.txt
```

### 3. Cài từ file khác

```bash
pip install package_name==1.2.3
```

### 4. Xóa package

```bash
pip uninstall package_name
```

---

## 📊 Dung lượng cần thiết

| Module | Dung lượng |
|--------|-----------|
| PyTorch (CPU) | ~500MB |
| Transformers | ~500MB |
| Mô hình AI | ~100-500MB |
| **Tổng cộng** | **~2GB** |

**Yêu cầu tối thiểu:**
- Dung lượng ổ cứng: 5GB
- RAM: 4GB
- Internet: 2-3GB (tải lần đầu)

---

## 🎯 Các file cài đặt

| File | Dùng cho | Cách chạy |
|------|---------|----------|
| `requirements.txt` | Cài cơ bản | `pip install -r requirements.txt` |
| `requirements-dev.txt` | Phát triển | `pip install -r requirements-dev.txt` |
| `install_modules.bat` | Windows | Double-click hoặc `install_modules.bat` |
| `install_modules.sh` | Linux/Mac | `bash install_modules.sh` |
| `setup.py` | Kiểm tra | `python setup.py` |

---

## ✨ Sau khi cài đặt xong

```bash
# Test nhanh
python demo.py

# Chạy ứng dụng
python waste_classifier.py images/trash.jpg

# Với servo
python waste_classifier_servo.py images/trash.jpg COM3
```

---

**🎉 Chúc bạn cài đặt thành công!** 🚀
