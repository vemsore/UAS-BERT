@echo off
title Analisis Sentimen IndoBERT

cd /d "%~dp0"

echo ==========================================
echo MEMULAI PROJECT
echo ==========================================

echo.
echo Menjalankan FastAPI...

start "FastAPI" cmd /k "call .venv\Scripts\activate && uvicorn app.api.main:app --reload"

timeout /t 8 >nul

echo.
echo Menjalankan Dashboard...

start "Dashboard" cmd /k "cd dashboard && python -m http.server 5500"

timeout /t 3 >nul

echo.
echo Membuka Browser...

start http://127.0.0.1:5500

start http://127.0.0.1:8000/docs

echo.
echo ==========================================
echo PROJECT BERHASIL DIJALANKAN
echo ==========================================

pause