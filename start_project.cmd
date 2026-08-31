@echo off
cd /d "%~dp0"
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_project.ps1" %*
if errorlevel 1 (
  echo.
  echo DentalV8 failed to start. Review the message above.
  pause
)
