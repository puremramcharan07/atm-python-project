@echo off
cd /d "%~dp0web_atm"

echo Starting ATM Application...
echo.

python app.py

echo.
echo ATM application stopped.
pause