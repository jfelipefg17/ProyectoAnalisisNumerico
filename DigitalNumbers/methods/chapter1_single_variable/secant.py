"""
Secant Method
=============
Finds a root of f(x) = 0 using two initial approximations to build
successive linear interpolations, without needing the derivative.
Converges superlinearly (order ≈ 1.618).

Formula: x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))

Author: Juan Felipe Florez Giraldo
Last updated: April 2026
"""

import pandas as pd


def secant(f, x0: float, x1: float, tol: float, n_max: int) -> dict:
    """
    Secant method to find a root of f(x) = 0.

    Parameters
    ----------
    f     : callable — continuous function f(x)
    x0    : float    — first initial approximation
    x1    : float    — second initial approximation
    tol   : float    — error tolerance (stopping criterion)
    n_max : int      — maximum number of iterations

    Returns
    -------
    dict with keys:
        'root'      : float        — approximated root
        'iters'     : int          — number of iterations performed
        'error'     : float        — final absolute error
        'table'     : pd.DataFrame — iteration table
        'converged' : bool         — True if tolerance was reached

    Table columns
    -------------
    iter   : iteration number (0 and 1 = initial guesses)
    xi     : current approximation      (10 decimal places)
    f(xi)  : f evaluated at xi          (scientific notation)
    E      : absolute error |xi - xi_prev| (scientific notation, blank for iter 0-1)
    """

    rows = []

    # Rows 0 and 1 — initial guesses (no error yet)
    rows.append({"iter": 0, "xi": x0, "f(xi)": f(x0), "E": None})
    rows.append({"iter": 1, "xi": x1, "f(xi)": f(x1), "E": None})

    E = None

    for i in range(2, n_max + 2):

        f_x0  = f(x0)
        f_x1  = f(x1)
        denom = f_x1 - f_x0

        if denom == 0:
            raise ValueError(
                f"f(x1) - f(x0) = 0 at iteration {i}. Method cannot proceed."
            )

        x2 = x1 - f_x1 * (x1 - x0) / denom
        E  = abs(x2 - x1)

        rows.append({
            "iter":  i,
            "xi":    x2,
            "f(xi)": f(x2),
            "E":     E,
        })

        if E < tol:
            return {
                "root":      x2,
                "iters":     i,
                "error":     E,
                "table":     pd.DataFrame(rows),
                "converged": True,
            }

        x0 = x1
        x1 = x2

    return {
        "root":      x1,
        "iters":     n_max,
        "error":     E,
        "table":     pd.DataFrame(rows),
        "converged": False,
    }
