@echo off
:: Cai dat tung module mot
:: File nay giup cai dat individual packages de debug

cls
echo.
echo ============================================================
echo  ^> Cai dat Modules (Mode Debug)
echo ============================================================
echo.

set /p response="Ban muon cai toan bo modules? (Y/N): "
if /i "%response%"=="Y" (
    goto install_all
) else if /i "%response%"=="N" (
    goto install_individual
) else (
    echo Lua chon khong hop le!
    pause
    exit /b 1
)

:install_all
echo.
echo [ * ] Cai dat tat ca modules tu requirements.txt
echo.
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [ x ] Loi!
    pause
    exit /b 1
)
echo.
echo [ SUCCESS ] Hoan tat
pause
exit /b 0

:install_individual
echo.
echo Chon module can cai:
echo   1. torch (PyTorch)
echo   2. transformers
echo   3. Pillow (Image processing)
echo   4. requests
echo   5. pyserial
echo   6. All above
echo   0. Cancel
echo.

set /p choice="Chon module (0-6): "

if "%choice%"=="1" (
    echo [ * ] Cai torch...
    python -m pip install torch
) else if "%choice%"=="2" (
    echo [ * ] Cai transformers...
    python -m pip install transformers
) else if "%choice%"=="3" (
    echo [ * ] Cai Pillow...
    python -m pip install Pillow
) else if "%choice%"=="4" (
    echo [ * ] Cai requests...
    python -m pip install requests
) else if "%choice%"=="5" (
    echo [ * ] Cai pyserial...
    python -m pip install pyserial
) else if "%choice%"=="6" (
    echo [ * ] Cai tat ca...
    python -m pip install torch transformers Pillow requests pyserial
) else if "%choice%"=="0" (
    echo Huy bo
    exit /b 0
) else (
    echo Lua chon khong hop le!
    pause
    exit /b 1
)

echo.
echo [ SUCCESS ] Hoan tat
echo.
pause
exit /b 0
