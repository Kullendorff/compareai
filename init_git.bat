@echo off
echo =======================================
echo =    Initialize Git Repository        =
echo =======================================
echo.

echo Checking if Git is installed...
git --version > NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git is not installed or not in your PATH.
    echo Please install Git from https://git-scm.com/downloads
    pause
    exit /b
)

echo Initializing Git repository...
git init

echo Adding files to Git...
git add .

echo Check status:
git status

echo.
echo =======================================
echo Repository initialized!
echo.
echo Next steps:
echo 1. Review the files staged for commit
echo 2. Create your first commit with:
echo    git commit -m "Initial commit"
echo 3. Link to your GitHub repository with:
echo    git remote add origin https://github.com/yourusername/ai-assistant.git
echo 4. Push your code with:
echo    git push -u origin main
echo =======================================
echo.

pause