@echo off
title IndoBERT API

cd /d "%~dp0"

call .venv\Scripts\activate

echo.
echo ==========================================
echo Menjalankan FastAPI...
echo ==========================================
echo.

uvicorn app.api.main:app --reload

pause