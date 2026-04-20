"""
False Position Method  (Regula Falsi)
======================================
Finds a root of f(x) = 0 on [a, b] using linear interpolation between
the endpoints rather than simple halving.

Formula: xm = ( f(b)·a − f(a)·b ) / ( f(b) − f(a) )

Requires: f(a) * f(b) < 0

Author: Juan Guillermo Isaza
Last updated: April 2026
"""

import pandas as pd


def false_position(f, a: float, b: float, tol: float, n_max: int) -> dict:
    """
    False Position (Regula Falsi) method to find a root of f(x) = 0 on [a, b].

    Parameters
    ----------
    f     : callable — continuous function f(x)
    a     : float    — left endpoint of the initial interval
    b     : float    — right endpoint of the initial interval
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
    iter   : iteration number
    a      : left endpoint                          (10 decimal places)
    xm     : linear interpolation estimate           (10 decimal places)
    b      : right endpoint                         (10 decimal places)
    f(xm)  : f evaluated at xm                      (scientific notation)
    E      : absolute error |xm - xm_prev|           (scientific notation)
    """

    if f(a) * f(b) > 0:
        raise ValueError(
            f"f(a) and f(b) must have opposite signs. "
            f"Got f({a}) = {f(a):.6e},  f({b}) = {f(b):.6e}"
        )

    f_a  = f(a)
    f_b  = f(b)
    xm   = (f_b * a - f_a * b) / (f_b - f_a)
    f_xm = f(xm)
    E    = None
    count = 1
    rows  = []

    while (E is None or E > tol) and count < n_max:

        rows.append({
            "iter":  count,
            "a":     a,
            "xm":    xm,
            "b":     b,
            "f(xm)": f_xm,
            "E":     E,
        })

        if f_a * f_xm < 0:
            b    = xm
            f_b  = f_xm
        else:
            a    = xm
            f_a  = f_xm

        xm_prev = xm
        f_a     = f(a)
        f_b     = f(b)
        xm      = (f_b * a - f_a * b) / (f_b - f_a)
        f_xm    = f(xm)
        E       = abs(xm - xm_prev)
        count  += 1

    rows.append({
        "iter":  count,
        "a":     a,
        "xm":    xm,
        "b":     b,
        "f(xm)": f_xm,
        "E":     E,
    })

    return {
        "root":      xm,
        "iters":     count,
        "error":     E,
        "table":     pd.DataFrame(rows),
        "converged": E <= tol,
    }
