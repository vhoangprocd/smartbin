"""
Module điều khiển Servo Motor qua ESP32
Dùng để xoay servo sang trái (90°) nếu rác Vô cơ, 
và xoay sang phải (-90° hoặc 90° ngược lại) nếu rác Hữu cơ
"""

import serial
import time
import json
from pathlib import Path
from typing import Optional, Dict


class ServoController:
    """Điều khiển servo motor qua ESP32 qua kết nối Serial"""
    
    def __init__(self, port: str = "COM3", baudrate: int = 115200, timeout: float = 1.0):
        """
        Khởi tạo kết nối serial với ESP32
        
        Args:
            port: Cổng COM (ví dụ: COM3, /dev/ttyUSB0)
            baudrate: Tốc độ baud (mặc định: 115200)
            timeout: Timeout kết nối (giây)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        self.is_connected = False
        
    def connect(self) -> bool:
        """Kết nối đến ESP32"""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Đợi ESP reset
            self.is_connected = True
            print(f"✅ Kết nối thành công tới {self.port}")
            return True
        except serial.SerialException as e:
            print(f"❌ Lỗi kết nối: {e}")
            return False
    
    def disconnect(self):
        """Ngắt kết nối"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            self.is_connected = False
            print("✅ Ngắt kết nối thành công")
    
    def send_command(self, command: Dict) -> bool:
        """
        Gửi lệnh điều khiển servo tới ESP32
        
        Args:
            command: Dictionary chứa thông tin lệnh
                {
                    "action": "rotate",
                    "angle": 90,
                    "speed": 50,
                    "direction": "left"
                }
        
        Returns:
            True nếu gửi thành công, False nếu thất bại
        """
        if not self.is_connected:
            print("❌ Chưa kết nối đến ESP32")
            return False
        
        try:
            # Chuyển dictionary thành JSON
            json_command = json.dumps(command)
            # Thêm ký tự kết thúc
            json_command += "\n"
            # Gửi qua serial
            self.serial_conn.write(json_command.encode())
            print(f"📤 Lệnh gửi: {command}")
            
            # Chờ nhận phản hồi
            time.sleep(0.5)
            response = self.read_response()
            return True
            
        except Exception as e:
            print(f"❌ Lỗi gửi lệnh: {e}")
            return False
    
    def read_response(self) -> Optional[str]:
        """Đọc phản hồi từ ESP32"""
        try:
            if self.serial_conn.in_waiting:
                response = self.serial_conn.readline().decode().strip()
                if response:
                    print(f"📥 Phản hồi: {response}")
                    return response
        except Exception as e:
            print(f"⚠️ Lỗi đọc phản hồi: {e}")
        return None
    
    def rotate_servo_left(self, angle: int = 90, speed: int = 50) -> bool:
        """
        Xoay servo sang trái
        
        Args:
            angle: Góc xoay (0-180, mặc định 90°)
            speed: Tốc độ xoay (0-255, mặc định 50)
        
        Returns:
            True nếu thành công
        """
        command = {
            "action": "rotate",
            "angle": angle,
            "speed": speed,
            "direction": "left"
        }
        return self.send_command(command)
    
    def rotate_servo_right(self, angle: int = 90, speed: int = 50) -> bool:
        """
        Xoay servo sang phải
        
        Args:
            angle: Góc xoay (0-180, mặc định 90°)
            speed: Tốc độ xoay (0-255, mặc định 50)
        
        Returns:
            True nếu thành công
        """
        command = {
            "action": "rotate",
            "angle": angle,
            "speed": speed,
            "direction": "right"
        }
        return self.send_command(command)
    
    def center_servo(self) -> bool:
        """Đưa servo về vị trí trung tâm (90°)"""
        command = {
            "action": "center",
            "angle": 90
        }
        return self.send_command(command)
    
    def stop_servo(self) -> bool:
        """Dừng servo"""
        command = {
            "action": "stop"
        }
        return self.send_command(command)


