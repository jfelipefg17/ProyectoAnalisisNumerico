def secante(f, x0, x1, tol, N):
  print("k  x0  x1  f(x2)  error")

for k in range(1, N+1):
  if f(x1) - f(x0) == 0:
      print("Error: división por cero")
      return None
    
  x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
  error = abs(x2-x1)
  
  print(k, x0, x1, x2, f(x2), error)
  
  if error < tol:
    print("Aproximación de la raíz:", x2)
    return x2
  x0 = x1
  x1 = x2

print("El método no convergió")
return 2
