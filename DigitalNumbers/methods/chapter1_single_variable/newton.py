"""
Newton-Raphson Method
=====================
Finds a root of f(x) = 0 using the tangent line at each iteration.
Converges quadratically when the initial guess is close to the root
and f'(x) ≠ 0.

Formula: x_{n+1} = x_n - f(x_n) / f'(x_n)

Author: Juan Felipe Florez Giraldo
Last updated: April 2026
"""

import pandas as pd


def newton_method(f, df, x0: float, tol: float, n_max: int) -> dict:
    """
    Newton-Raphson method to find a root of f(x) = 0.

    Parameters
    ----------
    f     : callable — function whose root we want to find
    df    : callable — first derivative of f
    x0    : float    — initial guess
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
    iter   : iteration number (0 = initial guess)
    xi     : current approximation      (10 decimal places)
    f(xi)  : f evaluated at xi          (scientific notation)
    E      : absolute error |xi - xi_prev| (scientific notation, blank at iter 0)
    """

    xi   = x0
    rows = []

    # Row 0 — initial guess (no error yet)
    rows.append({
        "iter":  0,
        "xi":    xi,
        "f(xi)": f(xi),
        "E":     None,
    })

    for i in range(1, n_max + 1):

        f_xi  = f(xi)
        df_xi = df(xi)

        if df_xi == 0:
            raise ValueError(
                f"Derivative is zero at xi = {xi:.10f}. Method cannot proceed."
            )

        xi_next = xi - f_xi / df_xi
        E       = abs(xi_next - xi)

        rows.append({
            "iter":  i,
            "xi":    xi_next,
            "f(xi)": f(xi_next),
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
