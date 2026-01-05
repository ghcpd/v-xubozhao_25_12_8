# PowerShell script to create venv and install dependencies
$ErrorActionPreference = 'Stop'
if (-Not (Test-Path -Path .venv)) {
    python -m venv .venv
}
. .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
Write-Host "Setup complete. Activate with: . .venv\Scripts\Activate.ps1"