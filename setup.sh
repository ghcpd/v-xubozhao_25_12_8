#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r requirements.txt

echo "Setup complete. Activate with: source .venv/bin/activate"