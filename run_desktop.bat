@echo off
REM Quick start script for desktop mode

echo 🚀 Claude Config Editor - Desktop Mode
echo.

REM Check if venv exists
if not exist "venv\" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate venv
call venv\Scripts\activate.bat

REM Install requirements if needed
python -c "import webview" 2>nul
if errorlevel 1 (
    echo 📥 Installing PyWebView...
    pip install -q -r requirements.txt
    echo.
)

REM Run in desktop mode
python server.py --desktop %*
