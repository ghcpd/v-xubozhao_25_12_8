import sys
import importlib

import pytest


def import_optional(name):
    try:
        return importlib.import_module(name)
    except Exception as exc:  # pragma: no cover - we want tests to report missing deps
        pytest.skip(f"Optional dependency {name!r} not available: {exc}")


def test_numpy_basic():
    np = import_optional('numpy')
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    s = a + b
    assert s.tolist() == [5, 7, 9]


def test_pandas_basic():
    pd = import_optional('pandas')
    df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
    assert tuple(df.shape) == (2, 2)


def test_scipy_basic():
    sp = import_optional('scipy')
    # Do a lightweight operation
    res = sp.integrate.quad(lambda x: x ** 2, 0, 1)
    assert pytest.approx(res[0], rel=1e-4) == 1.0 / 3.0


def test_sklearn_basic():
    skl = import_optional('sklearn')
    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    X, y = make_classification(n_samples=80, n_features=6, n_classes=2, random_state=0)
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    score = model.score(X, y)
    assert score >= 0.5


def test_fastapi_app_import():
    fastapi = import_optional('fastapi')
    from fastapi import FastAPI
    app = FastAPI()
    @app.get('/ping')
    def ping():
        return {'ok': True}

    # FastAPI contains routes mapping
    assert 'ping' in [r.name for r in app.routes if r.name is not None]
