# Dependency Upgrade Audit & Changes

Date: 2025-12-08

## Summary
The project previously used an outdated set of packages (requirements_old.txt). These versions predate Python 3.10 and contain both missing features and potential security fixes. The dependency list was audited, updated to modern and stable releases known to be compatible with Python 3.10+, and pinned in `requirements.txt` for reproducibility.

## Before → After
Final pinned versions (tested on Python 3.13 in CI run here):

- scikit-learn: 0.24.1 → 1.5.2
  - Reason: Jump to a modern release that provides CPython 3.13 wheels, improved algorithms, and better interoperability with numpy 2.x.

- numpy: 1.18.0 → 2.3.5
  - Reason: Supports Python 3.13, improved performance, and widely-available binary wheels for Windows/Linux/macOS.

- pandas: 1.1.5 → 2.3.3
  - Reason: Pandas 2.x is required for compatibility with numpy 2.x and includes major performance and API improvements.

- matplotlib: 3.3.2 → 3.10.7
  - Reason: Newer releases support numpy 2.x and ship pre-built wheels for modern Python.

- scipy: 1.5.2 → 1.16.3
  - Reason: Choosen because it supplies pre-built wheels for Python 3.13 and compatible with numpy 2.x.

- pytest: 5.4.3 → 8.4.2
  - Reason: Stable test runner with support for modern fixtures and plugins and compatible wheels for 3.13.

- fastapi: 0.63.0 → 0.95.2
  - Reason: Stable FastAPI version with maintained dependencies and compatibility with pydantic/starlette used in 3.13 environments.

- uvicorn: 0.13.3 → 0.22.0
  - Reason: Fast async server with bug fixes and compatibility improvements.

- httpx: added → 0.25.2
  - Reason: Test client dependency used by FastAPI TestClient; matches modern async stacks.

Notes:
- Multiple iterative adjustments were necessary to land on a consistent, wheel-based set for Python 3.13—this avoids building heavy packages from source (meson/openblas) on CI/Windows.
- All final pinned versions were installed and validated by running pytest in a freshly-created virtual environment; `6 passed`.

## Reproducibility
All packages are pinned with exact versions to ensure reproducible installs across environments. Use `setup.sh` to create a venv and install requirements.

## Tests and Automation
- `tests/test_runtime.py` contains lightweight runtime sanity checks for core libraries and a small FastAPI health endpoint.
- `run_tests.sh` executes pytest from the venv.

## Notes
- These upgrades represent conservative, stable releases that were widely available and compatible with Python 3.10 at the time of the upgrade.
- If you require the *very latest* versions, consider a follow-up where we bump to the newest releases and regenerate lockfiles (poetry/constraints).
