[CmdletBinding()]
param(
    [ValidateRange(1024, 65535)]
    [int]$Port = 7860,

    [string]$ListenAddress = "127.0.0.1"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$projectRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$runtimeRoot = [System.IO.Path]::GetFullPath((Join-Path $projectRoot ".runtime"))
$managedNames = @("temp", "gradio")
$markerName = ".managed-by-dentalv8"
$markerText = "DentalV8 managed runtime cache"
$lockPath = Join-Path $runtimeRoot "dentalv8-runtime.lock"
$lockStream = $null
$locationPushed = $false
$serverExitCode = 0

function Resolve-ManagedCacheTarget {
    param([Parameter(Mandatory = $true)][string]$Name)

    if ($managedNames -notcontains $Name) {
        throw "Cleanup target is not allowlisted: $Name"
    }

    $candidate = [System.IO.Path]::GetFullPath((Join-Path $runtimeRoot $Name))
    $parent = [System.IO.Directory]::GetParent($candidate)
    if ($null -eq $parent -or -not [System.StringComparer]::OrdinalIgnoreCase.Equals($parent.FullName, $runtimeRoot)) {
        throw "Runtime cache path escaped the managed root: $candidate"
    }
    return $candidate
}

function Initialize-ManagedCacheTarget {
    param([Parameter(Mandatory = $true)][string]$Name)

    $target = Resolve-ManagedCacheTarget -Name $Name
    if (-not (Test-Path -LiteralPath $target)) {
        New-Item -ItemType Directory -Path $target -Force | Out-Null
    }

    $targetInfo = Get-Item -LiteralPath $target -Force
    if (($targetInfo.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "Runtime cache target must not be a symlink or junction: $target"
    }

    $marker = Join-Path $target $markerName
    if (-not (Test-Path -LiteralPath $marker)) {
        $existing = @(Get-ChildItem -LiteralPath $target -Force -ErrorAction Stop)
        if ($existing.Count -gt 0) {
            throw "Refusing to clean a non-empty directory without the DentalV8 marker: $target"
        }
        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::WriteAllText($marker, $markerText, $utf8NoBom)
    }
    elseif ((Get-Content -LiteralPath $marker -Raw -ErrorAction Stop).Trim() -ne $markerText) {
        throw "Runtime cache marker does not match: $target"
    }
    return $target
}

function Remove-ManagedCacheEntry {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Boundary
    )

    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $fullBoundary = [System.IO.Path]::GetFullPath($Boundary).TrimEnd([System.IO.Path]::DirectorySeparatorChar)
    $boundaryPrefix = $fullBoundary + [System.IO.Path]::DirectorySeparatorChar
    if (-not $fullPath.StartsWith($boundaryPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Cache entry escaped the managed target: $fullPath"
    }

    $entry = Get-Item -LiteralPath $fullPath -Force -ErrorAction Stop
    if (($entry.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
        Remove-Item -LiteralPath $entry.FullName -Force -ErrorAction Stop
        return
    }
    if (-not $entry.PSIsContainer) {
        Remove-Item -LiteralPath $entry.FullName -Force -ErrorAction Stop
        return
    }

    $children = @(Get-ChildItem -LiteralPath $entry.FullName -Force -ErrorAction Stop)
    foreach ($child in $children) {
        Remove-ManagedCacheEntry -Path $child.FullName -Boundary $fullBoundary
    }
    Remove-Item -LiteralPath $entry.FullName -Force -ErrorAction Stop
}

function Clear-ManagedCacheTarget {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [switch]$RemoveContainer
    )

    $target = Initialize-ManagedCacheTarget -Name $Name
    $marker = Join-Path $target $markerName
    $entries = @(Get-ChildItem -LiteralPath $target -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne $markerName })
    foreach ($entry in $entries) {
        try {
            Remove-ManagedCacheEntry -Path $entry.FullName -Boundary $target
        }
        catch {
            Write-Warning "Could not remove this cache item; it was kept safely: $($entry.FullName)"
        }
    }

    if ($RemoveContainer) {
        $remaining = @(Get-ChildItem -LiteralPath $target -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne $markerName })
        if ($remaining.Count -eq 0) {
            Remove-Item -LiteralPath $marker -Force -ErrorAction SilentlyContinue
            Remove-Item -LiteralPath $target -Force -ErrorAction SilentlyContinue
        }
    }
}

function Save-ProcessEnvironment {
    param([Parameter(Mandatory = $true)][string[]]$Names)

    $snapshot = @{}
    foreach ($name in $Names) {
        $value = [System.Environment]::GetEnvironmentVariable($name, "Process")
        $snapshot[$name] = @{ Exists = ($null -ne $value); Value = $value }
    }
    return $snapshot
}

function Restore-ProcessEnvironment {
    param([Parameter(Mandatory = $true)][hashtable]$Snapshot)

    foreach ($name in $Snapshot.Keys) {
        $state = $Snapshot[$name]
        $value = if ($state.Exists) { [string]$state.Value } else { $null }
        [System.Environment]::SetEnvironmentVariable($name, $value, "Process")
    }
}

