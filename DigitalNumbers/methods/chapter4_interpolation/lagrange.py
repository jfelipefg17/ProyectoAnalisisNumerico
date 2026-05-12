# Method 13 — Lagrange Interpolation Method

import sympy as sp

def lagrange_interpolation(x_values, y_values):
    x = sp.Symbol("x")
    n = len(x_values)
    polynomial = 0

    print("Lagrange basis polynomials:")

    for i in range(n):
        basis = 1

        for j in range(n):
            if i != j:
                basis *= (x - x_values[j]) / (x_values[i] - x_values[j])

        print(f"L_{i}(x) = {sp.expand(basis)}")
        polynomial += y_values[i] * basis

    expanded_polynomial = sp.expand(polynomial)

    print("\nLagrange polynomial:")
    print(expanded_polynomial)

    coefficients = sp.Poly(expanded_polynomial, x).all_coeffs()

    print("\nPolynomial coefficients:")
    print(coefficients)

    return expanded_polynomial, coefficients


x_values = [-1, 0, 3, 4]
y_values = [15.5, 3, 8, 1]

lagrange_interpolation(x_values, y_values)
