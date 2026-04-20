import math

def fixed_point_method(g, f, x0, tol=1e-7, max_iter=100):
    """
    Fixed-Point Iteration Method for solving f(x) = 0

    📌 METHOD IDEA:
    Transform f(x) = 0 into x = g(x), then iterate:

        x_{n+1} = g(x_n)

    📌 CONDITIONS:
    - g(x) must be continuous
    - |g'(x)| < 1 near the root (for convergence)
    - A good initial guess is required

    📌 PARAMETERS:
    g        : iteration function
    f        : original function (for evaluation)
    x0       : initial guess
    tol      : tolerance
    max_iter : maximum iterations

    📌 RETURNS:
    Approximation of the root
    """

    print("\nResults Table:\n")
    print("| iter |      xi        |     g(xi)      |    f(xi)     |      E      |")
    print("|------|----------------|----------------|--------------|-------------|")

    x_n = x0

    # 🔹 Iteration 0
    g_xn = g(x_n)
    f_xn = f(x_n)

    print(f"|  0   | {x_n:>14.10f} | {g_xn:>14.10f} | {f_xn:>12.1e} |             |")

    for i in range(1, max_iter + 1):

        # Apply fixed-point formula
        x_next = g(x_n)

        # Error
        error = abs(x_next - x_n)

        # Evaluate functions
        g_xnext = g(x_next)
        f_xnext = f(x_next)

        # Print row
        print(f"| {i:^4} | {x_next:>14.10f} | {g_xnext:>14.10f} | {f_xnext:>12.1e} | {error:>11.1e} |")

        # Stopping condition
        if error < tol:
            print(f"\nAn approximation of the root was found at {x_next}")
            return x_next

        x_n = x_next

    print("\nThe method did not converge within the maximum number of iterations.")
    return x_n


# 🔹 ORIGINAL FUNCTION
def f(x):
    return x - (math.log(math.sin(x)**2 + 1) - 0.5)


# 🔹 ITERATION FUNCTION g(x)
def g(x):
    return math.log(math.sin(x)**2 + 1) - 0.5


# 🔹 INITIAL VALUE
x0 = -0.5

# 🔹 EXECUTION
root = fixed_point_method(g, f, x0)

print("\nFinal Result:")
print(f"Approximate root = {root}")