$persistentPaths = [ordered]@{
    TORCH_HOME = (Join-Path $runtimeRoot "torch")
    HF_HOME = (Join-Path $runtimeRoot "huggingface")
    HUGGINGFACE_HUB_CACHE = (Join-Path $runtimeRoot "huggingface\hub")
    XDG_CACHE_HOME = (Join-Path $runtimeRoot "cache")
    YOLO_CONFIG_DIR = (Join-Path $runtimeRoot "ultralytics")
    MPLCONFIGDIR = (Join-Path $runtimeRoot "matplotlib")
    CUDA_CACHE_PATH = (Join-Path $runtimeRoot "cuda")
    JOBLIB_TEMP_FOLDER = (Join-Path $runtimeRoot "joblib")
}
$tempPath = Resolve-ManagedCacheTarget -Name "temp"
$gradioPath = Resolve-ManagedCacheTarget -Name "gradio"
$environmentValues = [ordered]@{
    DENTAL_RUNTIME_ROOT = $runtimeRoot
    DENTAL_MANAGED_RUNTIME = "1"
    TEMP = $tempPath
    TMP = $tempPath
    TMPDIR = $tempPath
    GRADIO_TEMP_DIR = $gradioPath
    GRADIO_ANALYTICS_ENABLED = "False"
}
foreach ($item in $persistentPaths.GetEnumerator()) {
    $environmentValues[$item.Key] = $item.Value
}
$environmentSnapshot = Save-ProcessEnvironment -Names @($environmentValues.Keys)

try {
    New-Item -ItemType Directory -Path $runtimeRoot -Force | Out-Null
    $runtimeInfo = Get-Item -LiteralPath $runtimeRoot -Force
    if (($runtimeInfo.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "The .runtime directory must not be a symlink or junction: $runtimeRoot"
    }

    $systemDrive = [System.IO.Path]::GetPathRoot($env:SystemRoot)
    $runtimeDrive = [System.IO.Path]::GetPathRoot($runtimeRoot)
    if ([System.StringComparer]::OrdinalIgnoreCase.Equals($systemDrive, $runtimeDrive)) {
        throw "Runtime cache is still on the system drive $runtimeDrive. Startup was refused."
    }

    $listener = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    if ($listener) {
        $ownerText = (($listener | Select-Object -ExpandProperty OwningProcess -Unique) -join ", ")
        throw "Port $Port is already used by process $ownerText. Close the old app first; no cache was cleaned."
    }

    try {
        $lockStream = [System.IO.File]::Open(
            $lockPath,
            [System.IO.FileMode]::OpenOrCreate,
            [System.IO.FileAccess]::ReadWrite,
            [System.IO.FileShare]::None
        )
    }
    catch {
        throw "Another DentalV8 launcher is active. Startup was cancelled to protect its cache."
    }

    Clear-ManagedCacheTarget -Name "temp"
    Clear-ManagedCacheTarget -Name "gradio"
    foreach ($path in $persistentPaths.Values) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
        $pathInfo = Get-Item -LiteralPath $path -Force
        if (($pathInfo.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Persistent cache directory must not be a symlink or junction: $path"
        }
    }
    foreach ($item in $environmentValues.GetEnumerator()) {
        [System.Environment]::SetEnvironmentVariable($item.Key, [string]$item.Value, "Process")
    }

    $pythonCandidates = @(
        @(
            $env:DENTAL_PYTHON,
            "D:\py\python.exe",
            (Join-Path $projectRoot ".venv\Scripts\python.exe")
        ) | Where-Object { $_ -and (Test-Path -LiteralPath $_ -PathType Leaf) }
    )
    if ($pythonCandidates.Count -eq 0) {
        $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
        if ($null -eq $pythonCommand) {
            throw "Python was not found. Set DENTAL_PYTHON or install the project environment."
        }
        $pythonExecutable = $pythonCommand.Source
    }
    else {
        $pythonExecutable = $pythonCandidates[0]
    }

    Write-Host "Starting DentalV8" -ForegroundColor Cyan
    Write-Host "URL: http://${ListenAddress}:$Port"
    Write-Host "Temporary files: $tempPath"
    Write-Host "Gradio cache: $gradioPath"
    Write-Host "Press Ctrl+C to stop. Only the two temporary folders above are cleaned on exit."

    Push-Location $projectRoot
    $locationPushed = $true
    & $pythonExecutable -m uvicorn app:app --host $ListenAddress --port $Port
    $serverExitCode = $LASTEXITCODE
}
finally {
    if ($locationPushed) {
        Pop-Location
    }

    if ($null -ne $lockStream) {
        try {
            foreach ($name in $managedNames) {
                try {
                    Clear-ManagedCacheTarget -Name $name -RemoveContainer
                }
                catch {
                    Write-Warning "Exit cleanup for '$name' was incomplete and will be retried on the next safe start: $($_.Exception.Message)"
                }
            }
        }
        finally {
            $lockStream.Dispose()
        }
    }
    try {
        Restore-ProcessEnvironment -Snapshot $environmentSnapshot
    }
    catch {
        Write-Warning "Could not completely restore the current PowerShell environment: $($_.Exception.Message)"
    }
}

if ($serverExitCode -notin @(0, 130, -1073741510, 3221225786)) {
    throw "The project process exited with code $serverExitCode"
}
