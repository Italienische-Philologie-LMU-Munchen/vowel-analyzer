# Check for installed Python version
$pythonVersion = python -V 2>&1 | %{$_.ToString().Trim()}
if ($pythonVersion -match "Python (\d+\.\d+\.\d+)") {
    $pythonVersion = $Matches[1]
    Write-Host "Python version $pythonVersion is installed."
} else {
    Write-Host "Python is not installed. Please install Python and try again."
    exit
}

# Install packages from requirements.txt using pip or pip3
if ($pythonVersion -like "2.*") {
    $pipCommand = "pip"
} else {
    $pipCommand = "pip3"
}
Write-Host "Installing packages from requirements.txt using $pipCommand..."
$pipInstallCommand = "$pipCommand install -r requirements.txt"
Invoke-Expression $pipInstallCommand

# Copy files from specified directory to AppData folder
$sourceDirectory = "$(Get-Location)\src"
$destinationDirectory = "$env:APPDATA\VowelAnalyzer"
# Using https://devblogs.microsoft.com/powershell-community/determine-if-a-folder-exists/ 
Write-Host "Check if there is a previous installation of Vowel Anaylzer..."
if (Test-Path -Path $destinationDirectory) 
{
    Write-Host "Emptying $destinationDirectory..."
    # Using code from https://superuser.com/questions/1786887/how-to-delete-all-contents-of-a-folder-without-deleting-the-folder-itself
    Get-ChildItem -Path $destinationDirectory | ForEach-Object -Process { 
        If($_.attributes -eq "Directory"){
            Remove-Item -Path $_.FullName -Recurse -Force;
            }Else{
            Remove-Item -Path $_.FullName -Force;};
            };
}
else 
{
    Write-Host "Creating base directory $destinationDirectory..."
    md -Path $destinationDirectory
}
Write-Host "Copying files from $sourceDirectory to $destinationDirectory..."
Copy-Item -Path "$sourceDirectory\*" -Destination $destinationDirectory -Recurse

# Create shortcut to start Vowel Analyzer on desktop
# Using information from https://community.spiceworks.com/topic/2317514-powershell-how-can-i-change-the-icon-of-a-shortcut-to-a-custom-icon-file-i-have
Write-Host "Creating a shortcut to Vowel Analyzer on Desktop..."
$TargetFile = "$env:APPDATA\VowelAnalyzer\vowelAnalyzer.ps1"
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutFile = "$desktopPath\Vowel Analyzer.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$shortcut = $WScriptShell.CreateShortcut($ShortcutFile)
$shortcut.TargetPath = "powershell.exe"
$shortcut.Arguments = "-NoExit -ExecutionPolicy Bypass -Command `"& '" + $TargetFile + "'`""
$shortcut.IconLocation = "$env:APPDATA\VowelAnalyzer\assets\magnifying-glass-chart-solid.ico"
$shortcut.Save()

Read-Host -Prompt "Press Enter to exit"
