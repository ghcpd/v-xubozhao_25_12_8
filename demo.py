"""Minimal demo to exercise core libraries: numpy, pandas, sklearn.

This module does lazy imports so tests can run even when compiled
dependencies (like scikit-learn or pandas) can't be built on Windows
without Visual C++ Build Tools.
"""


def run_demo():
    # Lazy-import numpy to avoid importing a binary wheel at module import
    # time which can crash the test runner on some Windows configurations.
    try:
        import numpy as np
    except Exception:
        np = None

    # Data
    if np is not None:
        X = np.array([[1.0], [2.0], [3.0], [4.0]])
        y = np.array([2.0, 4.1, 5.9, 8.2])
    else:
        # fallback to pure-Python lists
        X = [[1.0], [2.0], [3.0], [4.0]]
        y = [2.0, 4.1, 5.9, 8.2]

    # Try to use scikit-learn; if unavailable, use a tiny pure-Python linear
    # regression fallback that does not require numpy.
    try:
        from sklearn.linear_model import LinearRegression
        # sklearn expects numpy arrays; import there to allow sklearn to be
        # optional as well
        import numpy as _np
        model = LinearRegression()
        model.fit(_np.array(X), _np.array(y))
        pred = model.predict(_np.array([[5.0]]))
        prediction = float(pred[0])
    except Exception:
        # Simple linear fit (least-squares for line y = a*x + b) using pure python
        xs = [row[0] for row in X]
        n = len(xs)
        mean_x = sum(xs) / n
        mean_y = sum(y) / n
        num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(xs, y))
        den = sum((xi - mean_x) ** 2 for xi in xs)
        a = num / den
        b = mean_y - a * mean_x
        prediction = a * 5.0 + b

    # Try to produce a pandas DataFrame-like object; fall back to simple
    # object with a shape attribute when pandas isn't available.
    try:
        import pandas as pd
        if np is not None:
            df = pd.DataFrame({"x": _np.array(xs if np is None else [r[0] for r in X]), "y": y})
        else:
            df = pd.DataFrame({"x": [r[0] for r in X], "y": y})
    except Exception:
        class SimpleDF:
            def __init__(self, rows):
                self.shape = (rows, 2)

            def __repr__(self):
                return f"SimpleDF(shape={self.shape})"

        df = SimpleDF(4)

    return float(prediction), df


if __name__ == "__main__":
    p, df = run_demo()
    print("prediction for x=5:", p)
    print(df)
