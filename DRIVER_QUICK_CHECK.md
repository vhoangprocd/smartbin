# 🔌 DRIVER ESP32 - TÓM TẮT NHANH

## ❓ CọI DRIVER KHÔNG?

### ✅ **CÓ - Phải cài driver ESP32**

Nếu không cài:
- ❌ Máy không thấy ESP32
- ❌ Arduino IDE upload không được
- ❌ Python không kết nối

---

## 📋 CHECKLIST NHANH

### 1️⃣ Kiểm tra xem đã cài driver chưa

```bash
# Cách 1: Kiểm tra bằng Python
python check_esp32_driver.py

# Cách 2: Kiểm tra bằng Batch script
check_esp32_driver.bat

# Cách 3: Device Manager Windows
Nhấn Win + R → devmgmt.msc → Tìm "USB-SERIAL CH340"
```

**Kết quả:**
- ✅ Thấy "COM3", "COM5", v.v... → **ĐÃ CÀI OK**
- ❌ Thấy "Unknown device" → **CHƯA CÀI**
- ❌ Không thấy gì → **CHƯA CÀI**

---

### 2️⃣ Nếu CHƯA CÀI: Cài driver ngay

#### **Windows (Phổ biến):**

**Bước 1: Tải driver CH340**
```
Link: https://www.wch-ic.com/downloads/CH341SER_EXE.html
```

**Bước 2: Cài đặt**
1. Giải nén ZIP
2. Chạy `CH341SER.EXE`
3. Click "Install"
4. Restart máy

**Bước 3: Kiểm tra**
- Cắm ESP32
- Device Manager sẽ hiển thị COM port ✅

#### **Mac:**
```bash
# Homebrew
brew install ch340g-ch34x-usb-driver

# Hoặc: https://github.com/WCHSoftware/ch34x_install_macos
```

#### **Linux:**
```bash
# Ubuntu
sudo apt-get install ch340-dkms

# Fedora
sudo dnf install ch340-dkms
```

---

### 3️⃣ SAU KHI CÀI DRIVER

```bash
# Kiểm tra
python check_esp32_driver.py

# Nếu OK, kiểm tra kết nối servo
python servo_controller.py

# Hoặc chạy demo
python demo.py
```

---

## 🆘 LỖI THƯỜNG GẶP

| Lỗi | Giải pháp |
|-----|---------|
| "Unknown device" | Gỡ driver → Cài lại |
| Không thấy COM | Kiểm tra cable USB, cài driver |
| COM port bị khóa | Kiểm tra Arduino IDE có mở không |
| Python: "Permission denied" | Linux: `sudo usermod -a -G dialout $USER` |

---

## 🔧 FILES KIỂM TRA DRIVER

| File | Dùng để |
|------|--------|
| `check_esp32_driver.py` | Python - Kiểm tra chi tiết |
| `check_esp32_driver.bat` | Batch - Kiểm tra nhanh |
| `ESP32_DRIVER_SETUP.md` | Hướng dẫn đầy đủ |

---

## ⏱️ THỜI GIAN

- ⏳ Tải driver: 1-2 phút
- ⏳ Cài driver: 1-2 phút
- ⏳ Restart: 2-5 phút
- **Tổng cộng: <10 phút**

---

## 📱 CÓ 2 LOẠI DRIVER PHỔ BIẾN

| Chip | Driver | Link |
|------|--------|------|
| **CH340** | CH240 Driver | https://bit.ly/CH340Driver |
| **CP2102** | Silabs Driver | https://bit.ly/CP2102Driver |

**Cách biết chip nào:** Nhìn bo mạch ESP32, tìm chip USB (phía trên)

---

## 🚀 START HERE

```bash
# Bước 1: Kiểm tra ngay
python check_esp32_driver.py

# Bước 2: Nếu cần cài
# Download từ link trên → Cài → Restart

# Bước 3: Kiểm tra lại
python check_esp32_driver.py

# Bước 4: Chạy app
python waste_classifier_servo.py images/trash.jpg COM3
```

---

**✅ Kết luận: CÓ! Phải cài driver**

**📌 Làm ngay bước 1 (kiểm tra) để biết cần cài không!**
