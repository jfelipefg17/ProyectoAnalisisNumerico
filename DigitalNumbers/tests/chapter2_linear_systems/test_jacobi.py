"""
Jacobi Method
=============
Solves the linear system Ax = b iteratively.
At each step every component is updated using only values from the
previous iteration (no in-place updates).
Converges when the spectral radius of T = -D⁻¹(L+U) is less than 1.
Formula: x^{k+1} = T · x^k + C,   T = -D⁻¹(L+U),   C = D⁻¹ · b
Author: Juan Felipe Florez Giraldo
Last updated: April 2026
"""

import numpy as np
import pandas as pd


def jacobi(A, b, x0, tol: float, n_max: int, norm_type=2) -> dict:
    """
    Jacobi iterative method to solve Ax = b.

    Parameters
    ----------
    A         : array-like — n×n coefficient matrix
    b         : array-like — right-hand side vector of length n
    x0        : array-like — initial guess vector of length n
    tol       : float      — error tolerance (stopping criterion)
    n_max     : int        — maximum number of iterations
    norm_type : int|float  — norm used for the error (1, 2, or np.inf). Default: 2

    Returns
    -------
    dict with keys:
        'solution'        : np.ndarray   — approximated solution vector
        'iters'           : int          — number of iterations performed
        'error'           : float        — final norm-2 error
        'table'           : pd.DataFrame — iteration table
        'converged'       : bool         — True if tolerance was reached
        'T'               : np.ndarray   — iteration matrix -D⁻¹(L+U)
        'C'               : np.ndarray   — constant vector D⁻¹·b
        'spectral_radius' : float        — spectral radius of T

    Table columns
    -------------
    iter : iteration number (0 = initial guess)
    E    : error ||x_new - x_old|| using norm_type  (None for iter 0)
    x1 … xn : components of the solution vector at this iteration
    """
    A  = np.array(A,  dtype=float)
    b  = np.array(b,  dtype=float)
    x  = np.array(x0, dtype=float)
    n  = len(b)

    # ── Iteration matrix T = -D⁻¹(L+U) and vector C = D⁻¹·b ──────────────
    D_inv = np.diag(1.0 / np.diag(A))
    LU    = A - np.diag(np.diag(A))          # off-diagonal part of A
    T     = -D_inv @ LU
    C     =  D_inv @ b

    # ── Spectral radius ────────────────────────────────────────────────────
    spectral_radius = float(np.max(np.abs(np.linalg.eigvals(T))))

    # ── Column names for solution components ──────────────────────────────
    x_cols = [f"x{i + 1}" for i in range(n)]

    # ── Row 0 — initial guess (no error yet) ──────────────────────────────
    rows = [{
        "iter": 0,
        "E": None,
        **dict(zip(x_cols, x)),
    }]

    E = None
    for k in range(1, n_max + 1):
        x_new = T @ x + C
        E     = float(np.linalg.norm(x_new - x, ord=norm_type))

        rows.append({
            "iter": k,
            "E": E,
            **dict(zip(x_cols, x_new)),
        })

        x = x_new

        if E < tol:
            return {
                "solution":        x,
                "iters":           k,
                "error":           E,
                "table":           pd.DataFrame(rows),
                "converged":       True,
                "T":               T,
                "C":               C,
                "spectral_radius": spectral_radius,
            }

    return {
        "solution":        x,
        "iters":           n_max,
        "error":           E,
        "table":           pd.DataFrame(rows),
        "converged":       False,
        "T":               T,
        "C":               C,
        "spectral_radius": spectral_radius,
    }
