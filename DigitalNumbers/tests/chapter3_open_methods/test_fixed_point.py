"""
Test — Fixed Point Iteration Method  (Chapter 3)
=================================================
Instructor values: f1, g, x0 = -0.5, Tol = 1e-7, N = 100

To run:
    python tests/chapter3_open_methods/test_fixed_point.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.fixed_point import fixed_point_method
from tests.print_helpers import print_root_result

g = lambda x: np.log(np.sin(x)**2 + 1) - 0.5

result = fixed_point_method(g=g, x0=-0.5, tol=1e-7, n_max=100)
print_root_result(
    "Fixed Point  |  g(x) = ln(sin²(x)+1) - 1/2  |  x0=-0.5, Tol=1e-7, N=100",
    result
)
