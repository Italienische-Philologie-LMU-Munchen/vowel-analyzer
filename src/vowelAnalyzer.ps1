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
    $pythonCommand = "python"
} else {
    $pythonCommand = "python"
}

Write-Host "Starting Vowel Analyzer..."

$pythonRunCommand = "$env:APPDATA\VowelAnalyzer\vowelAnalyzerGui.py"
Start-Process $pythonRunCommand

Add-Type -AssemblyName UIAutomationClient

$MyProcess = Get-Process | Where-Object {$_.MainWindowTitle -like "*C:\Windows\py.exe*"}
$MyPowershellProcess = Get-Process -Id ([System.Diagnostics.Process]::GetCurrentProcess().Id)

$ae = [System.Windows.Automation.AutomationElement]::FromHandle($MyProcess.MainWindowHandle)
$wp = $ae.GetCurrentPattern([System.Windows.Automation.WindowPatternIdentifiers]::Pattern)


# Minimize python window so we only see GUI and no console window of python.exe.
$IsMinimized = $wp.Current.WindowVisualState -eq 'Minimized'
if (! $IsMinimized) { $wp.SetWindowVisualState('Minimized') } 

# Close current window as we don't need powershell after startup anymore
$MyPowershellProcess.Kill()