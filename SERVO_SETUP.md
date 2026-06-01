# 🤖 HƯỚ DẪN SETUP SERVO MOTOR + ESP32

## 📋 Danh sách liệu cần

### Phần cứng:
- [ ] ESP32 Dev Module (hoặc ESP32-S3, ESP32-C3)
- [ ] Servo motor SG90, MG90S, hoặc tương tự
- [ ] Cáp USB mini để nạp code
- [ ] Dây cáp điện (3 sợi: GND, 5V, Signal)
- [ ] Breadboard (tuỳ chọn)

### Phần mềm:
- [ ] Arduino IDE (tải tại arduino.cc)
- [ ] ESP32 Board Package (qua Board Manager)
- [ ] Thư viện ESP32Servo
- [ ] Thư viện ArduinoJSON (v6 trở lên)
- [ ] Python 3.8+ với pyserial

---

## ⚡ PHẦN 1: Sửa soạn phần cứng

### 1.1 Kết nối Servo với ESP32

```
Servo Motor        ESP32
─────────────────────────
GND (Nâu)    →    GND
VCC (Đỏ)     →    5V
Signal (Vàng) →   GPIO 23
```

**📌 Lưu ý:**
- Luôn kết nối GND trước
- Đừng cắm trực tiếp vào pin 5V mà không có resistor pull-up (mặc dù ESP32 có thể chịu)
- Nếu servo cần công suất cao, dùng nguồn ngoài 5V riêng

### 1.2 Sơ đồ kết nối chi tiết

```
ESP32 DEV MODULE
┌─────────────────┐
│                 │
│    23 (GPIO)───├─── Signal Servo (Vàng)
│    5V ────────├─── VCC Servo (Đỏ)
│    GND ───────├─── GND Servo (Nâu)
│                 │
└─────────────────┘
     │
     USB (để nạp code)
```

---

## 🔧 PHẦN 2: Cài đặt Arduino IDE

### 2.1 Cài đặt Board Support

1. **Mở Arduino IDE**
2. **Vào: File → Preferences**
3. **Dán vào "Additional Board Manager URLs":**
   ```
   https://dl.espressif.com/dl/package_esp32_index.json
   ```
4. **Vào: Tools → Board Manager**
5. **Tìm: "esp32"** → Cài bản mới nhất
6. **Chọn: Tools → Board → ESP32 Dev Module**

### 2.2 Cài đặt Thư viện

1. **Vào: Sketch → Include Library → Manage Libraries**
2. **Cài đặt các thư viện sau:**
   - `ESP32Servo` (tác giả: Kevin Harrington)
   - `ArduinoJson` (tác giả: Benoit Blanchon, v6+)

3. **Xác nhận cài đặt:**
   ```
   Tools → Board → ESP32 Dev Module
   Tools → Port → COM3 (hoặc cổng của bạn)
   Tools → Upload Speed → 115200
   ```

---

## 📝 PHẦN 3: Nạp Code Arduino

### 3.1 Nạp code ESP32

1. **Sao chép toàn bộ code từ `esp32_servo_controller.ino`**
2. **Dán vào Arduino IDE**
3. **Ấn nút Upload (Ctrl+U hoặc mũi tên phải)**
4. **Đợi thông báo "Upload Done"**

### 3.2 Kiểm tra kết nối

1. **Mở Serial Monitor (Tools → Serial Monitor)**
2. **Set Baud Rate: 115200**
3. **Nạp lại code (Upload)**
4. **Bạn sẽ thấy:**
   ```
   ================================
   🤖 ESP32 Servo Controller v1.0
   ================================
   ✅ Khởi tạo thành công!
   📡 Baud Rate: 115200
   🎯 Servo Pin: GPIO23
   ================================
   
   Sẵn sàng nhận lệnh JSON từ Python...
   ```

**✅ Nếu thấy tin nhắn trên → OK!**

---

## 🐍 PHẦN 4: Cài đặt Python & pyserial

### 4.1 Cài đặt pyserial

```bash
pip install pyserial
```

### 4.2 Kiểm tra cổng COM

**Trên Python (nên):**
```bash
python servo_controller.py
```

Bạn sẽ thấy danh sách cổng COM:
```
  - COM3: USB-SERIAL CH340 (Interfaces)
  - COM5: Silicon Labs CP210x USB to UART Bridge
```

**Hoặc trên Windows (Device Manager):**
1. Cắm ESP32 vào USB
2. Mở Device Manager
3. Tìm "Ports (COM & LPT)"
4. Tìm ESP32 (tên có thể chứa "CH340" hoặc "CP210x")
5. Ghi nhớ cổng COM (ví dụ: COM3)

---

## ✅ PHẦN 5: Kiểm tra Servo

### 5.1 Test kết nối servo (từ Python)

```bash
# Đổi COM3 nếu cần
python -c "from servo_controller import test_servo_connection; test_servo_connection('COM3')"
```

**Hoặc chạy trực tiếp:**
```bash
python servo_controller.py
```

