import numpy as np

def gauss_seidel(A, b, x0, tol, Nmax, norm_type=2):

    # Convert inputs to arrays
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)

    n = len(b)

    # Iteration counter
    iterations = 0

    # Initial error
    error = tol + 1

    # Gauss-Seidel iteration
    while error > tol and iterations < Nmax:

        # Store previous approximation
        x_old = x.copy()

        # Compute each component
        for i in range(n):

            summation1 = 0
            summation2 = 0

            # Terms using updated values
            for j in range(i):
                summation1 += A[i, j] * x[j]

            # Terms using previous values
            for j in range(i + 1, n):
                summation2 += A[i, j] * x_old[j]

            # Update current variable
            x[i] = (b[i] - summation1 - summation2) / A[i, i]

        # Compute error using selected norm
        error = np.linalg.norm(x - x_old, ord=norm_type)

        # Increase iteration counter
        iterations += 1

    return x, iterations, error
    
