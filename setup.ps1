# Kiểm tra Python đã được cài đặt chưa
$pythonInstalled = Get-Command "python" -ErrorAction SilentlyContinue

if ($pythonInstalled) {
    # Python đã được cài đặt
    Write-Host "Python is already installed. Skipping installation."
} else {
    # Đường dẫn để tải Python từ trang chính thức
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"

    # Đường dẫn lưu file cài đặt
    $pythonInstallerPath = Join-Path -Path $env:TEMP -ChildPath "python-installer.exe"

    # Tải xuống Python installer
    Write-Host "Downloading Python installer..."
    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath

    # Đường dẫn cài đặt Python
    $pythonInstallPath = "C:\Python311"

    # Cài đặt Python không yêu cầu tương tác
    Write-Host "Installing Python..."
    Start-Process -FilePath $pythonInstallerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 TargetDir=$pythonInstallPath" -Wait

    # Kiểm tra phiên bản Python đã cài đặt
    Write-Host "Checking Python version..."
    python --version

    # Xóa file cài đặt
    Remove-Item $pythonInstallerPath -Force

    Write-Host "Python installation completed."
}

# Cập nhật pip và cài đặt requests
Write-Host "Updating pip..."
python -m pip install --upgrade pip

Write-Host "Installing 'requests' package..."
python -m pip install requests

Write-Host "Python setup completed with pip updated and 'requests' installed."



$currentPath = Get-Location
$downloadUrl = "https://raw.githubusercontent.com/hoangks5/add_vps/refs/heads/main/dist/add_vps.exe"
$destinationPath = Join-Path -Path $currentPath -ChildPath "add_vps.exe"
Invoke-WebRequest -Uri $downloadUrl -OutFile $destinationPath
# Đường dẫn đến file add_vps.exe
$currentPath = Get-Location
# Thêm tên file vào đường dẫn hiện tại
$exePath = Join-Path -Path $currentPath -ChildPath "add_vps.exe"
$currentPath = Get-Location
$configPath = Join-Path -Path $currentPath -ChildPath "config.json"
$configContent = @"
{
    "ip_socket": "3.18.29.6",
    "port_socket": 12345,
    "ip_redis": "3.18.29.6",
    "port_redis": 6379
}
"@
$configContent | Out-File -FilePath $configPath -Encoding UTF8
# Tạo shortcut trong thư mục Startup
$shortcutPath = [System.IO.Path]::Combine($env:APPDATA, "Microsoft\Windows\Start Menu\Programs\Startup\add_vps.lnk")
$wshShell = New-Object -ComObject WScript.Shell
$shortcut = $wshShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $exePath
$shortcut.WorkingDirectory = [System.IO.Path]::GetDirectoryName($exePath)
$shortcut.Save()
Write-Host "Shortcut created and application will start with Windows."
