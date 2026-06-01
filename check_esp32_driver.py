#!/usr/bin/env python3
"""
Script kiểm tra Driver ESP32
Chạy: python check_esp32_driver.py
"""

import sys
import platform
import subprocess


def print_header(text):
    """In tiêu đề"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_step(text):
    """In bước thực hiện"""
    print(f"\n🔍 {text}")


def print_success(text):
    """In thành công"""
    print(f"✅ {text}")


def print_error(text):
    """In lỗi"""
    print(f"❌ {text}")


def print_warning(text):
    """In cảnh báo"""
    print(f"⚠️  {text}")


def check_pyserial():
    """Kiểm tra pyserial"""
    print_step("Kiểm tra pyserial...")
    
    try:
        import serial.tools.list_ports
        print_success("pyserial đã cài")
        return True
    except ImportError:
        print_error("pyserial chưa cài")
        print("  Cài: pip install pyserial")
        return False


def list_com_ports():
    """Liệt kê các cổng COM"""
    print_step("Quét các cổng COM khả dụng...")
    
    try:
        import serial.tools.list_ports
        
        ports = list(serial.tools.list_ports.comports())
        
        if not ports:
            print_warning("Không tìm thấy cổng COM nào")
            print("  Kiểm tra:")
            print("    1. ESP32 có cắm vào USB không?")
            print("    2. Driver CH340/CP2102 đã cài không?")
            print("    3. Cable USB có bị hỏng không?")
            return None
        
        print(f"✅ Tìm thấy {len(ports)} cổng COM:\n")
        
        esp32_found = False
        for i, port in enumerate(ports, 1):
            info = f"{port.device:8} | {port.description}"
            
            # Kiểm tra xem có phải ESP32 không
            if any(x in port.description.upper() for x in ['CH340', 'CP210X', 'USB', 'SERIAL']):
                print(f"  [{i}] 🤖 {info} ← Có thể là ESP32")
                esp32_found = True
            else:
                print(f"  [{i}]    {info}")
        
        if not esp32_found:
            print_warning("\nKhông tìm thấy ESP32 trong danh sách")
            print("  Hoặc driver chưa cài, hoặc USB không nhận")
        
        return ports
        
    except Exception as e:
        print_error(f"Lỗi: {e}")
        return None


def check_windows_ports():
    """Kiểm tra COM ports trên Windows"""
    if platform.system() != "Windows":
        return
    
    print_step("Kiểm tra Device Manager (Windows)...")
    
    try:
        result = subprocess.run(
            ['wmic', 'path', 'win32_pnpentity', 'get', 'name,description'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            output = result.stdout
            
            # Tìm các cổng serial
            lines = output.split('\n')
            serial_ports = [l for l in lines if 'COM' in l or 'USB' in l]
            
            if serial_ports:
                print("  Device Manager entries:\n")
                for port in serial_ports:
                    if port.strip():
                        print(f"    {port}")
                        
                        if 'Unknown' in port or '!' in port:
                            print_error("    ⚠️  Có Unknown device - cần gỡ driver!")
            else:
                print_warning("  Không tìm thấy serial ports")
                
    except Exception as e:
        print_warning(f"  Không thể kiểm tra Device Manager: {e}")


def check_linux_ports():
    """Kiểm tra trên Linux"""
    if platform.system() != "Linux":
        return
    
    print_step("Kiểm tra trên Linux...")
    
    try:
        result = subprocess.run(
            ['ls', '-la', '/dev/tty*'],
            capture_output=True,
            text=True
        )
        
        print("  Available TTY devices:")
        for line in result.stdout.split('\n'):
            if 'USB' in line or 'ttyUSB' in line or 'ttyACM' in line:
                print(f"    {line}")
                
    except Exception as e:
        print_warning(f"  Lỗi: {e}")


def test_esp32_connection():
    """Test kết nối ESP32"""
    print_step("Test kết nối ESP32...")
    
    try:
        import serial.tools.list_ports
        import serial
        
        ports = [p.device for p in serial.tools.list_ports.comports()]
        
        if not ports:
            print_warning("Không có cổng COM nào")
            return False
        
        # Chọn cổng đầu tiên
        test_port = ports[0]
        
        print(f"  Thử kết nối {test_port}...")
        
        try:
            ser = serial.Serial(test_port, 115200, timeout=2)
            print_success(f"Kết nối {test_port} thành công!")
            
            # Đọc dữ liệu (nếu có)
            data = ser.read(10)
            if data:
                print(f"  Nhận dữ liệu: {data[:20]}")
            
            ser.close()
            return True
            
        except serial.SerialException as e:
            print_error(f"Không thể kết nối: {e}")
            return False
            
    except Exception as e:
        print_error(f"Lỗi: {e}")
        return False


def print_recommendations():
    """In khuyến nghị"""
    print_header("📋 KHUYẾN NGHỊ")
    
    print("""
1. NẾU KHÔNG THẤY CỔM COM:

   ✅ Kiểm tra:
      - ESP32 có cắm vào USB không?
      - USB cable có tốt không?
      - Cắm vào port USB khác
   
   ✅ Driver:
      - Windows: Cài CH340 driver
      - Mac: Dùng Homebrew hoặc tải từ WCH
      - Linux: Thường có sẵn
   
   ✅ Device Manager (Windows):
      - Mở: devmgmt.msc
      - Tìm "Unknown device"
      - Update driver nếu cần

2. CÀI DRIVER CH340 (WINDOWS - Phổ biến):

   Link: https://www.wch-ic.com/downloads/CH341SER_EXE.html
   
   Bước:
   1. Tải CH341SER.EXE
   2. Giải nén ZIP
   3. Chạy install
   4. Restart máy
   5. Cắm lại ESP32

3. SAU KHI CÀI DRIVER:

   ✅ Chạy lại script này
   ✅ Kiểm tra Device Manager
   ✅ Thử: python servo_controller.py

4. NẾU VẪN CÓ PROBLEM:

   ✅ Gỡ driver cũ:
      Device Manager → Right-click → Uninstall
   
   ✅ Thử cable/port khác
   
   ✅ Cài lại driver từ đầu
    """)


def main():
    """Hàm chính"""
    
    print_header("🤖 KIỂM TRA DRIVER ESP32")
    
    # Thông tin hệ thống
    print(f"\n💻 Hệ điều hành: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {platform.python_version()}")
    
    # Kiểm tra pyserial
    if not check_pyserial():
        print("\n⚠️  Cần cài pyserial trước")
        print("   pip install pyserial")
        return
    
    # Liệt kê COM ports
    ports = list_com_ports()
    
    # Kiểm tra hệ điều hành
    if platform.system() == "Windows":
        check_windows_ports()
    elif platform.system() == "Linux":
        check_linux_ports()
    
    # Test kết nối
    if ports:
        test_esp32_connection()
    
    # In khuyến nghị
    print_recommendations()
    
    print_header("✨ HOÀN TẤT")
    
    print("""
Các bước tiếp theo:

1. Nếu tìm thấy COM port:
   ✅ Cài driver thành công
   ✅ Có thể dùng: python servo_controller.py
   ✅ Hoặc: python waste_classifier_servo.py

2. Nếu không tìm thấy:
   ✅ Cài driver CH340/CP2102
   ✅ Restart máy
   ✅ Chạy lại script này

3. Cần giúp? Xem: ESP32_DRIVER_SETUP.md
    """)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Đã hủy")
        sys.exit(0)
    except Exception as e:
        print_error(f"Lỗi: {e}")
        import traceback
        traceback.print_exc()
