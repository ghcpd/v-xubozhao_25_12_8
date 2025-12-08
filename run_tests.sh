#!/usr/bin/env bash
set -euo pipefail
# Cross-platform test runner: prefers .venv Python executable
if [ -f ".venv/bin/python" ]; then
  .venv/bin/python -m pytest -q --maxfail=1
else
  # Windows
  .venv\Scripts\python -m pytest -q --maxfail=1
fi
