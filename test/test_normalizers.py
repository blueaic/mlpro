## -------------------------------------------------------------------------------------------------
## -- Project : MLPro - The integrative middleware framework for standardized machine learning
## -- Package : test
## -- Module  : test_normalizers.py
## -------------------------------------------------------------------------------------------------

"""Unit tests for normalizer renormalization."""

import unittest

import numpy as np

from mlpro.bf.math import Dimension, Element, Set
from mlpro.bf.math.normalizers import Normalizer


class TestRenormalize(unittest.TestCase):

    def setUp(self):
        self.normalizer = Normalizer(p_autocreate_elements=False)
        self.old = np.array([[0.5, 2.0], [-1.0, 3.0]])
        self.new = np.array([[1.5, 0.25], [2.0, -4.0]])
        self.normalizer._scaler_param_old = self.old.copy()
        self.normalizer._scaler_param_new = self.new.copy()

    def test_array(self):
        data = np.array([[0.0, 2.0], [3.0, -5.0]], dtype=float)
        expected = (data - self.old[1]) / self.old[0] * self.new[0] + self.new[1]
        result = self.normalizer.renormalize(data)
        self.assertIs(result, data)
        np.testing.assert_allclose(result, expected, rtol=1e-14, atol=1e-14)

    def test_dimension(self):
        data = np.array([[0.0, 2.0], [3.0, -5.0]], dtype=float)
        expected = data.copy()
        expected[:, 1] = (data[:, 1] - self.old[1, 1]) / self.old[0, 1] * self.new[0, 1] + self.new[1, 1]
        self.normalizer.renormalize(data, p_dim=1)
        np.testing.assert_allclose(data, expected, rtol=1e-14, atol=1e-14)

    def test_explicit_parameters(self):
        data = np.array([[1.0, 4.0]], dtype=float)
        old = np.array([[2.0, 0.5], [1.0, -3.0]])
        new = np.array([[4.0, 3.0], [-1.0, 2.0]])
        expected = (data - old[1]) / old[0] * new[0] + new[1]
        self.normalizer.renormalize(data, p_param_old=old, p_param_new=new)
        np.testing.assert_allclose(data, expected, rtol=1e-14, atol=1e-14)

    def test_unchanged_dimension(self):
        self.normalizer._scaler_param_new[:, 0] = self.old[:, 0]
        data = np.array([[1.0, 4.0]], dtype=float)
        self.assertIs(self.normalizer.renormalize(data, p_dim=0), data)
        np.testing.assert_array_equal(data, [[1.0, 4.0]])

    def test_no_previous_parameters(self):
        self.normalizer._scaler_param_old = None
        data = np.array([[1.0, 4.0]], dtype=float)
        self.assertIs(self.normalizer.renormalize(data), data)

    def test_element(self):
        dimensions = Set()
        dimensions.add_dim(Dimension(p_name_short="x"))
        dimensions.add_dim(Dimension(p_name_short="y"))
        data = Element(dimensions)
        data.set_values(np.array([1.0, 4.0]))
        expected = (data.get_values().copy() - self.old[1]) / self.old[0] * self.new[0] + self.new[1]
        self.assertIs(self.normalizer.renormalize(data), data)
        np.testing.assert_allclose(data.get_values(), expected, rtol=1e-14, atol=1e-14)


if __name__ == "__main__":
    unittest.main()
