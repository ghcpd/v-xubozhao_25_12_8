# PowerShell test runner
$ErrorActionPreference = 'Stop'
if (Test-Path ".venv\Scripts\python.exe") {
    .venv\Scripts\python.exe -m pytest -q --maxfail=1
} else {
    Write-Host ".venv not found; creating temporary venv and installing requirements"
    python -m venv .venv
    .venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
    .venv\Scripts\python.exe -m pip install -r requirements.txt
    .venv\Scripts\python.exe -m pytest -q --maxfail=1
}