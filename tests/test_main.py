import pytest
import numpy as np
from regressio.datagen import generate_random_walk
from regressio.models import linear_regression, isotonic_regression

'''
Pytest:
- prefix your class with 'Test', and functions with 'test' otherwise they will be skipped.
'''

class Test_generate_random_walk: 
    def test_positive(self):
        x, y = generate_random_walk(10, 1)
        assert len(x) == len(y) == 10

    def test_zero(self):
        with pytest.raises(ValueError):
            x, y = generate_random_walk(0, 1)

    def test_negative(self):
        with pytest.raises(ValueError):
            x, y = generate_random_walk(-10, -1)

class Test_linear_regression: 
    def test_degree_greater_than_10(self):
        with pytest.raises(ValueError):
            model = linear_regression(11)

    def test_degree_less_than_10(self):
        with pytest.raises(ValueError):
            model = linear_regression(-1)

class Test_isotonic_regression: 
    def test_no_data_in_knot(self):
        with pytest.raises(ValueError):
            x, y = np.arange(20), np.cumsum(np.ones(20))
            model = isotonic_regression(21)
            model.fit(x, y)