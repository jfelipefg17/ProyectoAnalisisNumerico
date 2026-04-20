"""
Fixed Point Iteration Method
=============================
Solves x = g(x) by repeatedly applying g starting from an initial guess.
Convergence is guaranteed when |g'(x)| < 1 near the fixed point.

Formula: x_{n+1} = g(x_n)

Author: Luciana Pineda
Last updated: April 2026
"""

import pandas as pd


def fixed_point_method(g, x0: float, tol: float, n_max: int) -> dict:
    """
    Fixed Point Iteration method to solve x = g(x).

    Parameters
    ----------
    g     : callable — iteration function in the form x = g(x)
    x0    : float    — initial guess
    tol   : float    — error tolerance (stopping criterion)
    n_max : int      — maximum number of iterations

    Returns
    -------
    dict with keys:
        'root'      : float        — approximated fixed point
        'iters'     : int          — number of iterations performed
        'error'     : float        — final absolute error
        'table'     : pd.DataFrame — iteration table
        'converged' : bool         — True if tolerance was reached

    Table columns
    -------------
    iter   : iteration number (0 = initial guess)
    xi     : current approximation      (10 decimal places)
    g(xi)  : g evaluated at xi          (10 decimal places)
    f(xi)  : residual xi - g(xi)        (scientific notation)
    E      : absolute error |xi - xi_prev| (scientific notation, blank at iter 0)
    """

    xi   = x0
    rows = []

    # Row 0 — initial guess (no error yet)
    rows.append({
        "iter":  0,
        "xi":    xi,
        "g(xi)": g(xi),
        "f(xi)": xi - g(xi),
        "E":     None,
    })

    for i in range(1, n_max + 1):

        xi_next = g(xi)
        E       = abs(xi_next - xi)

        rows.append({
            "iter":  i,
            "xi":    xi_next,
            "g(xi)": g(xi_next),
            "f(xi)": xi_next - g(xi_next),
            "E":     E,
        })

        if E < tol:
            return {
                "root":      xi_next,
                "iters":     i,
                "error":     E,
                "table":     pd.DataFrame(rows),
                "converged": True,
            }

        xi = xi_next

    return {
        "root":      xi,
        "iters":     n_max,
        "error":     E,
        "table":     pd.DataFrame(rows),
        "converged": False,
    }
