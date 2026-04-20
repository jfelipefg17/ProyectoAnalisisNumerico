def multiple_roots(f, df, d2f, x0, tol, N):
  print("k   x   f(x)   f'(x)   error")

  for k in range(1, N+1):
    fx = f(x0)
    dfx = df(x0)
    d2fx = d2f(x0)
  
    denom = dfx**2 - fx*d2fx
  
    if denom == 0:
      print("Error: división por cero")
      return None
    
    x1 = x0 - (fx * dfx) / denom
    error = abs(x1 - x0)
  
    print(k, x0, fx, dfx, error)
  
    if error < tol:
      print("Aproximación de la raíz:", x1)
      return x1
    x0 = x1
  
  print("El método no covergió")
  return x1
