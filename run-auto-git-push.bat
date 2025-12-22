@echo off
echo Starting Auto Git Push...
echo This will watch for file changes and automatically commit and push to git (master branch).
echo Each file gets its OWN individual commit when changed or created!
echo Press Ctrl+C to stop when you're done.
echo.

powershell -ExecutionPolicy Bypass -File auto-git-push.ps1

pause
