"""
Phân loại rác với điều khiển Servo Motor
Tích hợp waste_classifier.py + servo_controller.py
"""

import sys
from pathlib import Path
from waste_classifier import load_model, predict_waste_binary
from servo_controller import WasteServoDispenser


def classify_and_control_servo(image_path: str, servo_port: str = "COM3"):
    """
    Phân loại ảnh rác và điều khiển servo tương ứng
    
    Args:
        image_path: Đường dẫn file ảnh
        servo_port: Cổng COM của ESP32 (mặc định: COM3)
    
    Quy luật:
        • Rác VÔ CƠ → Servo quay 90° SANG TRÁI
        • Rác HỮU CƠ → Servo quay 90° SANG PHẢI
    """
    
    print("\n" + "=" * 70)
    print("🗑️  PHÂN LOẠI RÁC + ĐIỀU KHIỂN SERVO")
    print("=" * 70)
    
    # Bước 1: Tải mô hình AI
    print("\n📊 BƯỚC 1: Tải mô hình phân loại...")
    processor, model = load_model()
    
    # Bước 2: Phân loại ảnh
    print("\n🔍 BƯỚC 2: Phân loại ảnh rác...")
    result = predict_waste_binary(image_path, processor, model)
    
    if not result:
        print("❌ Phân loại thất bại!")
        return False
    
    # Bước 3: Khởi tạo servo
    print("\n🤖 BƯỚC 3: Khởi tạo điều khiển servo...")
    dispenser = WasteServoDispenser(port=servo_port)
    
    if not dispenser.initialize():
        print(f"❌ Không thể kết nối ESP32 trên {servo_port}")
        print("💡 Gợi ý:")
        print("   1. Kiểm tra ESP32 đã được nạp code không?")
        print("   2. Kiểm tra cáp USB đã kết nối không?")
        print("   3. Kiểm tra cổng COM có đúng không (chạy: python servo_controller.py)")
        return False
    
    # Bước 4: Điều khiển servo dựa trên kết quả phân loại
    print("\n⚙️ BƯỚC 4: Điều khiển servo...")
    success = dispenser.classify_and_dispense(result)
    
    # Dọn dẹp
    dispenser.cleanup()
    
    if success:
        print("\n" + "=" * 70)
        print("✅ HOÀN TẤT! Servo đã xoay thành công!")
        print("=" * 70)
        return True
    else:
        print("\n❌ Điều khiển servo thất bại!")
        return False


def main():
    """Hàm chính"""
    
    if len(sys.argv) < 2:
        print("⚠️ CÁC H SỬ DỤNG:")
        print(f"   python {sys.argv[0]} <đường_dẫn_ảnh> [cổng_COM]")
        print("\n📌 VÍ DỤ:")
        print(f"   python {sys.argv[0]} img.png")
        print(f"   python {sys.argv[0]} images/trash.jpg COM3")
        print(f"   python {sys.argv[0]} images/plastic.png COM5")
        sys.exit(1)
    
    image_path = sys.argv[1]
    servo_port = sys.argv[2] if len(sys.argv) > 2 else "COM3"
    
    # Kiểm tra file ảnh tồn tại
    if not Path(image_path).exists():
        print(f"❌ Lỗi: Không tìm thấy file '{image_path}'")
        sys.exit(1)
    
    # Chạy phân loại + servo
    classify_and_control_servo(image_path, servo_port=servo_port)


if __name__ == "__main__":
    main()
