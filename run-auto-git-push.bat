@echo off
echo Starting Auto Git Push...
echo This will find all files changed today and commit each one separately to git (master branch).
echo Each file gets its own commit to boost your GitHub contribution count!
echo Run this daily to push your changes!
echo.

powershell -ExecutionPolicy Bypass -File auto-git-push.ps1

pause
