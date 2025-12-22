# Auto Git Push Script

This script automatically monitors file changes and commits/pushes them to your git repository. **Each file gets its own individual commit when changed or created!**

## Files Created
- `auto-git-push.ps1` - The main PowerShell script that watches for file changes
- `run-auto-git-push.bat` - A simple batch file to easily start the watcher

## How to Use

### Method 1: Double-click the batch file (Recommended)
1. Double-click `run-auto-git-push.bat`
2. A PowerShell window will open and start watching for file changes
3. When you save/create any file, it will automatically:
   - Stage ONLY that specific file: `git add "$fileName"`
   - Commit with message `git commit -m "Update $fileName"`
   - Push to `git push origin master`
   - Each file gets its own individual commit!

### Method 2: Manual PowerShell
1. Open PowerShell in this directory
2. Run: `powershell -ExecutionPolicy Bypass -File auto-git-push.ps1`

## Notes
- The script watches ALL files in the current directory and subdirectories
- It automatically ignores changes in the `.git` folder
- Press `Ctrl+C` in the PowerShell window to stop the watcher
- The script uses `master` branch (your repository's current branch)
- Make sure you're in a git repository with a configured remote origin

## Troubleshooting
- If you get permission errors, try running PowerShell as Administrator
- If git commands fail, check that your repository is properly configured
- The script will show colored output: Cyan for file changes, Green for success, Red for errors