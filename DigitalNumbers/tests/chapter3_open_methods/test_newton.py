"""
Test — Newton-Raphson Method  (Chapter 3)
==========================================
Instructor values: f, f', x0 = 0.5, Tol = 1e-7, N = 100

To run:
    python tests/chapter3_open_methods/test_newton.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.newton import newton_method
from tests.print_helpers import print_root_result

f  = lambda x: np.log(np.sin(x)**2 + 1) - 0.5
df = lambda x: 2 * (np.sin(x)**2 + 1)**(-1) * np.sin(x) * np.cos(x)

result = newton_method(f=f, df=df, x0=0.5, tol=1e-7, n_max=100)
print_root_result(
    "Newton-Raphson  |  f(x) = ln(sin²(x)+1) - 1/2  |  x0=0.5, Tol=1e-7, N=100",
    result
)
