"""
Test — Incremental Search Method
==================================
Uses the exact inputs specified by the professor in Prueba_métodos_1.pdf

To run (from DigitalNumbers/ root):
    python tests/chapter1_single_variable/test_incremental_search.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter1_single_variable.incremental_search import incremental_search


def print_results(label: str, result: dict):
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    print(result["table"].to_string(index=False))
    print(f"\n  Total steps : {result['iters']}")
    if result["found"]:
        print(f"  Intervals found ({len(result['intervals'])}):")
        for a, b in result["intervals"]:
            print(f"    [{a:.10f}, {b:.10f}]")
        print(f"  Status      : Sign changes found ✓")
    else:
        print(f"  Status      : No sign change found")
    print()


# ── Professor's exact inputs ──────────────────────────────────────────────────
# f(x) = ln(sin²(x) + 1) − 1/2
# x0 = -3,  h = 0.5,  N = 100
# ─────────────────────────────────────────────────────────────────────────────
f = lambda x: np.log(np.sin(x)**2 + 1) - 0.5

result = incremental_search(f=f, x0=-3, h=0.5, n_max=100)
print_results("f(x) = ln(sin²(x)+1) - 1/2  |  x0=-3, h=0.5, N=100", result)
