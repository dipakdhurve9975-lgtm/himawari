@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\pythonw.exe" (
  echo First-time setup is needed. Follow the Windows setup steps in README.md.
  pause
  exit /b 1
)
start "" ".venv\Scripts\pythonw.exe" "app.py"
exit /b 0
