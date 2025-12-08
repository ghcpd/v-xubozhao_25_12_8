#!/usr/bin/env bash
set -euo pipefail
VENV_DIR=${VENV_DIR:-.venv}
# shellcheck disable=SC1091
source "${VENV_DIR}/Scripts/activate"
pytest -q
