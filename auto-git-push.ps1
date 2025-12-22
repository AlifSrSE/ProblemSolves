# Auto Git Push Script
# This script watches for file changes and automatically commits and pushes to git

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = Get-Location
$watcher.Filter = "*.*"
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

$action = {
    $path = $Event.SourceEventArgs.FullPath
    $fileName = $Event.SourceEventArgs.Name
    $changeType = $Event.SourceEventArgs.ChangeType
    
    # Skip .git folder changes
    if ($path -match "\.git") { return }
    
    # Only trigger on file changes (not directories)
    if (Test-Path $path -PathType Leaf) {
        Write-Host "File changed: $fileName" -ForegroundColor Cyan
        
        try {
            # Stage only the specific file that changed
            git add "$fileName"
            git commit -m "Update $fileName"
            git push origin master
            Write-Host "Successfully pushed: $fileName" -ForegroundColor Green
        } catch {
            Write-Host "Error: $_" -ForegroundColor Red
        }
    }
}

Register-ObjectEvent $watcher "Changed" -Action $action | Out-Null
Register-ObjectEvent $watcher "Created" -Action $action | Out-Null

Write-Host "Watching for file changes... Press Ctrl+C to stop." -ForegroundColor Yellow

# Keep the script running
while ($true) { Start-Sleep -Seconds 1 }
