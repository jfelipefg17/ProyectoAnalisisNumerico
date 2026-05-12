import numpy as np
import pandas as pd


def vandermonde(X, Y):
    """
    Finds the interpolating polynomial coefficients using the Vandermonde method.

    Parameters
    ----------
    X : array-like — x-coordinates of the data points (must be distinct)
    Y : array-like — y-coordinates of the data points

    Returns
    -------
    dict with keys:
        'coefficients' : numpy.ndarray — polynomial coefficients in descending
                         order [a_{n-1}, a_{n-2}, ..., a_0]
        'degree'       : int           — degree of the polynomial (n - 1)
        'matrix'       : numpy.ndarray — Vandermonde matrix A
        'table'        : pd.DataFrame  — table of points and polynomial evaluation
    """

    # --- Convert inputs to numpy arrays ---
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    # --- Validations ---
    if X.shape[0] != Y.shape[0]:
        raise ValueError("X and Y must have the same number of elements")

    if len(np.unique(X)) != len(X):
        raise ValueError("X values must be distinct (no repeated abscissas)")

    if len(X) < 2:
        raise ValueError("At least 2 data points are required")

    n = len(X)

    # --- Build Vandermonde matrix ---
    # Column i contains X^(n-1-i), so A @ Coef = Y
    A = np.zeros((n, n))
    for i in range(n):
        A[:, i] = X ** (n - 1 - i)

    # --- Solve the system A * Coef = Y ---
    Coef = np.linalg.solve(A, Y)

    # --- Build result table ---
    rows = []
    for i in range(n):
        p_xi = np.polyval(Coef, X[i])
        rows.append({
            "i":    i,
            "xi":   round(X[i], 10),
            "yi":   round(Y[i], 10),
            "p(xi)": round(p_xi, 10),
            "error": round(abs(p_xi - Y[i]), 10),
        })

    return {
        "coefficients": Coef,
        "degree":       n - 1,
        "matrix":       A,
        "table":        pd.DataFrame(rows),
    }
