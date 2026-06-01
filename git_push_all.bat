@echo off
REM Git push helper for Windows (run from repo root)
SETLOCAL ENABLEDELAYEDEXPANSION

echo.
echo ==================================================
echo  SmartBin - Git Push All (Windows)
echo ==================================================
echo.

:: Ensure we are in script folder (repo root)
cd /d "%~dp0"

:: Check git
git --version >nul 2>&1
if %errorlevel% neq 0 (
  echo ERROR: Git not found in PATH.
  pause
  exit /b 1
)

:: Optionally set identity
set /p GIT_NAME="Enter Git user.name (leave empty to keep existing): "
if not "%GIT_NAME%"=="" (
  git config user.name "%GIT_NAME%"
  echo Set user.name = %GIT_NAME%
)
set /p GIT_EMAIL="Enter Git user.email (leave empty to keep existing): "
if not "%GIT_EMAIL%"=="" (
  git config user.email "%GIT_EMAIL%"
  echo Set user.email = %GIT_EMAIL%
)

:: Remote URL (optional)
set /p REMOTE_URL="Enter remote URL to add/set (leave empty to use existing origin): "
if not "%REMOTE_URL%"=="" (
  git remote remove origin 2>nul
  git remote add origin %REMOTE_URL%
  echo Remote origin set to %REMOTE_URL%
)

:: Show status
echo.
echo --- Git status ---
git status --porcelain

echo.

:: If no commits, create initial commit
git rev-parse --verify HEAD >nul 2>&1
if %errorlevel% neq 0 (
  echo No commits found. Creating initial commit...
  git add .
  git commit -m "Initial commit"
  if %errorlevel% neq 0 (
    echo ERROR: commit failed. Fix issues and try again.
    pause
    exit /b 1
  )
) else (
  echo Commits exist.
)

:: Ensure branch main
git branch -M main
if %errorlevel% neq 0 (
  echo WARNING: Could not rename/create branch 'main'.
)

:: Push
echo Pushing to origin main...

git push -u origin main
if %errorlevel% neq 0 (
  echo ERROR: push failed. Check remote URL and credentials.
  echo If using HTTPS, ensure credentials or credential manager is configured.
  pause
  exit /b 1
)

echo SUCCESS: Pushed to origin main.
pause
endlocal
