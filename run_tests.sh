#!/usr/bin/env bash
set -euo pipefail
VENV_DIR=${VENV_DIR:-.venv}

if [ -f "$VENV_DIR/bin/activate" ]; then
  # shellcheck source=/dev/null
  source "$VENV_DIR/bin/activate"
else
  echo "Virtualenv not found. Running tests using system python. Consider running ./setup.sh first."
fi

pytest -q --disable-warnings --maxfail=1
