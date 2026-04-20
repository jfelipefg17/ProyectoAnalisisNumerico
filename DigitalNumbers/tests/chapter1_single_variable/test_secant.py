"""
Test — Secant Method
======================
Uses the exact inputs specified by the professor in Prueba_métodos_1.pdf

To run (from DigitalNumbers/ root):
    python tests/chapter1_single_variable/test_secant.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.secant import secant
from tests.print_helpers import print_root_result

# ── Professor's exact inputs ──────────────────────────────────────────────────
# f(x) = ln(sin²(x) + 1) − 1/2
# x0 = 0.5,  x1 = 1,  tol = 1e-7,  N = 100
# Expected root ≈ 0.9364045809
# ─────────────────────────────────────────────────────────────────────────────
f = lambda x: np.log(np.sin(x)**2 + 1) - 0.5

result = secant(f=f, x0=0.5, x1=1.0, tol=1e-7, n_max=100)
print_root_result("f(x) = ln(sin²(x)+1) - 1/2  |  x0=0.5, x1=1, tol=1e-7, N=100", result)
