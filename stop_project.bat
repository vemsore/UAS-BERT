@echo off

echo.
echo Menghentikan Server...

taskkill /F /IM python.exe

taskkill /F /IM uvicorn.exe

echo.

echo Server berhasil dihentikan.

pause