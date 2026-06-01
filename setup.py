#!/usr/bin/env python3
"""
Script cài đặt SmartBin Waste Classification System
Chạy lệnh: python setup.py
"""

import os
import subprocess
import sys
from pathlib import Path


def print_header(text):
    """In ra tiêu đề"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_step(step_num, text):
    """In ra bước thực hiện"""
    print(f"\n📍 Bước {step_num}: {text}")


def check_python_version():
    """Kiểm tra phiên bản Python"""
    print_step(1, "Kiểm tra phiên bản Python")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ được yêu cầu. Bạn đang dùng Python {version.major}.{version.minor}")
        sys.exit(1)
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK!")


def check_pip():
    """Kiểm tra pip"""
    print_step(2, "Kiểm tra pip")
    
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()}")
        else:
            print("❌ Không thể tìm thấy pip")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Lỗi kiểm tra pip: {e}")
        sys.exit(1)


def install_dependencies():
    """Cài đặt dependencies"""
    print_step(3, "Cài đặt dependencies")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print(f"❌ Không tìm thấy {requirements_file}")
        sys.exit(1)
    
    print(f"📦 Đang cài đặt từ {requirements_file}...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
                      check=True, timeout=300)
        print("✅ Dependencies cài đặt thành công!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi cài đặt: {e}")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("❌ Timeout cài đặt (quá lâu)")
        sys.exit(1)


def create_directories():
    """Tạo các thư mục cần thiết"""
    print_step(4, "Tạo cấu trúc thư mục")
    
    directories = [
        "images",
        "output",
        "models",
        "logs"
    ]
    
    for directory in directories:
        path = Path(directory)
        path.mkdir(exist_ok=True)
        print(f"  ✅ {path}/")


def test_installation():
    """Kiểm tra cài đặt"""
    print_step(5, "Kiểm tra cài đặt")
    
    try:
        import torch
        print(f"  ✅ PyTorch: {torch.__version__}")
        
        import transformers
        print(f"  ✅ Transformers: {transformers.__version__}")
        
        from PIL import Image
        print(f"  ✅ Pillow: {Image.__version__}")
        
        # Kiểm tra GPU
        if torch.cuda.is_available():
            print(f"  ✅ GPU: {torch.cuda.get_device_name(0)}")
        else:
            print("  ℹ️  GPU: Không có (sẽ dùng CPU)")
        
        print("\n✅ Tất cả dependencies đã cài đặt thành công!")
        
    except ImportError as e:
        print(f"❌ Lỗi import: {e}")
        sys.exit(1)


def print_next_steps():
    """In ra bước tiếp theo"""
    print_header("🎉 CÀI ĐẶT HOÀN TẤT!")
    
    print("""
📚 Bước tiếp theo:

1️⃣  Đặt ảnh rác vào thư mục 'images/' hoặc sử dụng file ảnh của bạn

2️⃣  Chạy phân loại ảnh:
    python waste_classifier.py <đường_dẫn_ảnh>
    
    Ví dụ:
    python waste_classifier.py images/plastic_bottle.jpg

3️⃣  Xem ví dụ sử dụng:
    python example_usage.py

4️⃣  Đọc README:
    README.md

📖 Thông tin thêm:
    - config.py: Tùy chỉnh cấu hình
    - requirements.txt: Danh sách dependencies
    - waste_classifier.py: Module chính

🆘 Nếu gặp lỗi:
    1. Kiểm tra Python 3.8+
    2. Chạy lại: pip install -r requirements.txt
    3. Nếu dùng GPU, cài PyTorch theo hướng dẫn tại pytorch.org

Chúc bạn sử dụng vui vẻ! 🚀
""")


def main():
    """Hàm chính"""
    print_header("🗑️ SMART BIN - WASTE CLASSIFICATION SETUP")
    print("Hệ thống phân loại rác tự động\n")
    
    try:
        check_python_version()
        check_pip()
        install_dependencies()
        create_directories()
        test_installation()
        print_next_steps()
        
    except KeyboardInterrupt:
        print("\n\n❌ Cài đặt bị hủy bởi người dùng")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Lỗi không mong muốn: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
