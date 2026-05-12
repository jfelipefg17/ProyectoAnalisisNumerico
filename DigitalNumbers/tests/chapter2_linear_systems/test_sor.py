"""
Test — SOR Method
=================

Runs a test case for the SOR method
and prints the final approximation,
number of iterations, and final error.

To run:
    python tests/chapter2_linear_systems/test_sor.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from methods.chapter2_linear_systems.sor import sor


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

x0 = np.array([0, 0, 0, 0], dtype=float)

tol = 1e-7
Nmax = 100

# Relaxation factor
w = 1.5

norm_type = 2

# Run method
x, iterations, error = sor(
    A,
    b,
    x0,
    w,
    tol,
    Nmax,
    norm_type
)

# Print results
print("\nSOR Method")
print("===========")

print("\nSolution:")
print(x)

print("\nIterations:")
print(iterations)

print("\nError:")
print(error)
