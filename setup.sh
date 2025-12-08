#!/usr/bin/env bash
set -euo pipefail
PY_VERSION=${PY_VERSION:-3.10}
VENV_DIR=${VENV_DIR:-.venv}
python${PY_VERSION} -m venv "${VENV_DIR}"
# shellcheck disable=SC1091
source "${VENV_DIR}/Scripts/activate"
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
