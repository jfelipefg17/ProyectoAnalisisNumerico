import math

def newton_method(f, df, x0, tol=1e-8, max_iter=100):
    """
    Newton-Raphson Method for solving f(x) = 0

    📌 METHOD IDEA:
    Uses the tangent line at x_n to approximate the root.

    Formula:
        x_{n+1} = x_n - f(x_n)/f'(x_n)

    📌 CONDITIONS:
    - The function must be differentiable near the root
    - The derivative must not be zero
    - A good initial guess is required

    📌 PARAMETERS:
    f        : function
    df       : derivative of f
    x0       : initial guess
    tol      : tolerance (stopping criterion)
    max_iter : maximum number of iterations

    📌 RETURNS:
    Approximation of the root
    """

    print("\nResults Table:\n")
    print("| iter |      xi        |    f(xi)     |      E      |")
    print("|------|----------------|--------------|-------------|")

    x_n = x0

    # 🔹 Iteration 0
    f_xn = f(x_n)
    print(f"|  0   | {x_n:>14.10f} | {f_xn:>12.1e} |             |")

    for i in range(1, max_iter + 1):

        # Evaluate derivative
        df_xn = df(x_n)

        # ❗ CONDITION 1: avoid division by zero
        if df_xn == 0:
            print("\nError: derivative is zero. Method fails.")
            return None

        # 🔹 Newton formula
        x_next = x_n - f_xn / df_xn

        # 🔹 Absolute error
        error = abs(x_next - x_n)

        # Evaluate function at new point
        f_xnext = f(x_next)

        # 🔹 Print table row
        print(f"| {i:^4} | {x_next:>14.10f} | {f_xnext:>12.1e} | {error:>11.1e} |")

        # ❗ CONDITION 2: stopping criterion
        if error < tol:
            print(f"\nAn approximation of the root was found at {x_next}")
            return x_next

        # Update values
        x_n = x_next
        f_xn = f_xnext

    # ❗ CONDITION 3: max iterations reached
    print("\nThe method did not converge within the maximum number of iterations.")
    return x_n


# 🔹 FUNCTION
def f(x):
    """
    f(x) = ln(sin²(x) + 1) - 0.5
    """
    return math.log(math.sin(x)**2 + 1) - 0.5


# 🔹 DERIVATIVE
def df(x):
    """
    f'(x) = (2 sin(x) cos(x)) / (sin²(x) + 1)
    """
    return (2 * math.sin(x) * math.cos(x)) / (math.sin(x)**2 + 1)


# 🔹 INITIAL VALUE
x0 = 0.5

# 🔹 EXECUTION
root = newton_method(f, df, x0)

print("\nFinal Result:")
print(f"Approximate root = {root}")
