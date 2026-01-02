@echo off
title ENVYYY Rocket League Macro
cd /d "%~dp0"

echo ==========================================
echo        ENVYYY ROCKET LEAGUE MACRO
echo ==========================================
echo.

REM --- Use venv python directly (most reliable) ---
set VENV_PY=%~dp0venv\Scripts\python.exe

if not exist "%VENV_PY%" (
    echo [ERROR] venv not found at: %VENV_PY%
    echo Make sure your venv folder is named "venv"
    echo.
    pause
    exit /b
)

echo Checking dependencies...
"%VENV_PY%" -m pip install --upgrade pip >nul 2>&1
"%VENV_PY%" -m pip install keyboard mouse pygame plyer >nul 2>&1

echo Starting macro...
"%VENV_PY%" "%~dp0Main_Macros.py"

echo.
echo ==========================================
echo   Macro stopped. Press any key to exit.
echo ==========================================
pause >nul