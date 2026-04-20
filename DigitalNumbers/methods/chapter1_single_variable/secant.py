def secant(f, x0, x1, tol, N):
    import pandas as pd

    data = []
    error = float("inf")

    for k in range(1, N+1):
        if f(x1) - f(x0) == 0:
            return {
                "table": pd.DataFrame(data),
                "iters": k,
                "root": x1,
                "error": error,
                "converged": False
            }

        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        error = abs(x2 - x1)

        data.append([k, x2, f(x2), error])

        if error < tol:
            return {
                "table": pd.DataFrame(data, columns=["iter","xi","f(xi)","error"]),
                "iters": k,
                "root": x2,
                "error": error,
                "converged": True
            }

        x0 = x1
        x1 = x2

    return {
        "table": pd.DataFrame(data, columns=["iter","xi","f(xi)","error"]),
        "iters": N,
        "root": x2,
        "error": error,
        "converged": False
    }
