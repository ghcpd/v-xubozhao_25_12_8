"""
Analytics Service Runtime Tests
Tests core functionality of upgraded dependencies and system compatibility
"""

import pytest
import sys


class TestEnvironment:
    """Test Python environment and basic imports"""

    def test_python_version(self):
        """Verify Python 3.10+ is running"""
        assert sys.version_info >= (3, 10), f"Python 3.10+ required, got {sys.version_info.major}.{sys.version_info.minor}"

    def test_import_numpy(self):
        """Test numpy import and basic operations"""
        import numpy as np
        
        arr = np.array([1, 2, 3, 4, 5])
        assert arr.shape == (5,)
        assert arr.sum() == 15
        assert np.mean(arr) == 3.0

    def test_import_pandas(self):
        """Test pandas import and DataFrame operations"""
        import pandas as pd
        
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        assert df.shape == (3, 2)
        assert df['A'].sum() == 6
        assert len(df) == 3

    def test_import_scipy(self):
        """Test scipy import and statistical functions"""
        from scipy import stats
        
        # Test basic statistical function
        result = stats.norm.ppf(0.95)
        assert 1.6 < result < 1.7  # 95th percentile of normal distribution

    def test_import_sklearn(self):
        """Test scikit-learn import and basic functionality"""
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        import numpy as np
        
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        y = np.array([0, 1, 0, 1])
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        assert X_train.shape[0] == 3
        assert X_test.shape[0] == 1

    def test_import_matplotlib(self):
        """Test matplotlib import and basic figure creation"""
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        assert fig is not None
        plt.close(fig)

    def test_import_fastapi(self):
        """Test FastAPI import and basic app creation"""
        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/test")
        def test_endpoint():
            return {"message": "success"}
        
        assert app is not None
        assert len(app.routes) > 0

    def test_import_pytest(self):
        """Test pytest is properly installed"""
        import pytest as pt
        
        assert pt.__version__
        assert pt.__version__.startswith(('7.', '8.'))


class TestDataAnalytics:
    """Test analytics-specific functionality"""

    def test_numpy_array_operations(self):
        """Test NumPy array operations"""
        import numpy as np
        
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        
        result = np.dot(arr1, arr2)
        assert result == 32  # 1*4 + 2*5 + 3*6

    def test_pandas_groupby(self):
        """Test pandas groupby operations"""
        import pandas as pd
        
        df = pd.DataFrame({
            'category': ['A', 'B', 'A', 'B'],
            'value': [10, 20, 30, 40]
        })
        
        grouped = df.groupby('category')['value'].sum()
        assert grouped['A'] == 40
        assert grouped['B'] == 60

    def test_scipy_statistical_functions(self):
        """Test scipy statistical functions"""
        from scipy import stats
        import numpy as np
        
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        mean, std = stats.norm.fit(data)
        
        assert 4 < mean < 6
        assert 2 < std < 4

    def test_sklearn_pipeline(self):
        """Test scikit-learn pipeline functionality"""
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LogisticRegression
        import numpy as np
        
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        y = np.array([0, 1, 0, 1])
        
        pipe = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', LogisticRegression(random_state=42, max_iter=200))
        ])
        
        pipe.fit(X, y)
        predictions = pipe.predict(X)
        
        assert len(predictions) == 4
        assert all(p in [0, 1] for p in predictions)

    def test_matplotlib_plotting(self):
        """Test matplotlib plotting capabilities"""
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('sin(x)')
        
        assert ax.get_xlabel() == 'x'
        assert ax.get_ylabel() == 'sin(x)'
        plt.close(fig)


class TestDependencyVersions:
    """Verify correct dependency versions are installed"""

    def test_numpy_version(self):
        """Verify numpy version >= 2.0"""
        import numpy as np
        major = int(np.__version__.split('.')[0])
        assert major >= 2, f"numpy {np.__version__} is too old"

    def test_pandas_version(self):
        """Verify pandas version >= 2.2"""
        import pandas as pd
        major, minor = map(int, pd.__version__.split('.')[:2])
        assert (major, minor) >= (2, 2), f"pandas {pd.__version__} is too old"

    def test_scipy_version(self):
        """Verify scipy version >= 1.14"""
        import scipy
        major, minor = map(int, scipy.__version__.split('.')[:2])
        assert (major, minor) >= (1, 14), f"scipy {scipy.__version__} is too old"

    def test_sklearn_version(self):
        """Verify scikit-learn version >= 1.5"""
        import sklearn
        major, minor = map(int, sklearn.__version__.split('.')[:2])
        assert (major, minor) >= (1, 5), f"sklearn {sklearn.__version__} is too old"

    def test_pytest_version(self):
        """Verify pytest version >= 8.0"""
        import pytest
        major = int(pytest.__version__.split('.')[0])
        assert major >= 8, f"pytest {pytest.__version__} is too old"

    def test_fastapi_version(self):
        """Verify fastapi version >= 0.115"""
        import fastapi
        major, minor = map(int, fastapi.__version__.split('.')[:2])
        assert (major, minor) >= (0, 115), f"fastapi {fastapi.__version__} is too old"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
