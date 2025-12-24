# Auto Git Push Script
# This script finds all files changed today and commits each one separately, then pushes

$currentDate = Get-Date -Format "yyyy-MM-dd"
$today = Get-Date

Write-Host "Finding files changed on $currentDate..." -ForegroundColor Yellow

$changedFiles = Get-ChildItem -Recurse -File | Where-Object {
    $_.LastWriteTime.Date -eq $today.Date -and $_.FullName -notmatch "\\\.git"
} | ForEach-Object {
    $_.FullName -replace [regex]::Escape((Get-Location).Path + "\"), ""
}

if ($changedFiles.Count -gt 0) {
    Write-Host "Committing each file separately for $currentDate..." -ForegroundColor Green
    $commitCount = 0
    try {
        foreach ($file in $changedFiles) {
            git add "$file"
            git commit -m "$file"
            $commitCount++
            Write-Host "Committed: $file" -ForegroundColor Cyan
        }
        git push origin master
        Write-Host "Successfully pushed $commitCount commits for $currentDate" -ForegroundColor Green
    } catch {
        Write-Host "Error committing/pushing: $_" -ForegroundColor Red
    }
} else {
    Write-Host "No changes found for $currentDate" -ForegroundColor Cyan
}
