# Auto Git Push Script

This script finds all files changed on the current day and commits each one separately, then pushes them to your git repository. **Each file gets its own commit to increase your GitHub contribution count!**

## Files Created
- `auto-git-push.ps1` - The main PowerShell script that finds and commits daily changes
- `run-auto-git-push.bat` - A simple batch file to easily run the script

## How to Use

### Method 1: Double-click the batch file (Recommended)
1. Double-click `run-auto-git-push.bat`
2. The script will automatically find all files modified or created today
3. For each changed file, it will:
   - Stage the file: `git add "filename"`
   - Commit with message: `git commit -m "Update filename"`
4. Push all commits: `git push origin master`

### Method 2: Manual PowerShell
1. Open PowerShell in this directory
2. Run: `powershell -ExecutionPolicy Bypass -File auto-git-push.ps1`

## Notes
- The script scans ALL files in the current directory and subdirectories
- It automatically ignores changes in the `.git` folder
- Each file changed today gets its own individual commit
- The script uses `master` branch (your repository's current branch)
- Make sure you're in a git repository with a configured remote origin
- Run this script once per day to commit and push that day's changes

## Troubleshooting
- If you get permission errors, try running PowerShell as Administrator
- If git commands fail, check that your repository is properly configured
- The script will show colored output: Yellow for scanning, Green for success, Red for errors, Cyan for each commit