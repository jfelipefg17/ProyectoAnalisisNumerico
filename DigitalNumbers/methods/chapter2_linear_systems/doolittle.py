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

def doolittle(A, b):
    """
    Solves Ax = b using Doolittle factorization.

    Returns:
        x       : solution vector
        L       : lower triangular matrix
        U       : upper triangular matrix
        stages  : list containing all stages of L and U
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
    U = np.eye(n)

    stages = []

    # --- Store initial stage ---
    stages.append({
        "A": A.copy()
    })

    # --- Doolittle Factorization ---
    for i in range(n - 1):

        # Compute row i of U
        for j in range(i, n):

            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # Zero pivot validation
        if U[i, i] == 0:
            raise ValueError("Zero pivot encountered")

        # Compute column i of L
        for j in range(i + 1, n):

            L[j, i] = (
                A[j, i] - np.dot(L[j, :i], U[:i, i])
            ) / U[i, i]

        # Store stage
        stages.append({
            "L": L.copy(),
            "U": U.copy()
        })

    # Compute last element of U
    U[n - 1, n - 1] = (
        A[n - 1, n - 1]
        - np.dot(L[n - 1, :n - 1], U[:n - 1, n - 1])
    )

    if U[n - 1, n - 1] == 0:
        raise ValueError("Zero pivot encountered")

    # --- Forward substitution ---
    z = forward_substitution(np.column_stack((L, b)))

    # --- Backward substitution ---
    x = backward_substitution(np.column_stack((U, z)))

    return x, L, U, stages
