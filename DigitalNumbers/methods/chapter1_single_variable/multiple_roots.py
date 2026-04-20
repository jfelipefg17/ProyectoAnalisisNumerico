def multiple_roots(f, df, d2f, x0, tol, N):
    import pandas as pd

    data = []
    error = float("inf")

    for k in range(1, N+1):
        fx = f(x0)
        dfx = df(x0)
        d2fx = d2f(x0)

        denom = dfx**2 - fx*d2fx

        if denom == 0:
            return {
                "table": pd.DataFrame(data),
                "iters": k,
                "root": x0,
                "error": error,
                "converged": False
            }

        x1 = x0 - (fx * dfx) / denom
        error = abs(x1 - x0)

        data.append([k, x0, fx, dfx, error])

        if error < tol:
            return {
                "table": pd.DataFrame(data, columns=["k", "x", "f(x)", "f'(x)", "error"]),
                "iters": k,
                "root": x1,
                "error": error,
                "converged": True
            }

        x0 = x1

    return {
        "table": pd.DataFrame(data, columns=["k", "x", "f(x)", "f'(x)", "error"]),
        "iters": N,
        "root": x1,
        "error": error,
        "converged": False
    }
