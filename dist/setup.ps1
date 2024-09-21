# Đường dẫn đến file add_vps.exe
$exePath = "C:\Users\hoangks5\Desktop\socket-client\dist\add_vps.exe"

# Tạo shortcut trong thư mục Startup
$shortcutPath = [System.IO.Path]::Combine($env:APPDATA, "Microsoft\Windows\Start Menu\Programs\Startup\add_vps.lnk")

$wshShell = New-Object -ComObject WScript.Shell
$shortcut = $wshShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $exePath
$shortcut.WorkingDirectory = [System.IO.Path]::GetDirectoryName($exePath)
$shortcut.Save()

Write-Host "Shortcut created and application will start with Windows."
