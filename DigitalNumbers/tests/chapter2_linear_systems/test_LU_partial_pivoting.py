"""
Test — LU Factorization with Partial Pivoting
=============================================

Runs a test case for LU factorization with partial pivoting
and prints all stages, matrices P, L, U, and the final solution vector.

To run:
    python tests/chapter2_linear_systems/test_LU_partial_pivoting.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from methods.chapter2_linear_systems.LU_partial_pivoting import LU_partial_pivoting
from tests.print_helpers import print_lu_result


# ──────────────────────────────────────────────
# Test 
# ──────────────────────────────────────────────

A = np.array([
    [4, -1, 0, 3],
    [1, 15.5, 3, 8],
    [0, -1.3, -4, 1.1],
    [14, 5, -2, 30]
], dtype=float)

b = np.array([1, 1, 1, 1], dtype=float)

# Run method
x, P, L, U, stages = LU_partial_pivoting(A, b)

# Print results
print_lu_result(
    "LU Factorization with Partial Pivoting",
    x,
    stages
)
