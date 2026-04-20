"""
Incremental Search Method
=========================
Walks from x0 in steps of h, finding all intervals [a, b] where f(x)
changes sign. Each sign change guarantees a root inside that interval
by the Intermediate Value Theorem.

Author: Juan Guillermo Isaza
Last updated: April 2026
"""

import pandas as pd


def incremental_search(f, x0: float, h: float, n_max: int) -> dict:
    """
    Searches for all intervals [xi, xi+1] where f(x) changes sign.

    Parameters
    ----------
    f     : callable — continuous function f(x)
    x0    : float    — starting point of the search
    h     : float    — step size (increment)
    n_max : int      — maximum number of steps allowed

    Returns
    -------
    dict with keys:
        'intervals' : list of (a, b) — all bracketing intervals found
        'iters'     : int            — total steps performed
        'table'     : pd.DataFrame   — iteration table
        'found'     : bool           — True if at least one interval was found

    Table columns
    -------------
    iter     : step number
    xi       : left endpoint of current step
    f(xi)    : f evaluated at xi          (scientific notation)
    xi+1     : right endpoint of current step
    f(xi+1)  : f evaluated at xi+1        (scientific notation)
    """

    x_prev    = x0
    f_prev    = f(x_prev)
    rows      = []
    intervals = []

    for i in range(1, n_max + 1):

        x_curr = x_prev + h
        f_curr = f(x_curr)

        rows.append({
            "iter":    i,
            "xi":      x_prev,
            "f(xi)":   f_prev,
            "xi+1":    x_curr,
            "f(xi+1)": f_curr,
        })

        if f_prev * f_curr < 0:
            intervals.append((x_prev, x_curr))

        x_prev = x_curr
        f_prev = f_curr

    return {
        "intervals": intervals,
        "iters":     n_max,
        "table":     pd.DataFrame(rows),
        "found":     len(intervals) > 0,
    }
