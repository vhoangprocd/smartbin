@echo off
:: Menu Cai dat SmartBin
:: Giup lua chon phuong phap cai dat

cls
echo.
echo ============================================================
echo  ^> SmartBin - Menu Cai dat
echo ============================================================
echo.
echo Lua chon phuong phap cai dat:
echo.
echo   1. [ AUTO ] install_modules.bat (KHUYEN NGHI)
echo      - Tu dong kiem tra va cai dat
echo      - Hien thi chi tiet toan bo qua trinh
echo.
echo   2. [ MANUAL ] install_individual.bat
echo      - Cai dat tung module mot
echo      - Phu hop khi co van de
echo.
echo   3. [ PYTHON ] python install_modules.py
echo      - Chay script Python
echo      - Tuong thich tat ca he dieu hanh
echo.
echo   4. [ CMD ] Cai tay voi pip
echo      - Tuong tac truc tiep
echo      - Cho nguoi advanced
echo.
echo   0. [ EXIT ] Thoat
echo.
echo ============================================================
echo.

set /p choice="Chon phuong phap (0-4): "

if "%choice%"=="1" (
    echo.
    echo [ >> ] Chay install_modules.bat
    echo.
    call install_modules.bat
    exit /b %errorlevel%
    
) else if "%choice%"=="2" (
    echo.
    echo [ >> ] Chay install_individual.bat
    echo.
    call install_individual.bat
    exit /b %errorlevel%
    
) else if "%choice%"=="3" (
    echo.
    echo [ >> ] Chay python install_modules.py
    echo.
    python install_modules.py
    exit /b %errorlevel%
    
) else if "%choice%"=="4" (
    echo.
    echo [ >> ] Che do tay - Cai voi pip
    echo.
    echo [ * ] Cai toan bo:
    echo       pip install -r requirements.txt
    echo.
    echo [ * ] Hoac cai tung module:
    echo       pip install torch
    echo       pip install transformers
    echo       pip install Pillow
    echo       pip install requests
    echo       pip install pyserial
    echo.
    echo [ * ] Kiem tra:
    echo       python install_modules.py
    echo       python setup.py
    echo       python demo.py
    echo.
    pause
    exit /b 0
    
) else if "%choice%"=="0" (
    echo Thoat
    exit /b 0
    
) else (
    echo Lua chon khong hop le!
    pause
    call :menu_cai_dat
    exit /b 1
)

:menu_cai_dat
cls
goto start
