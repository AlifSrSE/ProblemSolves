# Auto Git Push Script

This script finds all files changed on the current day and commits/pushes them to your git repository. **Run it daily to push all changes made that day!**

## Files Created
- `auto-git-push.ps1` - The main PowerShell script that finds and commits daily changes
- `run-auto-git-push.bat` - A simple batch file to easily run the script

## How to Use

### Method 1: Double-click the batch file (Recommended)
1. Double-click `run-auto-git-push.bat`
2. The script will automatically find all files modified or created today
3. It will stage, commit, and push all changes with a message like "Daily changes for YYYY-MM-DD"

### Method 2: Manual PowerShell
1. Open PowerShell in this directory
2. Run: `powershell -ExecutionPolicy Bypass -File auto-git-push.ps1`

## Notes
- The script scans ALL files in the current directory and subdirectories
- It automatically ignores changes in the `.git` folder
- The script uses `master` branch (your repository's current branch)
- Make sure you're in a git repository with a configured remote origin
- Run this script once per day to commit and push that day's changes

## Troubleshooting
- If you get permission errors, try running PowerShell as Administrator
- If git commands fail, check that your repository is properly configured
- The script will show colored output: Yellow for scanning, Green for success, Red for errors, Cyan for no changes