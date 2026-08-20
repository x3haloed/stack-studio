@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0skill_shim.ps1" %*
exit /b %ERRORLEVEL%