class WasteServoDispenser:
    """
    Kết hợp phân loại rác với điều khiển servo
    Tự động xoay servo dựa trên loại rác được phát hiện
    """
    
    def __init__(self, port: str = "COM3", baudrate: int = 115200):
        """
        Khởi tạo hệ thống phân loại + servo
        
        Args:
            port: Cổng COM cổng kết nối ESP32
            baudrate: Tốc độ baud
        """
        self.servo = ServoController(port=port, baudrate=baudrate)
        self.connected = False
    
    def initialize(self) -> bool:
        """Khởi tạo kết nối servo"""
        self.connected = self.servo.connect()
        if self.connected:
            # Center servo khi bắt đầu
            time.sleep(1)
            self.servo.center_servo()
        return self.connected
    
    def classify_and_dispense(self, classification_result: Dict) -> bool:
        """
        Phân loại rác từ kết quả AI và điều khiển servo tương ứng
        
        Args:
            classification_result: Kết quả từ waste_classifier
                {
                    "final_category": "VÔ CƠ (Rác tái chế - Nhựa)",
                    "original_label": "plastic",
                    "confidence_score": 0.95,
                    ...
                }
        
        Returns:
            True nếu điều khiển thành công
        """
        if not self.connected:
            print("❌ Servo chưa được kết nối")
            return False
        
        final_category = classification_result.get("final_category", "")
        confidence = classification_result.get("confidence_score", 0)
        
        print(f"\n🤖 Phân loại: {final_category}")
        print(f"   Độ tự tin: {confidence:.2%}")
        
        # Kiểm tra loại rác
        if "VÔ CƠ" in final_category:
            print("🔄 Xoay servo sang TRÁI (90°) cho rác Vô cơ...")
            return self.servo.rotate_servo_left(angle=90, speed=50)
        
        elif "HỮU CƠ" in final_category:
            print("🔄 Xoay servo sang PHẢI (90°) cho rác Hữu cơ...")
            return self.servo.rotate_servo_right(angle=90, speed=50)
        
        else:
            print("⚠️ Không xác định được loại rác")
            return False
    
    def cleanup(self):
        """Dọn dẹp - đóng kết nối"""
        self.servo.disconnect()


# ============ FUNCTIONS HỰC TIỆN ============

def get_available_ports() -> list:
    """Liệt kê các cổng COM có sẵn"""
    import serial.tools.list_ports
    
    ports = []
    for port, desc, hwid in serial.tools.list_ports.comports():
        ports.append((port, desc))
        print(f"  - {port}: {desc}")
    
    return ports


def test_servo_connection(port: str = "COM3") -> bool:
    """
    Kiểm tra kết nối servo
    
    Args:
        port: Cổng COM cần kiểm tra
    
    Returns:
        True nếu kết nối thành công
    """
    print(f"🔍 Kiểm tra kết nối servo trên {port}...")
    
    servo = ServoController(port=port)
    
    if servo.connect():
        print("✅ Kết nối thành công!")
        
        # Test các lệnh
        print("\n🧪 Kiểm tra lệnh servo:")
        time.sleep(1)
        
        print("  1. Center servo...")
        servo.center_servo()
        time.sleep(1)
        
        print("  2. Xoay trái...")
        servo.rotate_servo_left()
        time.sleep(1)
        
        print("  3. Xoay phải...")
        servo.rotate_servo_right()
        time.sleep(1)
        
        print("  4. Center lại...")
        servo.center_servo()
        
        servo.disconnect()
        return True
    else:
        print("❌ Kết nối thất bại!")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("🔧 KIỂM TRA CỔNG SERIAL CÓ SẴN")
    print("=" * 60)
    
    get_available_ports()
    
    print("\n" + "=" * 60)
    print("✅ Chọn cổng COM của ESP32 và sử dụng trong waste_classifier_servo.py")
    print("=" * 60)
