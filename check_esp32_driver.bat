@echo off
:: Script kiem tra Driver ESP32
:: Chay: run_as_admin.bat hoac chay truc tiep

setlocal enabledelayedexpansion

cls
echo.
echo ============================================================
echo  ^> KIEM TRA DRIVER ESP32
echo ============================================================
echo.

echo [ 1 ] Hien thi tat ca COM ports:
echo.

REM List COM ports
mode con: cols=80 lines=25 >nul
for /f "tokens=1" %%A in ('wmic logicaldisk get name') do (
    if not "%%A"=="Name" echo %%A
)

echo.
echo [ 2 ] Chi tiet COM ports (neu co):
echo.

REM Chi tiet ports
wmic path win32_pnpentity get name,description | find "COM"

echo.
echo [ 3 ] Check Device Manager:
echo.
echo    Chay lenh nay trong PowerShell (admin):
echo    Get-PnpDevice | where {$_.Class -eq "Ports"}
echo.

echo [ 4 ] Kiem tra manual:
echo.
echo    - Nhan Win + R
echo    - Gotype: devmgmt.msc
echo    - Tim "USB-SERIAL CH340" o "Ports"
echo.

echo ============================================================
echo.
echo [ KIEM TRA NHANH ]
echo.
echo  - Neu thay COM port ben tren ^> Driver OK!
echo  - Neu khong thay, hoac "Unknown device" ^> Can cai driver
echo.
echo ============================================================
echo.

REM Check Python serial
echo [ * ] Kiem tra Python pyserial:
echo.
python -c "import serial.tools.list_ports; ports = [f'{p.device}: {p.description}' for p in serial.tools.list_ports.comports()]; print('\n'.join(ports) if ports else 'Khong tim thay port nao')" 2>nul

if %errorlevel% neq 0 (
    echo.
    echo [ ! ] Loi: Python hoac pyserial chua cai
    echo.
    echo    Chay: pip install pyserial
    echo.
)

echo.
echo ============================================================
echo.
pause
