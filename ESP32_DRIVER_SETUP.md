# 🔌 HƯỚNG DẪN CÀI DRIVER ESP32

## ❓ CÓ PHẢI CÀI DRIVER KHÔNG?

### ✅ **CÓ! Bạn PHẢI cài driver ESP32**

ESP32 cần driver USB để máy tính nhận diện và giao tiếp qua cổng COM.

Nếu không cài driver:
- ❌ Máy tính không thấy ESP32 (Device Manager không có)
- ❌ Arduino IDE không upload được code
- ❌ Python không kết nối được qua serial

---

## 🔍 KIỂM TRA ESP32 CÓ DRIVER KHÔNG

### Bước 1: Cắm ESP32 vào USB

### Bước 2: Mở Device Manager (Windows)

**Cách 1: Nhanh**
```
Nhấn: Win + R
Gõ: devmgmt.msc
Enter
```

**Cách 2: Qua Control Panel**
```
Settings → Device Manager
```

### Bước 3: Kiểm tra

**Trường hợp 1: ✅ Driver đã cài**
```
Ports (COM & LPT)
├── USB-SERIAL CH340 (COM3)
```
👉 **CÓ driver** - Bạn không cần làm gì

**Trường hợp 2: ❌ Chưa cài driver**
```
Other devices (hoặc Unknown devices)
├── CH340 (hoặc CP2102)
```
👉 **CHƯA cài** - Cần cài driver

**Trường hợp 3: ⚠️ Có dấu cảnh báo**
```
Ports (COM & LPT)
├── USB-SERIAL CH340 (COM3) ⚠️
```
👉 **Driver bị lỗi** - Cần gỡ và cài lại

---

## 🔧 CÁCH CÀI DRIVER

**ESP32 có 2 loại driver chính:**

### **Loại 1: CH340 Driver** (Phổ biến nhất)

#### Windows

**Cách 1: Tự động (Khuyến nghị)**
1. Tải: https://www.wch-ic.com/downloads/CH341SER_EXE.html
2. Giải nén file ZIP
3. Double-click `CH341SER.EXE`
4. Nhấn "Install"
5. Restart máy tính
6. Cắm lại ESP32

**Cách 2: Manual**
1. Download driver từ: https://bit.ly/CH340Driver
2. Extract ZIP
3. Chọn folder phù hợp:
   - `WINDOWS.ZIP → CH341SER.EXE` (64-bit)
   - Hoặc 32-bit nếu cần
4. Chạy install
5. Restart

**Cách 3: Windows Update tự động**
1. Cắm ESP32 vào USB
2. Windows sẽ tự tìm driver (~1 phút)
3. Device Manager sẽ hiển thị COM port

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install ch340-dkms

# Fedora
sudo dnf install ch340-dkms

# Hoặc cài qua pip
pip install pyserial
```

#### Mac
```bash
# Homebrew
brew install ch340g-ch34x-usb-driver

# Hoặc download từ: https://github.com/WCHSoftware/ch34x_install_macos
```

---

### **Loại 2: CP2102 Driver** (Ít phổ biến)

#### Windows
1. Tải: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers
2. Chọn "Downloads"
3. Chọn "Windows"
4. Download EXE
5. Chạy install
6. Restart

#### Linux
```bash
# Thường không cần, cài mặc định sẵn
# Nếu cần
sudo apt-get install libusb-1.0-0 libusb-1.0-0-dev
```

#### Mac
```bash
# Download từ: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers
# Chọn "macOS"
# Cài DMG file
```

---

## 🎯 CÁCH XÁC ĐỊNH DRIVER CỦA ESP32

### Bước 1: Tháo vỏ ESP32 (nếu có)

### Bước 2: Tìm chip USB (phía trên ESP32)

**Chip CH340 - Hình chữ nhật, có chữ "CH340"**
```
┌──────────┐
│ CH340    │
│ (chip)   │
└──────────┘
```

**Chip CP2102 - Hình vuông, có chữ "CP2102"**
```
┌──────────┐
│ CP2102   │
│ (chip)   │
└──────────┘
```

### Bước 3: Download driver tương ứng

---

## ✅ KIỂM TRA DRIVER ĐÃ CÀI XONG

### Cách 1: Device Manager

```
Device Manager
└─ Ports (COM & LPT)
   └─ USB-SERIAL CH340 (COM3)  ✅
