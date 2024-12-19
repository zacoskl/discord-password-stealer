@echo off

:: Start the Python script in the background
start "" builder.pyw

:: Slowly spell out the word "opened" with a smoother and better effect
echo.
timeout /nobreak /t 1 >nul
cls
echo o
timeout /nobreak /t 1 >nul
cls
echo o.
timeout /nobreak /t 1 >nul
cls
echo op
timeout /nobreak /t 1 >nul
cls
echo op.
timeout /nobreak /t 1 >nul
cls
echo ope
timeout /nobreak /t 1 >nul
cls
echo ope.
timeout /nobreak /t 1 >nul
cls
echo open
timeout /nobreak /t 1 >nul
cls
echo open.
timeout /nobreak /t 1 >nul
cls
echo opened
timeout /nobreak /t 1 >nul
cls
echo opened.
timeout /nobreak /t 1 >nul

:: Loop the animation to continue the effect
goto loading
