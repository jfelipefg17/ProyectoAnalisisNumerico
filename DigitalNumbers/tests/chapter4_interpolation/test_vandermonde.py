"""
Test — Vandermonde Interpolation
==================================

Runs test cases for the Vandermonde interpolating polynomial method
and prints the coefficient table and evaluation at each data point.

To run (from inside DigitalNumbers/):
    python tests/chapter4_interpolation/test_vandermonde.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np

from methods.chapter4_interpolation.vandermonde import vandermonde


def print_vandermonde_result(label, result):
    """Print coefficients, polynomial expression, and evaluation table."""

    print(f"\n{'='*65}")
    print(f"  {label}")
    print(f"{'='*65}\n")

    # Polynomial expression
    n = result["degree"]
    Coef = result["coefficients"]
    terms = []
    for i, c in enumerate(Coef):
        exp = n - i
        if exp == 0:
            terms.append(f"{c:.6f}")
        elif exp == 1:
            terms.append(f"{c:.6f}*x")
        else:
            terms.append(f"{c:.6f}*x^{exp}")
    print(f"  p(x) = {' + '.join(terms)}\n")

    # Evaluation table
    df = result["table"]
    header = f"{'i':>4}  {'xi':>16}  {'yi':>16}  {'p(xi)':>16}  {'error':>14}"
    print(header)
    print("-" * len(header))
    for _, row in df.iterrows():
        print(
            f"  {int(row['i']):>2}  "
            f"{row['xi']:>16.10f}  "
            f"{row['yi']:>16.10f}  "
            f"{row['p(xi)']:>16.10f}  "
            f"{row['error']:>14.4e}"
        )

    print()


# ──────────────────────────────────────────────
# Test 1 — Simple quadratic (3 points)
# ──────────────────────────────────────────────

X1 = [1.0, 2.0, 3.0]
Y1 = [1.0, 4.0, 9.0]   # y = x^2

result1 = vandermonde(X1, Y1)
print_vandermonde_result(
    "Vandermonde  |  3 points  |  y = x^2  expected",
    result1
)

# ──────────────────────────────────────────────
# Test 2 — Four points
# ──────────────────────────────────────────────

X2 = [0.0, 1.0, 2.0, 3.0]
Y2 = [1.0, 2.0, 5.0, 10.0]

result2 = vandermonde(X2, Y2)
print_vandermonde_result(
    "Vandermonde  |  4 points",
    result2
)
