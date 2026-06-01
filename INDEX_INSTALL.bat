@echo off
:: INDEX CỬ FILE CÀI ĐẶT
:: In danh sách tất cả file cài đặt

cls
echo.
echo ============================================================
echo  ^> DANH SACH TAT CA FILE CAI DAT
echo ============================================================
echo.

echo.
echo [ CHON MOT TRONG CAC PHUONG PHAP ]
echo.
echo 1. TU DONG (KHUYEN NGHI)
echo    - install_modules.bat
echo      ^ Chay: Double-click hoac goi truc tiep
echo      ^ Tuoi dung
echo.

echo 2. INTERACTIVE MENU
echo    - install.bat
echo      ^ Chon phuong phap cai dat
echo.

echo 3. INDIVIDUAL INSTALL
echo    - install_individual.bat
echo      ^ Cai tung module mot
echo      ^ Phu hop khi debug
echo.

echo 4. PYTHON SCRIPT
echo    - install_modules.py
echo      ^ Tuong thich tay ca OS
echo      ^ Chay: python install_modules.py
echo.

echo 5. LINUX/MAC SCRIPT
echo    - install_modules.sh
echo      ^ Chay: bash install_modules.sh
echo.

echo 6. PACKAGE LISTS
echo    - requirements.txt (bat buoc)
echo    - requirements-dev.txt (tuy chon)
echo.

echo 7. TAI LIEU
echo    - 00_INSTALL_FIRST.md (bat dau day)
echo    - INSTALL_GUIDE.md (tom tat)
echo    - INSTALL.md (chi tiet)
echo    - INSTALL_CHECKLIST.md (kiem tra)
echo.

echo ============================================================
echo.
echo  *  CHON PHUONG PHAP:
echo.
echo     [ 1 ] install_modules.bat (TU DONG)
echo     [ 2 ] install.bat (MENU)
echo     [ 3 ] install_individual.bat (DEBUG)
echo     [ 4 ] python install_modules.py (PYTHON)
echo     [ 5 ] bash install_modules.sh (LINUX/MAC)
echo     [ 0 ] Thoat
echo.

set /p choice="Chon: "

if "%choice%"=="1" (
    call install_modules.bat
) else if "%choice%"=="2" (
    call install.bat
) else if "%choice%"=="3" (
    call install_individual.bat
) else if "%choice%"=="4" (
    python install_modules.py
) else if "%choice%"=="5" (
    echo Hay chay: bash install_modules.sh
    pause
) else if "%choice%"=="0" (
    echo Thoat
    exit /b 0
) else (
    echo Lua chon khong hop le
    pause
    goto start
)

pause
exit /b 0
