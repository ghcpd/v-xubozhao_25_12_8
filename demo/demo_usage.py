"""Minimal demo script exercising key libraries.

Run this after `setup.sh` has installed dependencies into a venv.
"""
def main():
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    print('numpy version:', np.__version__)
    print('pandas version:', pd.__version__)

    # Small numeric demo
    X = np.array([[1.0], [2.0], [3.0]])
    y = np.array([2.0, 4.1, 6.05])
    model = LinearRegression()
    model.fit(X, y)
    print('fitted coef:', model.coef_.tolist())


if __name__ == '__main__':
    main()
