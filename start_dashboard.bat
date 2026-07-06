@echo off
title IndoBERT Dashboard

cd /d "%~dp0dashboard"

echo.
echo ==========================================
echo Menjalankan Dashboard...
echo ==========================================
echo.

python -m http.server 5500

pause