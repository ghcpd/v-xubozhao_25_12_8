#!/usr/bin/env bash
# Create and activate a venv, upgrade pip and install pinned dependencies
set -euo pipefail

PY=venv
if [ -n "${1:-}" ]; then
  PY="$1"
fi

echo "Creating virtualenv in ./${PY} ..."
python -m venv ${PY}
echo "Activating virtualenv and installing requirements..."
# shellcheck source=/dev/null
source ${PY}/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Installation complete. To use the environment:"
echo "  source ${PY}/bin/activate"
