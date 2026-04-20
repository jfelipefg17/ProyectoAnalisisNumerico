"""
Test — Naive Gaussian Elimination
====================================
Uses the exact inputs specified by the professor in Prueba_métodos_1.pdf

To run (from DigitalNumbers/ root):
    python tests/chapter2_linear_systems/test_naive_gaussian_elimination.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import numpy as np
from methods.chapter2_linear_systems.naive_gaussian_elimination import naive_gaussian_elimination
from tests.print_helpers import print_system_result

# ── Professor's exact inputs ──────────────────────────────────────────────────
# A = [[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]]
# b = [1,1,1,1]
# Expected x ≈ [0.038495, -0.180227, -0.309711, 0.247594]
# ─────────────────────────────────────────────────────────────────────────────
A = [[2, -1, 0, 3],
     [1, 0.5, 3, 8],
     [0, 13, -2, 11],
     [14, 5, -2, 3]]
b = [1, 1, 1, 1]

x, stages = naive_gaussian_elimination(A, b, return_stages=True)
print_system_result("Naive Gaussian Elimination  |  4x4 system", x, stages)
