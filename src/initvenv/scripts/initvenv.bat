@echo off
if "%~1"=="" (
  set "target=%CD%"
) else (
  set "target=%~1"
)

setlocal
"%~dp0initvenv.exe" "%target%"
endlocal
exit /b %ERRORLEVEL%