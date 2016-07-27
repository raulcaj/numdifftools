from __future__ import print_function
import unittest
import numdifftools.core as nd
import numpy as np
from numdifftools.step_generators import (MinStepGenerator, MaxStepGenerator,
                                          MinMaxStepGenerator, EPS)
from numpy.testing import assert_array_almost_equal

class TestMinMaxStepGenerator(unittest.TestCase):

    @staticmethod
    def test_default_generator():
        step_gen = nd.MinMaxStepGenerator(step_min=None, step_max=None,
                                          num_steps=10, scale=None,
                                          num_extrap=0)
        h = np.array([h for h in step_gen(0)])
        desired = np.array([5.47742059e-07, 9.61174159e-07,
                            1.68666209e-06, 2.95974352e-06,
                            5.19373845e-06, 9.11393803e-06,
                            1.59930785e-05, 2.80645488e-05,
                            4.92474854e-05, 8.64191631e-05])
        print(h)
        assert_array_almost_equal((h - desired) / desired, 0)

    @staticmethod
    def test_default_base_step():
        step_gen = nd.MinMaxStepGenerator(num_steps=1)
        h = [h for h in step_gen(0)]
        desired = nd.EPS ** (1. / 2.5)
        print(h)
        assert_array_almost_equal((h[0] - desired) / desired, 0)

    @staticmethod
    def test_fixed_base_step():
        desired = 0.1
        step_gen = nd.MinMaxStepGenerator(step_min=desired, num_steps=1,
                                          scale=2)
        h = [h for h in step_gen(0)]
        print(h)
        assert_array_almost_equal((h[-1] - desired) / desired, 0)


class TestMinStepGenerator(unittest.TestCase):

    @staticmethod
    def test_default_generator():
        step_gen = nd.MinStepGenerator(base_step=None, num_steps=10,
                                       step_ratio=4, offset=-1)
        h = np.array([h for h in step_gen(0)])
        desired = np.array([3.58968236e-02, 8.97420590e-03, 2.24355147e-03,
                            5.60887869e-04, 1.40221967e-04, 3.50554918e-05,
                            8.76387295e-06, 2.19096824e-06, 5.47742059e-07,
                            1.36935515e-07])

        assert_array_almost_equal((h - desired) / desired, 0)

    @staticmethod
    def test_default_base_step():
        step_gen = nd.MinStepGenerator(num_steps=1, offset=0)
        h = [h for h in step_gen(0)]
        desired = nd.EPS ** (1. / 2.5)
        assert_array_almost_equal((h[-1] - desired) / desired, 0)

    @staticmethod
    def test_fixed_base_step():
        desired = 0.1
        step_gen = nd.MinStepGenerator(base_step=desired, num_steps=1,
                                       offset=0)
        h = [h for h in step_gen(0)]
        assert_array_almost_equal((h[-1] - desired) / desired, 0)


class TestMaxStepGenerator(unittest.TestCase):

    @staticmethod
    def test_default_generator():
        step_gen = nd.MaxStepGenerator(num_steps=10)
        h = np.array([h for h in step_gen(0)])

        desired = 2.0* 2.0 ** (-np.arange(10)+ 0)

        assert_array_almost_equal((h - desired) / desired, 0)

    @staticmethod
    def test_default_base_step():
        step_gen = nd.MaxStepGenerator(num_steps=1, offset=0)
        h = [h for h in step_gen(0)]
        desired = 2.0
        assert_array_almost_equal((h[0] - desired) / desired, 0)

    @staticmethod
    def test_fixed_base_step():
        desired = 0.1
        step_gen = nd.MaxStepGenerator(step_max=desired, num_steps=1, offset=0)
        h = [h for h in step_gen(0)]
        assert_array_almost_equal((h[0] - desired) / desired, 0)
