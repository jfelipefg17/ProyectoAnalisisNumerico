import numpy as np

def forward_substitution(M):
    """
    Solves a lower triangular system using forward substitution.
    The input matrix M must be the augmented matrix [L | b].
    """

    n = M.shape[0]
    x = np.zeros(n)

    x[0] = M[0, n] / M[0, 0]

    for i in range(1, n):
        s = np.dot(M[i, :i], x[:i])
        x[i] = (M[i, n] - s) / M[i, i]

    return x


def backward_substitution(M):
    """
    Solves an upper triangular system using backward substitution.
    The input matrix M must be the augmented matrix [U | b].
    """

    n = M.shape[0]
    x = np.zeros(n)

    x[n - 1] = M[n - 1, n] / M[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        s = np.dot(M[i, i + 1:n], x[i + 1:n])
        x[i] = (M[i, n] - s) / M[i, i]

    return x


def LU_simple(A, b):
    """
    Solves Ax = b using LU factorization with simple Gaussian elimination.

    Returns:
        x       : solution vector
        L       : lower triangular matrix
        U       : upper triangular matrix
        stages  : list containing all stages of M, L, and U
    """

    # --- Convert inputs to numpy arrays ---
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # --- Validations ---
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square")

    n = A.shape[0]

    if b.shape[0] != n:
        raise ValueError("Vector b size must match A")

    if np.linalg.det(A) == 0:
        raise ValueError("Matrix A must be non-singular")

    # --- Initialization ---
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A.copy()

    stages = []

    # --- Store initial stage ---
    stages.append({
        "M": M.copy(),
        "L": L.copy(),
        "U": U.copy()
    })

    # --- LU Factorization ---
    for k in range(n - 1):

        if M[k, k] == 0:
            raise ValueError("Zero pivot encountered")

        for i in range(k + 1, n):

            if M[i, k] != 0:

                # Multiplier
                L[i, k] = M[i, k] / M[k, k]

                # Row elimination
                M[i, k:n] = M[i, k:n] - L[i, k] * M[k, k:n]

        # Build U progressively
        U[k, k:n] = M[k, k:n]
        U[k + 1, k + 1:n] = M[k + 1, k + 1:n]

        # Store stage
        stages.append({
            "M": M.copy(),
            "L": L.copy(),
            "U": U.copy()
        })

    U[n - 1, n - 1] = M[n - 1, n - 1]

    if U[n - 1, n - 1] == 0:
        raise ValueError("Zero pivot encountered")

    # --- Forward substitution ---
    z = forward_substitution(np.column_stack((L, b)))

    # --- Backward substitution ---
    x = backward_substitution(np.column_stack((U, z)))

    return x, L, U, stages
