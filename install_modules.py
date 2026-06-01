#!/usr/bin/env python3
"""
Script cài đặt các module Python cần thiết
Chạy: python install_modules.py
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def print_header(text):
    """In tiêu đề"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_step(step_num, text):
    """In bước thực hiện"""
    print(f"\n[{step_num}] {text}")


def print_success(text):
    """In thành công"""
    print(f"✅ {text}")


def print_error(text):
    """In lỗi"""
    print(f"❌ {text}")


def print_info(text):
    """In thông tin"""
    print(f"ℹ️  {text}")


def check_python_version():
    """Kiểm tra phiên bản Python"""
    print_step(1, "Kiểm tra phiên bản Python")
    
    version = sys.version_info
    print(f"   Python: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8+ được yêu cầu")
        sys.exit(1)
    
    print_success(f"Python {version.major}.{version.minor}.{version.micro}")


def check_pip():
    """Kiểm tra pip"""
    print_step(2, "Kiểm tra pip")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            print(f"   {lines[0]}")
            print_success("pip tìm thấy")
            return True
        else:
            print_error("Không thể tìm thấy pip")
            return False
            
    except Exception as e:
        print_error(f"Lỗi kiểm tra pip: {e}")
        return False


def upgrade_pip():
    """Nâng cấp pip"""
    print_step(3, "Nâng cấp pip")
    
    try:
        print("   Đang nâng cấp pip...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            capture_output=True,
            timeout=60
        )
        print_success("pip đã nâng cấp")
        return True
        
    except Exception as e:
        print_error(f"Lỗi nâng cấp pip: {e}")
        return False


def check_requirements_file():
    """Kiểm tra file requirements.txt"""
    print_step(4, "Kiểm tra file requirements.txt")
    
    if not Path("requirements.txt").exists():
        print_error("Không tìm thấy requirements.txt")
        print_info("Chạy script từ thư mục smartbin")
        return False
    
    print_success("requirements.txt tìm thấy")
    
    # Hiển thị nội dung
    print("\n   Các module cần cài:")
    with open("requirements.txt") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                print(f"     - {line}")
    
    return True


def install_requirements():
    """Cài đặt requirements"""
    print_step(5, "Cài đặt modules từ requirements.txt")
    
    try:
        print("   (Cây có thể mất 5-10 phút, vui lòng chờ...)")
        print()
        
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            timeout=600
        )
        
        print_success("Cài đặt requirements hoàn tất")
        return True
        
    except subprocess.TimeoutExpired:
        print_error("Timeout cài đặt (quá lâu)")
        return False
        
    except Exception as e:
        print_error(f"Lỗi cài đặt: {e}")
        return False


def verify_installation():
    """Kiểm tra cài đặt"""
    print_step(6, "Kiểm tra cài đặt")
    
    modules = [
        ("torch", "PyTorch"),
        ("transformers", "Transformers"),
        ("PIL", "Pillow"),
        ("serial", "PySerial")
    ]
    
    all_ok = True
    
    for module_name, display_name in modules:
        try:
            mod = __import__(module_name)
            version = getattr(mod, "__version__", "unknown")
            print(f"   ✅ {display_name:15} v{version}")
            
        except ImportError:
            print(f"   ❌ {display_name:15} NOT FOUND")
            all_ok = False
    
    # Kiểm tra GPU
    print()
    try:
        import torch
        if torch.cuda.is_available():
            device = torch.cuda.get_device_name(0)
            print(f"   ✅ GPU: {device}")
        else:
            print(f"   ℹ️  GPU: Không có (sẽ dùng CPU)")
    except:
        pass
    
    return all_ok


def print_next_steps():
    """In bước tiếp theo"""
    print_header("🎉 HOÀN TẤT!")
    
    os_name = platform.system()
    
    print("""
✅ Cài đặt module thành công!

📚 CÁC BƯỚC TIẾP THEO:

1. Chạy demo:
   python demo.py

2. Phân loại ảnh:
   python waste_classifier.py images/trash.jpg

3. Với servo motor:
   python waste_classifier_servo.py images/trash.jpg COM3

4. Cài thêm (phát triển):
   pip install -r requirements-dev.txt

📖 TÀI LIỆU:
   - README.md           → Tổng quan
   - QUICK_START.md      → Hướng dẫn nhanh
   - SERVO_SETUP.md      → Setup servo
   - INSTALL.md          → Cài đặt chi tiết

🔧 CÀI ĐẶT LẠI:
   - Windows: Double-click install_modules.bat
   - Linux:   bash install_modules.sh
   - Python:  python install_modules.py
    """)
    
    print("=" * 70)
    print("🚀 Sẵn sàng sử dụng SmartBin!")
    print("=" * 70 + "\n")


def main():
    """Hàm chính"""
    
    print_header("🗑️  SMARTBIN - CÀI ĐẶT MODULES PYTHON")
    
    try:
        # Kiểm tra
        check_python_version()
        
        if not check_pip():
            print_error("pip không khả dụng")
            sys.exit(1)
        
        upgrade_pip()
        
        if not check_requirements_file():
            sys.exit(1)
        
        # Cài đặt
        if not install_requirements():
            print_error("Cài đặt không thành công")
            sys.exit(1)
        
        # Xác nhận
        if not verify_installation():
            print_info("Có thể có vài module chưa được cài đầy đủ")
        
        # In bước tiếp theo
        print_next_steps()
        
        return 0
        
    except KeyboardInterrupt:
        print("\n❌ Cài đặt bị hủy bởi người dùng")
        return 1
        
    except Exception as e:
        print_error(f"Lỗi không mong muốn: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
