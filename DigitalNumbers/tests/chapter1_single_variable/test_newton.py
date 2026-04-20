"""
Test — Newton-Raphson Method
==============================
Uses the exact inputs specified by the professor in Prueba_métodos_1.pdf

To run (from DigitalNumbers/ root):
    python tests/chapter1_single_variable/test_newton.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.newton import newton_method
from tests.print_helpers import print_root_result

# ── Professor's exact inputs ──────────────────────────────────────────────────
# f(x)  = ln(sin²(x) + 1) − 1/2
# f'(x) = 2·sin(x)·cos(x) / (sin²(x) + 1)
# x0 = 0.5,  tol = 1e-7,  N = 100
# Expected root ≈ 0.9364045809
# ─────────────────────────────────────────────────────────────────────────────
f  = lambda x: np.log(np.sin(x)**2 + 1) - 0.5
df = lambda x: 2*np.sin(x)*np.cos(x) / (np.sin(x)**2 + 1)

result = newton_method(f=f, df=df, x0=0.5, tol=1e-7, n_max=100)
print_root_result("f(x) = ln(sin²(x)+1) - 1/2  |  x0=0.5, tol=1e-7, N=100", result)
