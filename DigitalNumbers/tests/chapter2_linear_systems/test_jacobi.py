"""
Test — Jacobi Method
====================
Runs the professor's test case for the Jacobi method and prints:
  - iteration matrix T
  - constant vector C
  - spectral radius
  - full iteration table
  - final solution, iterations, and error
To run:
    python tests/chapter2_linear_systems/test_jacobi.py
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter2_linear_systems.jacobi import jacobi

# ──────────────────────────────────────────────
# Test 1 — Professor's data
# ──────────────────────────────────────────────
A = np.array([
    [4,  -1,   0,   3],
    [1,  15.5, 3,   8],
    [0,  -1.3, -4,  1.1],
    [14,  5,  -2,  30],
], dtype=float)

b   = np.array([1, 1, 1, 1], dtype=float)
x0  = np.array([0, 0, 0, 0], dtype=float)
tol  = 1e-7
Nmax = 100

# ── Run method ────────────────────────────────
result = jacobi(A, b, x0, tol, Nmax)

# ── Print results ─────────────────────────────
print("\nJacobi Method")
print("=" * 30)

print("\nT:")
for row in result["T"]:
    print(" ".join(f"{v: .6f}" for v in row))

print("\nC:")
print(" ".join(f"{v: .6f}" for v in result["C"]))

print(f"\nRadio espectral:\n {result['spectral_radius']:.6f}")

print("\nIteration table:")
print(result["table"].to_string(index=False))

print(f"\nSolution:   {result['solution']}")
print(f"Iterations: {result['iters']}")
print(f"Error:      {result['error']:.2e}")
print(f"Converged:  {result['converged']}")
