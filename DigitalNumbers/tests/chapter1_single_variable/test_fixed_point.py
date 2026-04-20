"""
Test — Fixed Point Iteration Method
=====================================
Uses the exact inputs specified by the professor in Prueba_métodos_1.pdf

To run (from DigitalNumbers/ root):
    python tests/chapter1_single_variable/test_fixed_point.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.fixed_point import fixed_point_method
from tests.print_helpers import print_root_result

# ── Professor's exact inputs ──────────────────────────────────────────────────
# f1(x) = ln(sin²(x) + 1) − 1/2 − x   ← the equation being solved: f1(x)=0
# g(x)  = ln(sin²(x) + 1) − 1/2        ← rewritten as x = g(x)
# x0 = -0.5,  tol = 1e-7,  N = 100
# Expected root ≈ -0.3744450530
# ─────────────────────────────────────────────────────────────────────────────
g = lambda x: np.log(np.sin(x)**2 + 1) - 0.5

result = fixed_point_method(g=g, x0=-0.5, tol=1e-7, n_max=100)
print_root_result("g(x) = ln(sin²(x)+1) - 1/2  |  x0=-0.5, tol=1e-7, N=100", result)
