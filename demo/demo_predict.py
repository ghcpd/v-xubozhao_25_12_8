"""Minimal demo to verify scikit-learn + numpy + pandas operate normally."""
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


def run_demo():
    X = np.array([[0], [1], [2], [3]])
    y = np.array([0, 0, 1, 1])
    model = LogisticRegression(solver="liblinear")
    model.fit(X, y)
    df = pd.DataFrame(X, columns=["x"]).assign(pred=model.predict(X))
    print(df.to_string(index=False))


if __name__ == "__main__":
    run_demo()
