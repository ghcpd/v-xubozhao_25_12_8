import importlib
import os
import sys
# ensure repo root is on path so demo package can be imported during tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import numpy as np
import pandas as pd


def test_numpy_and_pandas_basic_operations():
    # numpy basic array ops
    a = np.array([1, 2, 3], dtype=float)
    assert a.mean() == 2.0

    # pandas DataFrame creation and aggregation
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    assert df.sum("index").sum() == 10


def test_sklearn_basic_training():
    sklearn = importlib.import_module("sklearn")
    from sklearn.linear_model import LogisticRegression

    X = np.array([[0], [1], [2], [3]])
    y = np.array([0, 0, 1, 1])
    model = LogisticRegression(solver="liblinear")
    model.fit(X, y)
    preds = model.predict(X)
    assert preds.shape == (4,)


def test_fastapi_and_uvicorn_imports():
    fastapi = importlib.import_module("fastapi")
    uvicorn = importlib.import_module("uvicorn")
    from fastapi import FastAPI

    app = FastAPI()
    assert isinstance(app, fastapi.applications.FastAPI)


def test_demo_script_runs():
    # sanity-run demo script
    import demo.demo_predict as demo

    # demo.run_demo should execute without raising
    demo.run_demo()
