"""
Test — Secant Method
========================
Runs one test case and prints the iteration table.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.secant import secant

# ──────────────────────────────────────────────
# Helper to print results consistently
# ──────────────────────────────────────────────
def print_results(label: str, result: dict):
    print(f"\n{'='*55}")
    print(f"  {label}")
    print(f"{'='*55}")
    print(result["table"].to_string(index=False))
    print(f"\n  Iterations : {result['iters']}")
    print(f"  Root       : {result['root']:.10f}")
    print(f"  Error      : {result['error']:.2e}")
    print(f"  Status     : {'Converged ✓' if result['converged'] else 'Max iterations reached'}")
    print()

# ──────────────────────────────────────────────
# Test — f(x) = ln(sin²(x) + 1) - 1/2
# Initial values: x0 = 0.5, x1 = 1
# ──────────────────────────────────────────────
f = lambda x: np.log(np.sin(x)**2 + 1) - 0.5

result = secant(f=f, x0=0.5, x1=1.0, tol=1e-7, N=100)

print_results("Secant Method Test", result)
