"""
Multiple Roots Method
======================
A modified Newton method for roots with multiplicity m > 1.
Standard Newton converges linearly at multiple roots; this variant
restores quadratic convergence using both f' and f''.

Formula: x_{n+1} = x_n - f(x_n)·f'(x_n) / ( f'(x_n)² - f(x_n)·f''(x_n) )

Author: Luciana Pineda
Last updated: April 2026
"""

import pandas as pd


def multiple_roots(f, df, d2f, x0: float, tol: float, n_max: int) -> dict:
    """
    Multiple Roots method for f(x) = 0 with multiplicity > 1.

    Parameters
    ----------
    f     : callable — function whose root we want to find
    df    : callable — first derivative of f
    d2f   : callable — second derivative of f
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

    E = None

    for i in range(1, n_max + 1):

        f_xi   = f(xi)
        df_xi  = df(xi)
        d2f_xi = d2f(xi)
        denom  = df_xi**2 - f_xi * d2f_xi

        if denom == 0:
            if abs(f_xi) <= tol:
                return {
                    "root": xi, "iters": i, "error": E if E else 0.0,
                    "table": pd.DataFrame(rows), "converged": True,
                }
            raise ValueError(
                f"Denominator f'² - f·f'' = 0 at xi = {xi:.10f} "
                f"but f(xi) = {f_xi:.4e}. Method cannot proceed."
            )

        xi_next = xi - (f_xi * df_xi) / denom
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
