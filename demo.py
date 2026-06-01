"""
Ví dụ toàn bộ hệ thống: Phân loại rác + Servo Motor

Chạy file này để xem tất cả tính năng (không cần ESP32 để test list ports)
"""

import sys
import time
from pathlib import Path


def print_section(title):
    """In tiêu đề phần"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def example_1_classify_image():
    """Ví dụ 1: Phân loại ảnh đơn"""
    print_section("VÍ DỤ 1: Phân loại ảnh rác")
    
    try:
        from waste_classifier import load_model, predict_waste_binary
        
        # Kiểm tra file ảnh test
        test_image = "images/sample.jpg"
        if not Path(test_image).exists():
            print("⚠️  Tạo ảnh test để demo...")
            test_image = "img.png"
            if not Path(test_image).exists():
                print("❌ Không tìm thấy ảnh test")
                print("💡 Đặt file ảnh vào thư mục 'images/' hoặc file 'img.png'")
                return
        
        print(f"\n📷 Chọn ảnh: {test_image}")
        print("📊 Tải mô hình...")
        processor, model = load_model()
        
        print(f"🔍 Phân loại ảnh...")
        result = predict_waste_binary(test_image, processor, model)
        
        if result:
            print(f"\n✅ Kết quả phân loại:")
            print(f"   - Loại: {result['final_category']}")
            print(f"   - Nhãn: {result['original_label']}")
            print(f"   - Độ tự tin: {result['confidence_score']:.2%}")
            return result
        
    except ImportError as e:
        print(f"❌ Lỗi: {e}")
        print("💡 Chuẩn bị: pip install -r requirements.txt")


def example_2_list_serial_ports():
    """Ví dụ 2: Liệt kê các cổng COM"""
    print_section("VÍ DỤ 2: Liệt kê cổng COM (cho ESP32)")
    
    try:
        from servo_controller import get_available_ports
        
        print("🔍 Tìm kiếm cổng COM khả dụng...\n")
        ports = get_available_ports()
        
        if ports:
            print(f"\n✅ Tìm thấy {len(ports)} cổng:")
            for i, (port, desc) in enumerate(ports, 1):
                print(f"   {i}. {port}")
        else:
            print("⚠️  Không tìm thấy cổng COM nào")
            print("💡 Kiểm tra:")
            print("   1. Kết nối USB ESP32")
            print("   2. Driver CH340/CP2102 đã cài?")
            
    except ImportError as e:
        print(f"❌ Lỗi: {e}")
        print("💡 Chuẩn bị: pip install pyserial")


def example_3_test_servo_connection():
    """Ví dụ 3: Kiểm tra kết nối servo"""
    print_section("VÍ DỤ 3: Test kết nối servo (cần ESP32)")
    
    try:
        from servo_controller import ServoController
        
        port = input("\n📱 Nhập cổng COM (mặc định: COM3): ").strip()
        if not port:
            port = "COM3"
        
        print(f"\n🔧 Kiểm tra kết nối {port}...")
        servo = ServoController(port=port)
        
        if servo.connect():
            print("✅ Kết nối thành công!")
            
            # Test commands
            print("\n🧪 Kiểm tra lệnh:")
            
            print("  1️⃣  Center (lệnh: center)...")
            servo.center_servo()
            time.sleep(1)
            
            print("  2️⃣  Xoay trái (lệnh: rotate left)...")
            servo.rotate_servo_left()
            time.sleep(1)
            
            print("  3️⃣  Xoay phải (lệnh: rotate right)...")
            servo.rotate_servo_right()
            time.sleep(1)
            
            print("  4️⃣  Center lại...")
            servo.center_servo()
            
            servo.disconnect()
            print("\n✅ Test hoàn tất!")
            
        else:
            print("❌ Không thể kết nối")
            print("💡 Kiểm tra:")
            print(f"   - Cổng {port} có tồn tại không?")
            print("   - ESP32 đã được nạp code không?")
            print("   - Baud rate 115200?")
            
    except ImportError as e:
        print(f"❌ Lỗi: {e}")


def example_4_classify_and_servo():
    """Ví dụ 4: Phân loại + Servo đầy đủ"""
    print_section("VÍ DỤ 4: Phân loại ảnh + Xoay servo (tích hợp)")
    
    try:
        # Nhập file ảnh
        print("\n📷 Nhập file ảnh:")
        image_file = input("  Đường dẫn ảnh (mặc định: img.png): ").strip()
        if not image_file:
            image_file = "img.png"
        
        if not Path(image_file).exists():
            print(f"❌ Không tìm thấy {image_file}")
            return
        
        # Nhập cổng COM
        print("\n📱 Nhập cổng COM:")
        com_port = input("  Cổng COM (mặc định: COM3): ").strip()
        if not com_port:
            com_port = "COM3"
        
        # Chạy hệ thống
        from waste_classifier_servo import classify_and_control_servo
        
        print(f"\n🚀 Khởi động...")
        print(f"  📷 Ảnh: {image_file}")
        print(f"  🤖 Port: {com_port}")
        
        classify_and_control_servo(image_file, servo_port=com_port)
        
    except ImportError as e:
        print(f"❌ Lỗi: {e}")
    except KeyboardInterrupt:
        print("\n⛔ Đã dừng bởi người dùng")


def main():
    """Menu chính"""
    
    print("\n" + "=" * 70)
    print("🗑️  SMART BIN - HỆ THỐNG PHÂN LoẠI RÁC TỰ ĐỘNG")
    print("=" * 70)
    print("\n📚 DANH SÁCH VÍ DỤ:\n")
    print("  1. Phân loại ảnh rác")
    print("  2. Liệt kê cổng COM (ESP32)")
    print("  3. Test kết nối servo")
    print("  4. Phân loại + xoay servo (đầy đủ)")
    print("  0. Thoát\n")
    
    while True:
        choice = input("🎯 Chọn ví dụ (0-4): ").strip()
        
        if choice == "0":
            print("👋 Tạm biệt!")
            break
        elif choice == "1":
            example_1_classify_image()
        elif choice == "2":
            example_2_list_serial_ports()
        elif choice == "3":
            example_3_test_servo_connection()
        elif choice == "4":
            example_4_classify_and_servo()
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        input("\n📌 Ấn Enter để tiếp tục...")
        print("\n" + "=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Đã thoát!")
        sys.exit(0)
