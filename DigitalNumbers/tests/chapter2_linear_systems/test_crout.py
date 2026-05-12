"""
Test — Crout Factorization
==========================

Runs a test case for Crout factorization
and prints all stages, matrices L and U,
and the final solution vector.

To run:
    python tests/chapter2_linear_systems/test_crout.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from methods.chapter2_linear_systems.crout import crout
from helpers.print_helpers import print_lu_result


# ──────────────────────────────────────────────
# Test 1
# ──────────────────────────────────────────────

A = np.array([
    [4, -1, 0, 3],
    [1, 15.5, 3, 8],
    [0, -1.3, -4, 1.1],
    [14, 5, -2, 30]
], dtype=float)

b = np.array([1, 1, 1, 1], dtype=float)

# Run method
x, L, U, stages = crout(A, b)

# Print results
print_lu_result(
    "Crout Factorization",
    x,
    stages
)
