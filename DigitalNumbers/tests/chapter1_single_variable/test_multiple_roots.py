"""
Test — Multiple Roots Method
========================
Runs one test case and prints the iteration table.

"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.multiple_roots import multiple_roots

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
# Test — h(x) = e^x - x - 1
# x0 = 1
# ──────────────────────────────────────────────
h = lambda x: np.exp(x) - x - 1
dh = lambda x: np.exp(x) - 1
d2h = lambda x: np.exp(x)

result = multiple_roots(f=h, df=dh, d2f=d2h, x0=1.0, tol=1e-7, N=100)

print_results("Multiple Roots Test", result)