**Kết quả mong đợi:**
```
🔍 Kiểm tra kết nối servo trên COM3...
✅ Kết nối thành công!

🧪 Kiểm tra lệnh servo:
  1. Center servo...
  📤 Lệnh gửi: {'action': 'center', 'angle': 90}
  📥 Phản hồi: {"status":"ok","message":"Centered to 90 degrees"...}
  
  2. Xoay trái...
  📤 Lệnh gửi: {'action': 'rotate', 'angle': 0, 'speed': 50, 'direction': 'left'}
  ✅ Servo xoay sang trái!
  
  3. Xoay phải...
  ✅ Servo xoay sang phải!
```

**🎉 Nếu servo xoay → Thành công!**

### 5.2 Troubleshooting

| ❌ Lỗi | ✅ Giải pháp |
|---|---|
| "ModuleNotFoundError: No module named 'serial'" | `pip install pyserial` |
| "SerialException: COMx not found" | Kiểm tra cổng COM trong Device Manager |
| "Servo không xoay" | Kiểm tra công suất cấp cho servo (5V, >500mA) |
| "Garbage characters ở Serial Monitor" | Kiểm tra Baud Rate (phải 115200) |

---

## 🎯 PHẦN 6: Chạy phân loại rác + Servo

### 6.1 Cách sử dụng

```bash
# Cách 1: Phân loại ảnh + Xoay servo (cổng mặc định COM3)
python waste_classifier_servo.py images/trash.jpg

# Cách 2: Chỉ định cổng COM
python waste_classifier_servo.py images/trash.jpg COM5

# Cách 3: Chỉ file trong thư mục hiện tại
python waste_classifier_servo.py img.png
```

### 6.2 Kết quả

```
======================================================================
🗑️  PHÂN LOẠI RÁC + ĐIỀU KHIỂN SERVO
======================================================================

📊 BƯỚC 1: Tải mô hình phân loại...
⏳ Đang tải mô hình từ Hugging Face...
✅ Mô hình đã tải thành công!

🔍 BƯỚC 2: Phân loại ảnh rác...
✅ Đã tải ảnh: images/plastic.jpg
🔍 Đang phân tích ảnh...

============================================================
🏆 PHÂN LOẠI CUỐI CÙNG: VÔ CƠ (RÁC TÁI CHẾ - NHỰA)
🔍 Nhãn chi tiết phát hiện: PLASTIC
📊 Độ tự tin: 95.23%
============================================================

🤖 BƯỚC 3: Khởi tạo điều khiển servo...
✅ Kết nối thành công tới COM3

⚙️ BƯỚC 4: Điều khiển servo...
🤖 Phân loại: VÔ CƠ (Rác tái chế - Nhựa)
   Độ tự tin: 95.23%
🔄 Xoay servo sang TRÁI (90°) cho rác Vô cơ...
📤 Lệnh gửi: {'action': 'rotate', 'angle': 90, 'speed': 50, 'direction': 'left'}

======================================================================
✅ HOÀN TẤT! Servo đã xoay thành công!
======================================================================
```

---

## 📊 Quy luật phân loại + Servo xoay

```
AI phân loại ảnh
    ↓
┌───────────────────────────────┐
│  VÔ CƠ:                       │
│  - Giấy, Bìa cứng             │
│  - Chai lọ, Kim loại, Nhựa    │
│  - Rác thải sinh hoạt         │
│                               │
│  👉 Servo xoay 90° SANG TRÁI  │
└───────────────────────────────┘
                ↓
            Thùng rác
            bên trái
            
────────────────────────────────────

┌───────────────────────────────┐
│  HỮU CƠ:                      │
│  - Rác thực phẩm              │
│  - Lá cây, cỏ                 │
│                               │
│  👉 Servo xoay 90° SANG PHẢI  │
└───────────────────────────────┘
                ↓
            Thùng rác
            bên phải
```

---

## 🔌 Kết nối đa thùng rác (Nâng cao)

Nếu muốn 3-4 thùng rác khác nhau:

```python
# Sửa trong servo_controller.py
if "VÔ CƠ" in final_category and "Giấy" in final_category:
    self.servo.rotate_servo_left(angle=0)      # 0° = Thùng 1
    
elif "VÔ CƠ" in final_category and "Nhựa" in final_category:
    self.servo.rotate_servo_left(angle=90)     # 90° = Thùng 2
    
elif "VÔ CƠ" in final_category:
    self.servo.rotate_servo_left(angle=180)    # 180° = Thùng 3
```

---

## 📚 Tài liệu thêm

- [ESP32 Pinout](https://www.mischianti.org/images/stm32/STM32L432CU.jpg)
- [ESP32Servo Library](https://github.com/madhephaestus/ESP32Servo)
- [ArduinoJSON](https://arduinojson.org/)
- [Servo Motor Tutorial](https://www.arduino.cc/en/Reference/Servo)

---

## 🆘 Hỗ trợ

Nếu gặp vấn đề:

1. **Kiểm tra Serial Monitor** (Tools → Serial Monitor)
2. **Xem log lỗi chi tiết**
3. **Thử reset ESP32** (nút Reset trên bo mạch)
4. **Nạp lại code Arduino**

---

**🎉 Chúc bạn thành công! 🚀**
