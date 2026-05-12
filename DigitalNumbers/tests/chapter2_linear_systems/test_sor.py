# Test for SOR Method

A = np.array([
    [4, -1, 0, 3],
    [1, 15.5, 3, 8],
    [0, -1.3, -4, 1.1],
    [14, 5, -2, 30]], dtype=float)

b = np.array([1, 1, 1, 1], dtype=float)

x0 = np.array([0, 0, 0, 0], dtype=float)

tol = 1e-7
Nmax = 100

# Relaxation factor
w = 1.5

# Select norm type
norm_type = 2

# Run method
x, iterations, error = sor(A, b, x0, w, tol, Nmax, norm_type)

# Results
print("Final Results:")

print("x =", x)

print("Iterations =", iterations)

print("Error =", error)
