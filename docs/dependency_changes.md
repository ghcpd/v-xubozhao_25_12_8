# Dependency changes (Before → After)

Source: requirements_old.txt → requirements.txt

## Summary
- Goal: Upgrade to versions that are compatible with Python 3.10+ and address known age/compatibility/security issues while keeping a reproducible, pinned environment.

## Diff
- scikit-learn: 0.24.1 → 1.2.2
  - Reason: 0.24.x is several major releases behind; scikit-learn 1.2.x supports Python 3.10 and contains many bug fixes and performance improvements. Ensures compatibility with newer numpy/scipy.

- numpy: 1.18.0 → 1.25.2
  - Reason: numpy 1.18 does not support Python 3.10. Bumping to a modern 1.x release compatible with Python 3.10+. Pinned for reproducibility.

- pandas: 1.1.5 → 1.5.3
  - Reason: pandas 1.1.x is older and may not support Python 3.10. pandas 1.5.x is stable and keeps API compatibility for common analytics code while supporting newer Python.

- matplotlib: 3.3.2 → 3.5.3
  - Reason: 3.3.x is dated. 3.5.x supports modern Python and fixes rendering/packaging issues.

- scipy: 1.5.2 → 1.10.1
  - Reason: scipy 1.5.x is old and may not be fully compatible with latest numpy/Python; 1.10.x is a stable, maintained release.

- pytest: 5.4.3 → 7.3.2
  - Reason: pytest 5.x lacks features and has compatibility issues with modern test plugins and Python 3.10. Use pytest 7.x for improved test runner features and compatibility.

- fastapi: 0.63.0 → 0.95.2
  - Reason: FastAPI matured with several improvements and security fixes since 0.63; upgrade to a maintained minor release.

- uvicorn: 0.13.3 → 0.22.0
  - Reason: Uvicorn 0.13 is old and has dependency changes; newer versions improve ASGI support and security fixes.

## Notes on breaking changes and risk
- Major-version risk: scikit-learn from 0.24 → 1.2 may include deprecated APIs. Tests should catch regressions in common usage (training/predicting). Code that used removed APIs will need to be updated.
- pandas 1.1 → 1.5: there were some API changes but typical DataFrame operations remain compatible; review code paths that use deprecated behavior.
- numpy version bumps occasionally change default dtypes and behavior for edge cases; validate numerical computations in tests.

## Reproducibility
- requirements.txt is fully pinned to exact versions.
- setup.sh creates a virtual environment, installs pinned versions, and writes requirements.lock (pip freeze) to capture the actual installed set.

