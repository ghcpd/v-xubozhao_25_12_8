#!/usr/bin/env bash
set -euo pipefail

VENVDIR=${1:-venv}

if [ -d "${VENVDIR}" ]; then
  echo "Using virtualenv: ${VENVDIR}"
  # shellcheck source=/dev/null
  source ${VENVDIR}/bin/activate
else
  echo "Virtualenv ${VENVDIR} not found — running tests with current environment"
fi

echo "Running pytest..."
pytest -q
