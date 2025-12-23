@echo off
echo Starting Auto Git Push...
echo This will find all files changed today and commit/push them to git (master branch).
echo Run this daily to push your changes!
echo.

powershell -ExecutionPolicy Bypass -File auto-git-push.ps1

pause
