@echo off
echo ===============================================
echo =    AI Assistant - Multiple AI Query Tool    =
echo ===============================================
echo.

echo Checking Python installation...
python --version > NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

echo Installing required packages...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install required packages.
    pause
    exit /b
)
echo.

echo Starting AI Assistant...
python app.py
if %ERRORLEVEL% NEQ 0 (
    echo An error occurred while running the application.
    pause
)
