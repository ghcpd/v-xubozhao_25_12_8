import subprocess
import sys
import importlib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def test_demo_runs():
    # Run demo as a separate process to avoid crashing the pytest process
    # if a binary dependency (like numpy) is incompatible on this platform.
    import subprocess
    import sys
    proc = subprocess.run([sys.executable, str(PROJECT_ROOT / 'demo.py')], capture_output=True, text=True)
    # If the demo executed successfully, it should exit with code 0 and print a prediction
    assert proc.returncode == 0, f"demo failed: returncode={proc.returncode}\nstdout={proc.stdout}\nstderr={proc.stderr}"
    # Basic output check
    assert "prediction for x=5:" in proc.stdout


def test_fastapi_import():
    try:
        import fastapi
    except Exception:
        import pytest
        pytest.skip("fastapi not installed in this environment")
    assert hasattr(fastapi, 'FastAPI')


def test_uvicorn_import():
    try:
        import uvicorn
    except Exception:
        import pytest
        pytest.skip("uvicorn not installed in this environment")
    assert hasattr(uvicorn, 'run')


def test_sklearn_optional():
    try:
        import sklearn.linear_model
    except Exception:
        import pytest
        pytest.skip("scikit-learn not available in this environment (no C build tools)")
    from sklearn.linear_model import LinearRegression
    import numpy as np
    X = np.array([[1.0], [2.0]])
    y = np.array([2.0, 4.0])
    model = LinearRegression()
    model.fit(X, y)
    assert hasattr(model, 'predict')
