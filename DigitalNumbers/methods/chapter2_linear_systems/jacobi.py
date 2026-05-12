import numpy as np

def jacobi(A, b, x0, tol, Nmax):

    # Convert inputs to arrays
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)

    n = len(b)

    # Iteration counter
    iterations = 0

    # Initial error
    error = tol + 1

    # Jacobi iteration
    while error > tol and iterations < Nmax:

        # Store previous approximation
        x_old = x.copy()

        # New approximation vector
        x_new = np.zeros(n)

        # Compute each component
        for i in range(n):

            summation = 0

            for j in range(n):

                if j != i:
                    summation += A[i, j] * x_old[j]

            x_new[i] = (b[i] - summation) / A[i, i]

        # Compute error
        error = np.linalg.norm(x_new - x_old, ord=np.inf)

        # Update approximation
        x = x_new.copy()

        # Increase iteration counter
        iterations += 1

    return x, iterations, error
