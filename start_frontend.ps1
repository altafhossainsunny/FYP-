# PowerShell script to start the frontend
Write-Host "Starting SecureCrop Frontend..." -ForegroundColor Green

# Set working directory
Set-Location "c:\Users\Public\Fyp\SecureCrop\frontend"

# Check if Node.js is available
$nodeExe = "C:\Anaconda3\envs\fyp\node.exe"
if (Test-Path $nodeExe) {
    Write-Host "Using conda Node.js..." -ForegroundColor Yellow
    $env:PATH = "C:\Anaconda3\envs\fyp;C:\Anaconda3\envs\fyp\Scripts;" + $env:PATH
} else {
    Write-Host "Using system Node.js..." -ForegroundColor Yellow
}

# Install dependencies if node_modules doesn't exist
if (!(Test-Path "node_modules")) {
    Write-Host "Installing dependencies..." -ForegroundColor Cyan
    npm install
}

# Start the development server
Write-Host "Starting development server..." -ForegroundColor Green
npm run dev

pause