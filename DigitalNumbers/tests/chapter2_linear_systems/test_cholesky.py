"""
Test — Cholesky Factorization
==============================

Runs a test case for the Cholesky factorization method and prints
all stages, matrices L and U, and the final solution vector.

Cholesky requires a symmetric positive definite matrix.

To run (from inside DigitalNumbers/):
    python tests/chapter2_linear_systems/test_cholesky.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from methods.chapter2_linear_systems.cholesky import cholesky
from tests.print_helpers import print_lu_result


# ──────────────────────────────────────────────
# Test 1 — Symmetric positive definite matrix
# ──────────────────────────────────────────────

A = np.array([
    [ 4,  2,  2],
    [ 2,  5,  3],
    [ 2,  3,  6],
], dtype=float)

b = np.array([8, 10, 11], dtype=float)

# Run method
x, L, U, stages = cholesky(A, b)

# Print results
print_lu_result(
    "Cholesky Factorization  |  A = L * L^T",
    x,
    stages
)

# Verify: L @ U should equal original A
A_reconstructed = L @ U
print("  Verification  L @ U == A :", np.allclose(A_reconstructed, A))
print()
