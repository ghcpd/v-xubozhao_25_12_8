#!/usr/bin/env bash
set -euo pipefail
PYTHON=${PYTHON:-python3}
VENV_DIR=${VENV_DIR:-.venv}

echo "Creating virtual environment in $VENV_DIR using $PYTHON..."
$PYTHON -m venv "$VENV_DIR"
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

echo "Upgrading pip, setuptools, wheel..."
python -m pip install --upgrade pip setuptools wheel

echo "Installing pinned requirements..."
python -m pip install -r requirements.txt

# Freeze installed packages to lockfile for reproducibility
python -m pip freeze > requirements.lock

echo "Setup complete. Activate the environment with: source $VENV_DIR/bin/activate"
