#!/bin/bash

#
# Script cài đặt các module Python cần thiết (Linux/Mac)
# Chạy: bash install_modules.sh
#

echo ""
echo "============================================================"
echo "  > SmartBin - Cai dat Module Python"
echo "============================================================"
echo ""

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "[ x ] Loi: Python3 chua duoc cai dat!"
    echo ""
    echo "  * Linux (Ubuntu/Debian):"
    echo "    sudo apt-get install python3 python3-pip"
    echo ""
    echo "  * Mac (Homebrew):"
    echo "    brew install python3"
    echo ""
    exit 1
fi

echo "[ + ] Python tim thay:"
python3 --version
echo ""

# Kiểm tra pip
if ! command -v pip3 &> /dev/null; then
    echo "[ x ] Loi: pip3 khong tim thay!"
    echo ""
    exit 1
fi

echo "[ + ] Pip tim thay:"
pip3 --version
echo ""

# Cập nhật pip
echo "[ * ] Cap nhat pip..."
pip3 install --upgrade pip
if [ $? -ne 0 ]; then
    echo ""
    echo "[ x ] Loi khi cap nhat pip"
    echo ""
    exit 1
fi

echo ""
echo "============================================================"
echo "  > Cai dat Modules"
echo "============================================================"
echo ""

# Kiểm tra file requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo ""
    echo "[ x ] Loi: Khong tim thay file 'requirements.txt'"
    echo ""
    echo "  * Chay script tu thu muc smartbin"
    echo ""
    exit 1
fi

echo "[ * ] Doc file requirements.txt..."
echo ""
cat requirements.txt
echo ""

# Cài đặt các module
echo "[ * ] Cai dat cac module (co the mat 5-10 phut)..."
echo ""

pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "[ x ] Loi khi cai dat modules!"
    echo ""
    exit 1
fi

echo ""
echo "============================================================"
echo "  > Kiem tra Cai dat"
echo "============================================================"
echo ""

echo "[ * ] Kiem tra torch..."
python3 -c "import torch; print('  [+] Torch', torch.__version__)"

echo "[ * ] Kiem tra transformers..."
python3 -c "import transformers; print('  [+] Transformers', transformers.__version__)"

echo "[ * ] Kiem tra PIL..."
python3 -c "from PIL import Image; print('  [+] Pillow', Image.__version__)"

echo "[ * ] Kiem tra serial..."
python3 -c "import serial; print('  [+] PySerial', serial.__version__)"

if [ $? -ne 0 ]; then
    echo ""
    echo "[ ! ] Canh bao: Co the co loi trong khi kiem tra"
    echo ""
else
    echo ""
fi

# Kiểm tra GPU (optional)
echo "[ * ] Kiem tra GPU (neu co)..."
python3 -c "import torch; print('  [+] GPU:', 'Co (CUDA)' if torch.cuda.is_available() else 'Khong co (CPU only)')"

echo ""
echo "============================================================"
echo "  > Hoan tat!"
echo "============================================================"
echo ""
echo "[ SUCCESS ] Cai dat module thanh cong!"
echo ""
echo "Ban co the bat dau su dung:"
echo "  - python3 waste_classifier.py"
echo "  - python3 waste_classifier_servo.py"
echo "  - python3 demo.py"
echo ""
echo "Chay 'python3 setup.py' de kiem tra toan bo he thong"
echo ""
