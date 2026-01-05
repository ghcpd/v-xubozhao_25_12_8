import sys
import numpy as np
import pandas as pd
import matplotlib
import scipy
import sklearn
from sklearn.linear_model import LogisticRegression
from demo_app import app
from fastapi.testclient import TestClient


def test_numpy_basic():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert np.dot(a, b) == 32


def test_pandas_basic():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    assert df["x"].sum() == 6


def test_sklearn_basic():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]
    clf = LogisticRegression(solver="liblinear")
    clf.fit(X, y)
    preds = clf.predict([[1.5], [0.2]])
    assert set(preds).issubset({0, 1})


def test_matplotlib_import():
    # ensure matplotlib backend can be set without display
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([0, 1], [0, 1])
    assert fig is not None


def test_fastapi_health():
    client = TestClient(app)
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_runtime_python_version():
    # Ensure running on Python 3.10+ during CI
    major, minor = sys.version_info[:2]
    assert (major == 3 and minor >= 10) or (major > 3)