```

### Cách 2: Command Prompt

```bash
# Windows - Liệt kê cổng COM
wmic logicaldisk get name
```

hoặc

```bash
# Python - Kiểm tra cổng COM
python -c "import serial.tools.list_ports; print([p.device for p in serial.tools.list_ports.comports()])"
```

**Kết quả mong đợi:**
```
['COM3', 'COM5']
```

### Cách 3: Arduino IDE

1. Mở Arduino IDE
2. Menu: Tools → Port
3. Nếu thấy "COM3" hoặc tương tự → ✅ OK

---

## 🆘 GẶP LỖI DRIVER

### ❌ Lỗi 1: "Unknown device" ở Device Manager

**Giải pháp:**
1. Right-click → Update driver
2. "Browse my computer"
3. Chọn thư mục driver CH340/CP2102
4. Cài đặt
5. Restart

hoặc

```bash
# Gỡ driver
# Right-click Unknown device → Uninstall device
# Bỏ cái "Delete driver" 
# Rút USB, cắm lại
# Windows update tự động
```

### ❌ Lỗi 2: "COM port không hiển thị"

**Giải pháp:**
1. Kiểm tra USB cable (dùng cable khác)
2. Cắm vào port USB khác
3. Restart máy tính
4. Cài lại driver

### ❌ Lỗi 3: "Permission denied" (Linux)

**Giải pháp:**
```bash
# Thêm user vào group dialout
sudo usermod -a -G dialout $USER

# Rồi logout/login lại
```

### ❌ Lỗi 4: Arduino IDE không thấy COM port

**Giải pháp:**
1. Kiểm tra driver (Device Manager)
2. Chọn Board: Tools → Board → ESP32 Dev Module
3. Tools → Port → Chọn COM port
4. Nếu vẫn không, restart Arduino IDE

---

## 📋 CHECKLIST DRIVER

- [ ] Tải driver (CH340 hoặc CP2102)
- [ ] Cài driver
- [ ] Restart máy tính
- [ ] Cắm ESP32 vào USB
- [ ] Kiểm tra Device Manager (có COM port không)
- [ ] Test với `python servo_controller.py`
- [ ] Device Manager không có dấu cảnh báo

---

## 🔌 CÁC CỔNG USB PHỔ BIẾN

| Cổng | Tốc độ | Cho phép |
|------|--------|---------|
| USB 2.0 | 480 Mbps | Có |
| USB 3.0 | 5 Gbps | Có |
| USB-C | 5-40 Gbps | Có (với adapter) |

**Khuyến nghị:** Dùng USB 2.0 hoặc 3.0 (nhanh, ổn định)

---

## 📱 BẠO RỔ: KIỂM TRA NHANH

```bash
# Bạo rổ 1: Liệt kê ports (Windows)
mode

# Bạo rổ 2: Liệt kê ports (Python)
python -c "import serial.tools.list_ports; print('\n'.join([f'{p.device}: {p.description}' for p in serial.tools.list_ports.comports()]))"

# Bạo rổ 3: Test kết nối
python servo_controller.py
```

---

## 🎯 TÓNG HỢP

| Bước | Hành động | Kết quả |
|------|---------|--------|
| 1 | Cắm ESP32 | Device Manager hiển thị |
| 2 | Tải driver CH340 | File .exe download xong |
| 3 | Cài driver | COM port hiển thị ✅ |
| 4 | Kiểm tra Device Manager | COM3, COM5, vv... |
| 5 | Test Python | `python servo_controller.py` OK ✅ |

---

## 🚀 SAU KHI CÀI DRIVER XONG

```bash
# Liệt kê cổng COM
python servo_controller.py

# Kết nối servo
python waste_classifier_servo.py images/trash.jpg COM3

# Chạy demo
python demo.py
```

---

## 📚 LINK TẢI DRIVER

| Driver | Link |
|--------|------|
| **CH340** | https://www.wch-ic.com/downloads/CH341SER_EXE.html |
| **CP2102** | https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers |
| **Khác** | Google: "[Chip name] driver download" |

---

## ✨ LƯU Ý

- 🔌 Dùng USB cable chất lượng tốt
- 🖇️ Nếu có dấu cảnh báo → Cài lại driver
- 💾 Sau cài driver → Restart máy
- 🔄 Rút/cắm ESP32 lại → Kiểm tra Device Manager
- 🆘 Không rõ chip nào → Tải cả 2 driver

---

**✅ Cần driver? LÀ CÓ - Cài ngay!**

**🎉 Sau cài xong, bạn có thể sử dụng SerialMonitor để debug và kết nối ESP32 từ Python**
