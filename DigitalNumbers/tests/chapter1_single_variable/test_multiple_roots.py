"""
Test — Multiple Roots Method
==============================
Uses the exact inputs specified by the professor in Prueba_métodos_1.pdf

To run (from DigitalNumbers/ root):
    python tests/chapter1_single_variable/test_multiple_roots.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.multiple_roots import multiple_roots
from tests.print_helpers import print_root_result

# ── Professor's exact inputs ──────────────────────────────────────────────────
# h(x)   = e^x − x − 1
# h'(x)  = e^x − 1
# h''(x) = e^x
# x0 = 1,  tol = 1e-7,  N = 100
# Expected root ≈ 0.0  (root of multiplicity 2)
# ─────────────────────────────────────────────────────────────────────────────
h   = lambda x: np.exp(x) - x - 1
dh  = lambda x: np.exp(x) - 1
d2h = lambda x: np.exp(x)

result = multiple_roots(f=h, df=dh, d2f=d2h, x0=1.0, tol=1e-7, n_max=100)
print_root_result("h(x) = eˣ - x - 1  |  x0=1.0, tol=1e-7, N=100", result)
