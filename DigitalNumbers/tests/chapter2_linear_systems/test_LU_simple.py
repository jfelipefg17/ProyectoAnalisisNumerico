"""
Test — LU Factorization with Simple Gaussian Elimination

Runs a test case for LU factorization using simple Gaussian elimination
and prints all stages, matrices L and U, and the final solution vector.

To run:
    python tests/chapter2_linear_systems/test_LU_simple.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from methods.chapter2_linear_systems.LU_simple import LU_simple
from helpers.print_helpers import print_lu_result

# ──────────────────────────────────────────────
# Test 
# ──────────────────────────────────────────────
# A =
# [ 4  -1   0   3 ]
# [ 1  15.5 3   8 ]
# [ 0  -1.3 -4  1.1 ]
# [ 14  5  -2  30 ]
#
# b = [1, 1, 1, 1]
#
# Expected solution:
# x ≈ [0.525109, 0.255459, -0.410480, -0.281659]
# ──────────────────────────────────────────────

A = np.array([
    [4, -1, 0, 3],
    [1, 15.5, 3, 8],
    [0, -1.3, -4, 1.1],
    [14, 5, -2, 30]
], dtype=float)

b = np.array([1, 1, 1, 1], dtype=float)

# Run method
x, L, U, stages = LU_simple(A, b)

# Print results
print_lu_result(
    "LU Factorization with Simple Gaussian Elimination",
    x,
    stages
)
