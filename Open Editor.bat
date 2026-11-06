@echo off
cd /d "%~dp0"
set QT_QPA_PLATFORM=windows
set QT_OPENGL=software
set QT_ENABLE_HIGHDPI_SCALING=0
"C:\Users\qaim9\miniconda3\python.exe" main.py
if errorlevel 1 pause
