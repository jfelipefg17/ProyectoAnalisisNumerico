# Method 12 — Newton Interpolation Method

import numpy as np
import sympy as sp

def newton_interpolation(x_values, y_values):
    n = len(x_values)
    table = np.zeros((n, n))
    table[:, 0] = y_values

    print("Divided Differences Table:")

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_values[i + j] - x_values[i])

    print(table)

    coefficients = table[0, :]
    print("\nNewton coefficients:")
    print(coefficients)

    x = sp.Symbol("x")
    polynomial = coefficients[0]

    product_term = 1
    for i in range(1, n):
        product_term *= (x - x_values[i - 1])
        polynomial += coefficients[i] * product_term

    expanded_polynomial = sp.expand(polynomial)

    print("\nNewton polynomial:")
    print(expanded_polynomial)

    return expanded_polynomial, coefficients


x_values = [-1, 0, 3, 4]
y_values = [15.5, 3, 8, 1]

newton_interpolation(x_values, y_values)
