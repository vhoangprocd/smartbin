@echo off
::
:: Script cài đặt các module Python cần thiết
:: Chạy: install_modules.bat
::

echo.
echo ============================================================
echo  ^> SmartBin - Cai dat Module Python
echo ============================================================
echo.

:: Kiểm tra Python đã cài chưa
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ x ] Loi: Python chua duoc cai dat!
    echo.
    echo  * Tai Python tu: https://www.python.org
    echo  * Chon: Add Python to PATH
    echo.
    pause
    exit /b 1
)

echo [ + ] Python tim thay: 
python --version
echo.

:: Kiểm tra pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ x ] Loi: pip khong tim thay!
    echo.
    pause
    exit /b 1
)

echo [ + ] Pip tim thay:
python -m pip --version
echo.

:: Cập nhật pip
echo [ * ] Cap nhat pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo.
    echo [ x ] Loi khi cap nhat pip
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  ^> Cai dat Modules
echo ============================================================
echo.

:: Kiểm tra file requirements.txt
if not exist "requirements.txt" (
    echo.
    echo [ x ] Loi: Khong tim thay file 'requirements.txt'
    echo.
    echo  * Chay script tu thu muc smartbin
    echo.
    pause
    exit /b 1
)

echo [ * ] Doc file requirements.txt...
echo.
type requirements.txt
echo.

:: Cài đặt các module
echo [ * ] Cai dat cac module (co the mat 5-10 phut)...
echo.

python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [ x ] Loi khi cai dat modules!
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  ^> Kiem tra Cai dat
echo ============================================================
echo.

echo [ * ] Kiem tra torch...
python -c "import torch; print('  [+] Torch', torch.__version__)"

echo [ * ] Kiem tra transformers...
python -c "import transformers; print('  [+] Transformers', transformers.__version__)"

echo [ * ] Kiem tra PIL...
python -c "from PIL import Image; print('  [+] Pillow', Image.__version__)"

echo [ * ] Kiem tra serial...
python -c "import serial; print('  [+] PySerial', serial.__version__)"

if %errorlevel% neq 0 (
    echo.
    echo [ ! ] Canh bao: Co the co loi trong khi kiem tra
    echo.
) else (
    echo.
)

:: Kiểm tra GPU (optional)
echo [ * ] Kiem tra GPU (neu co)...
python -c "import torch; print('  [+] GPU:', 'Co (CUDA)' if torch.cuda.is_available() else 'Khong co (CPU only)')"

echo.
echo ============================================================
echo  ^> Hoan tat!
echo ============================================================
echo.
echo [ SUCCESS ] Cai dat module thanh cong!
echo.
echo Ban co the bat dau su dung:
echo   - python waste_classifier.py
echo   - python waste_classifier_servo.py
echo   - python demo.py
echo.
echo Chay 'python setup.py' de kiem tra toan bo he thong
echo.
pause
exit /b 0
