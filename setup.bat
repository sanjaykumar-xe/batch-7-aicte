@echo off
REM Quick setup script for Resume Analyser (Windows)

echo ========================================
echo    Resume Analyser Setup (Windows)
echo ========================================
echo.

REM Check Python
python --version
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Create .streamlit directory
echo Creating .streamlit directory...
if not exist ".streamlit" mkdir .streamlit
echo.

REM Check API keys
echo ========================================
echo    API Key Setup
echo ========================================
echo.

if "%GROQ_API_KEY%"=="" (
    echo [WARNING] GROQ_API_KEY not set
    echo    Get your free key at: https://console.groq.com
) else (
    echo [OK] GROQ_API_KEY is set
)

if "%GEMINI_API_KEY%"=="" (
    echo [WARNING] GEMINI_API_KEY not set
    echo    Get your free key at: https://aistudio.google.com
) else (
    echo [OK] GEMINI_API_KEY is set
)

echo.
echo ========================================
echo    Setup Complete!
echo ========================================
echo.
echo To run the app:
echo   $env:GROQ_API_KEY="your_groq_key"
echo   $env:GEMINI_API_KEY="your_gemini_key"
echo   streamlit run app.py
echo.
pause
