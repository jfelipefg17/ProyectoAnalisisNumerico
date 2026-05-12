# Pseudocode — Chapter 1: Single Variable Equations
**DigitalNumbers Project · EAFIT University**
Author: Juan Guillermo Isaza · April 2026

---

## Method 1 — Incremental Search

**Purpose:** Find an interval [a, b] where the function changes sign, which guarantees
that a root exists somewhere inside it.

**Inputs:**
- f — a continuous function
- x0 — the starting point of the search
- h — the size of each step forward
- N — maximum number of steps allowed

**Output:**
- The interval [a, b] where the sign change was found

---

**BEGIN**

Set the current point to x0 and evaluate f there.  
Move one step forward to get the next point, and evaluate f there too.

Repeat up to N times:

> Check whether the function values at the two consecutive points have opposite signs.  
> If they do, a root must lie between them — stop and report that interval.
>
> If they do not, discard the left point and move one step forward again,  
> keeping only the most recent point and evaluating the function at the new one.

If no sign change was found after N steps, report that no interval was found.

**END**

---

## Method 2 — Bisection

**Purpose:** Given an interval [a, b] where a sign change is known to exist,
repeatedly cut the interval in half and keep only the half that still contains
the sign change, until the interval is small enough.

**Inputs:**
- f — a continuous function
- a, b — the endpoints of the starting interval (f(a) and f(b) must have opposite signs)
- tol — the acceptable error (how small the interval must get before stopping)
- N — maximum number of iterations allowed

**Output:**
- The midpoint of the final interval, which approximates the root

---

**BEGIN**

Verify that f(a) and f(b) have opposite signs. If not, stop — the method cannot proceed.

Compute the midpoint of [a, b] and evaluate f there.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Remember the current midpoint before updating it.
>
> Check the sign of f at the midpoint:
> - If f(a) and f(midpoint) have opposite signs, the root is in the left half —  
>   replace b with the current midpoint.
> - Otherwise, the root is in the right half —  
>   replace a with the current midpoint.
>
> Compute the new midpoint of the updated interval.  
> Evaluate f at the new midpoint.  
> Calculate the error as the absolute difference between the new and old midpoints.  
> Increase the iteration counter by one.

Report the final midpoint as the approximation of the root.

**END**

---

## Method 3 — False Position (Regula Falsi)

**Purpose:** Similar to bisection, but instead of cutting the interval exactly in half,
it draws a straight line between the two endpoints and uses the point where that
line crosses zero as the next estimate. This tends to converge faster than bisection
when the function behaves smoothly.

**Inputs:**
- f — a continuous function
- a, b — the endpoints of the starting interval (f(a) and f(b) must have opposite signs)
- tol — the acceptable error
- N — maximum number of iterations allowed

**Output:**
- The estimated root where the line crossed zero

---

**BEGIN**

Verify that f(a) and f(b) have opposite signs. If not, stop — the method cannot proceed.

Evaluate f at both endpoints.  
Compute the first estimate by drawing a straight line between (a, f(a)) and (b, f(b))  
and finding where it crosses the x-axis. This is done with the formula:

> p = ( f(b)·a − f(a)·b ) / ( f(b) − f(a) )

Evaluate f at this new point p.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Remember the current estimate p before updating it.
>
> Check the sign of f at p:
> - If f(a) and f(p) have opposite signs, the root is between a and p —  
>   replace b with p and update f(b).
> - Otherwise, the root is between p and b —  
>   replace a with p and update f(a).
>
> Re-evaluate f at the updated endpoints a and b.  
> Compute the new estimate p using the same straight-line formula as before.  
> Evaluate f at the new p.  
> Calculate the error as the absolute difference between the new and old estimates.  
> Increase the iteration counter by one.

Report the final estimate p as the approximation of the root.

**END**

---
---

## Method 4 — Newton-Raphson

**Purpose:** Starting from an initial guess, this method uses the tangent line of the function to generate better approximations of the root at each step. It usually converges very fast when the initial guess is close to the actual root.

**Inputs:**
- f — a function
- df — derivative of the function
- x0 — initial approximation
- tol — acceptable error
- N — maximum number of iterations

**Output:**
- Approximation of the root

---

**BEGIN**

Set the current approximation to x0 and evaluate f and df at that point.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Check if the derivative at the current point is zero.  
> If it is, stop — the method cannot proceed due to division by zero.
>
> Compute the next approximation using the tangent line formula:  
> x_next = x_current − f(x_current) / df(x_current)
>
> Calculate the error as the absolute difference between the new and old approximation.  
>
> Update the current approximation with the new value.  
> Evaluate f and df at the new point.  
> Increase the iteration counter by one.

Report the final approximation as the root.

**END**

---

## Method 5 — Fixed Point Iteration

**Purpose:** Transform the equation into the form x = g(x) and generate a sequence of approximations by repeatedly evaluating the function. The success of the method depends strongly on the choice of g(x).

**Inputs:**
- g — function written as x = g(x)
- x0 — initial approximation
- tol — acceptable error
- N — maximum number of iterations

**Output:**
- Approximation of the root

---

**BEGIN**

Set the current approximation to x0.  
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

> Compute the next approximation by evaluating the function:  
> x_next = g(x_current)
>
> Calculate the error as the absolute difference between the new and old approximation.  
>
> Update the current approximation with the new value.  
> Increase the iteration counter by one.

Report the final approximation as the root.

**END**
## Method 6 - Secant 

**Purpose:** Approximate a root of a nonlinear function by using two initial guesses and constructing successive linear approximations, without requiring the computation of derivatives.

**Inputs:**
- f — a continuous function
- x0, x1 — two initial approximations to the root
- tol — tolerance that determines when the approximation is accurate enough
- N — maximum number of iterations allowed

**Output:**
The approximate value of the root, or a message indicating that the method failed to converge within the maximum number of iterations.

---

**BEGIN**

Start with two initial approximations x0 and x1.
Evaluate f at both points.

Compute the first estimate using the secant formula based on x0 and x1.

Evaluate f at this new estimate.
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

>Remember the previous approximation before updating it.  
>Compute a new approximation using the secant formula with the two most recent values.
>
>Check that the denominator is not zero:
> - If it is zero, stop - the method cannot proceed.
>
>Evaluate f at the new approximation.  
>Calculate the error as the absolute difference between the new and previous approximations.  
>Update the values by discarding the oldest approximation and keeping the two most recent ones.  
>Increase the iteration counter by one.  

Report the final approximation as the root.

**END**

---

## Method 7 - Multiple Roots 

**Purpose:** Approximate a root of a nonlinear function with multiplicity greater than one by modifying the Newton method to improve convergence.

**Inputs:**
f — a continuous function
f′ — first derivative of the function
f″ — second derivative of the function
x0 — initial approximation to the root
tol — tolerance that determines when the approximation is accurate enough
N — maximum number of iterations allowed

**Output:**
The approximate value of the root, or a message indicating that the method failed to converge within the maximum number of iterations.

---

**BEGIN**

Start with an initial approximation x0.
Evaluate f, f', and f'' at this point.

Compute the first estimate using the multiple roots formula.

Evaluate f at this new estimate.
Set the initial error to a large number so the loop starts.

Repeat until the error is smaller than the tolerance or N iterations are reached:

>Remember the current approximation before updating it.  
>Compute a new approximation using the multiple roots formula.
>
>Check that the denominator is not zero:
> - If it is zero, stop - the method cannot proceed.
>   
>Evaluate f, f', and f'' at the new approximation.  
>Calculate the error as the absolute difference between the new and previous approximations.  
>Update the approximation with the new value.  
>Increase the iteration counter by one.  

Report the fina approximation as the root.

**END**

---

# Pseudocode — Chapter 2: Linear Systems
**DigitalNumbers Project · EAFIT University**
Author: Jerónimo Mesa Alzate · April 2026

---

## Method 1 — Naive Gaussian Elimination

**Purpose:** To solve de Equation Ax = b by reducing the coeficient matrix into it's upper triangular form using simple row equations in the augmented matrix, then, back substitution is used to solve the variables starting from the last row to find the values of the x components

**Inputs:**
- Matrix A (nxn)
- Vector b (nx1)
  
**Output:**
- Solution vector x
- Intermediate matrices of the process

**BEGIN**  

Check input dimensions: If A is not square (nxn) → Stop, and if b is not compatible with b (nx1) → Stop  
Check if the det(A) = 0 if it is → Stop.  
Chack if the number in the position A(1,1) = 0, if it is → Stop.  


> Form the augmented martix Aug = [A|b], then start the process of elimination:  
> For k = 1 to n-1:  
>   If Aug[k,k] = 0:  
>     Stop: zero pivot encountered  
>   For i = k+1 to n:  
>     m_i = Aug[i,k] / Aug[k,k]  
>     For j = k to n+1:  
>       Aug[i,j] = Aug[i,j] - m_i * Aug[k,j]  
      
Then we apply back substitution:  

> x[n] = Aug[n,n+1] / Aug[n,n]  
> For i = n-1 down to 1:  
>   x[i] = (Aug[i,n+1] - Σ Aug[i,j]*x[j]) / Aug[i,i]  

And finally the outputs are printed  


## Method 2 — Gaussian Elimination with Partial Pivoting (PP)  
**Purpose:** Similar to naive gaussian elimination, this method utilises row changes to face the problem that the firts number could be too small compared to the other numbers leading to a not exact answer, also solves the problem of a number in the position [1,1] being a 0  

**Input:**   
- Matrix A (n × n)
- vector b (n × 1)
  
**Output:**  
- Solution vector x  

Check input dimensions:   
  If A is not square → Stop  
  If b size is not compatible → Stop  
  If det(A) = 0 → Stop.   
  
Form augmented matrix Aug = [A | b]

> For k = 1 to n-1:  
>  Find pivot row:  
>  p = index of row i (from k to n) that maximizes |Aug[i,k]|  
> If the number on the new pivot is 0 then:  
>   Stop  
> If p ≠ k:  
>   Swap rows k and p  
> For i = k+1 to n:  
>   m = Aug[i,k] / Aug[k,k]  
> For j = k to n+1:  
>   Aug[i,j] = Aug[i,j] - m * Aug[k,j]  
  
> If the last pivot is 0 then  
>   Stop

Then we apply back substitution:  

> x[n] = Aug[n,n+1] / Aug[n,n]  
> For i = n-1 down to 1:  
>   x[i] = (Aug[i,n+1] - Σ Aug[i,j]*x[j]) / Aug[i,i]  

And finally the outputs are printed  

## Method 3 — Gaussian Elimination with Total Pivoting (TP)  
**Purpose:** find the largest absolute value number in the matrix A and with row and column swapping, you swap it for the current pivot, reducing the risk of dividing by very small numbers and minimizing the propagation of round-off errors, although it increases computational cost and requires tracking column permutations.  

**Input:**   
- Matrix A (n × n)
- vector b (n × 1)
  
**Output:**  
- Solution vector x  

Check input dimensions:   
  If A is not square → Stop  
  If b size is not compatible → Stop  
  If det(A) = 0 → Stop.   
  
Form augmented matrix Aug = [A | b]

Then, initialize a index vector that keeps track of the column swaps
> mark = [1, 2, ..., n]  
  
Find maximum element in submatrix:  
> Find (p, q) such that:  
> |Aug[p,q]| = max |Aug[i,j]| for i,j = k,...,n  

Then do row and column swapping:  
> If p ≠ k:  
> Swap rows p and k  
  
> If q ≠ k:  
> Swap columns q and k  
> Swap mark[q] and mark[k]

> For i = k+1 to n:  
>   m = Aug[i,k] / Aug[k,k]  
> For j = k to n+1:  
>   Aug[i,j] = Aug[i,j] - m * Aug[k,j]  
  
> If the last pivot is 0 then  
>   Stop

Then we apply back substitution:  

> x[n] = Aug[n,n+1] / Aug[n,n]  
> For i = n-1 down to 1:  
>   x[i] = (Aug[i,n+1] - Σ Aug[i,j]*x[j]) / Aug[i,i]
  
Lastly reorder the vector x to match the swaps of columns during the process:  
Create vector x_final such that:  
> x_final[mark[i]] = x[i]

return x_final

## Method 4 — LU with Simple Gaussian Elimination

**Purpose:**This method factors an invertible matrix A into the product:  
- A = LU  
where: L is a lower triangular matrix with ones on its diagonal and U is an upper triangular matrix, The factorization is performed using simple Gaussian elimination without pivoting.

After obtaining L and U, the system is solved by applying forward substitution and back substitution.  

**Inputs**
- Matrix A (n × n)
- Vector b (n × 1)

**Outputs**
- Solution vector x
- Lower triangular matrix L
- Upper triangular matrix U

Check input dimensions:
- If A is not square → Stop
- If dimensions of A and b are not compatible → Stop
- If det(A) = 0 → Stop

Initialize:
- n = size of A
- L = identity matrix of size n
- U = zero matrix of size n × n
- M = A

Store initial stage:
> Stage 0 = M
> For k = 1 to n-1:
>   If M[k,k] = 0 → Stop
> For i = k+1 to n:
>   If M[i,k] ≠ 0:
>     L[i,k] = M[i,k] / M[k,k]  

Perform row elimination:  
> For j = k to n:
>   M[i,j] = M[i,j] - L[i,k] * M[k,j]

Update matrix U:
- Copy the upper triangular part of M into U

Store current stage:
- Save matrices M, L, and U

End loops

> If U[n,n] = 0 → Stop

Apply forward substitution

Apply back substitution

Return the vector x and the stages


## Method 5 — LU Factorization with Partial Pivoting

**Purpose:** This method factors an invertible matrix A into the product:  
- PA = LU  

where:
- P is a permutation matrix
- L is a lower triangular matrix with ones on its diagonal
- U is an upper triangular matrix

The factorization is performed using Gaussian elimination with partial pivoting, improving numerical stability by selecting the largest pivot in each column.

After obtaining P, L and U, the system is solved by applying forward substitution and back substitution.

**Inputs**
- Matrix A (n × n)
- Vector b (n × 1)

**Outputs**
- Solution vector x
- Permutation matrix P
- Lower triangular matrix L
- Upper triangular matrix U

Check input dimensions:
- If A is not square → Stop
- If dimensions of A and b are not compatible → Stop
- If det(A) = 0 → Stop

Initialize:
- n = size of A
- L = identity matrix of size n
- U = zero matrix of size n × n
- P = identity matrix of size n
- M = A

Store initial stage:
> Stage 0 = M

> For k = 1 to n-1:

Find the pivot row:
> p = index of the row with the largest absolute value in column k

If the pivot row is different from k:
> Swap rows k and p in M
> Swap rows k and p in P

If k > 1:
> Swap rows k and p in L only from columns 1 to k-1

If M[k,k] = 0 → Stop

> For i = k+1 to n:

If M[i,k] ≠ 0:
> L[i,k] = M[i,k] / M[k,k]

Perform row elimination:
> For j = k to n:
>   M[i,j] = M[i,j] - L[i,k] * M[k,j]

Update matrix U:
- Copy the upper triangular part of M into U

Store current stage:
- Save matrices M, P, L, and U

End loops

> If U[n,n] = 0 → Stop

Apply forward substitution

Apply back substitution

Return the vector x and the stages

## Method 6 — Crout Factorization

**Purpose:** This method factors an invertible matrix A into the product:  
- A = LU  

where:
- L is a lower triangular matrix
- U is an upper triangular matrix with ones on its diagonal

The factorization is performed directly using the Crout method without Gaussian elimination.

After obtaining L and U, the system is solved by applying forward substitution and back substitution.

**Inputs**
- Matrix A (n × n)
- Vector b (n × 1)

**Outputs**
- Solution vector x
- Lower triangular matrix L
- Upper triangular matrix U

Check input dimensions:
- If A is not square → Stop
- If dimensions of A and b are not compatible → Stop
- If det(A) = 0 → Stop

Initialize:
- n = size of A
- L = identity matrix of size n × n
- U = identity matrix of size n × n

Store initial stage:
> Stage 0 = A

> For i = 1 to n-1:

Compute column i of L:
> For j = i to n:
>   L[j,i] = A[j,i] - dot(L[j,1:i-1], U[1:i-1,i])

If L[i,i] = 0 → Stop

Compute row i of U:
> For j = i+1 to n:
>   U[i,j] = (A[i,j] - dot(L[i,1:i-1], U[1:i-1,j])) / L[i,i]

Store current stage:
- Save matrices L and U

End loops

Compute the last element of L:
> L[n,n] = A[n,n] - dot(L[n,1:n-1], U[1:n-1,n])

Apply forward substitution

Apply back substitution

Return the vector x and the stages

## Method 7 — Doolittle Factorization

**Purpose:** This method factors an invertible matrix A into the product:  
- A = LU  

where:
- L is a lower triangular matrix with ones on its diagonal
- U is an upper triangular matrix

The factorization is performed directly using the Doolittle method without Gaussian elimination.

After obtaining L and U, the system is solved by applying forward substitution and back substitution.

**Inputs**
- Matrix A (n × n)
- Vector b (n × 1)

**Outputs**
- Solution vector x
- Lower triangular matrix L
- Upper triangular matrix U

Check input dimensions:
- If A is not square → Stop
- If dimensions of A and b are not compatible → Stop
- If det(A) = 0 → Stop

Initialize:
- n = size of A
- L = identity matrix of size n × n
- U = identity matrix of size n × n

Store initial stage:
> Stage 0 = A

> For i = 1 to n-1:

Compute row i of U:
> For j = i to n:
>   U[i,j] = A[i,j] - dot(L[i,1:i-1], U[1:i-1,j])

If U[i,i] = 0 → Stop

Compute column i of L:
> For j = i+1 to n:
>   L[j,i] = (A[j,i] - dot(L[j,1:i-1], U[1:i-1,i])) / U[i,i]

Store current stage:
- Save matrices L and U

End loops

Compute the last element of U:
> U[n,n] = A[n,n] - dot(L[n,1:n-1], U[1:n-1,n])

Apply forward substitution

Apply back substitution

Return the vector x and the stages


## Method 9 — Jacobi Method

**Purpose:** This iterative method solves a system of linear equations by computing each variable using only the values from the previous iteration. The process continues until the approximations stabilize within a desired tolerance.

**Inputs:**
A — coefficient matrix
b — independent terms vector
x0 — initial approximation vector
tol — acceptable error
N — maximum number of iterations

**Output:**
Approximation of the solution vector

**BEGIN**

Set the current approximation vector to x0.
Set the initial error to a large number so the loop starts.
Set the iteration counter to zero.

Repeat until the error is smaller than the tolerance or N iterations are reached:

>Create a new empty vector to store the updated approximations.
>
>For each equation in the system:
>
>>Compute the summation of all terms except the diagonal element using the values from the previous iteration.
>>
>>Calculate the new approximation for the current variable.
>>
>Compute the error as the norm or maximum absolute difference between the new vector and the previous approximation.
>
>Replace the old approximation vector with the new one.
>
>Increase the iteration counter by one.
>
>Report the final approximation vector as the solution.

**END**

## Method 10 — Gauss-Seidel Method

**Purpose:** This iterative method solves a system of linear equations by updating each variable sequentially and immediately using the newest available values during the same iteration. This usually allows faster convergence than the Jacobi method.

**Inputs:**
A — coefficient matrix
b — independent terms vector
x0 — initial approximation vector
tol — acceptable error
N — maximum number of iterations

**Output:**
Approximation of the solution vector

**BEGIN**

Set the current approximation vector to x0.
Set the initial error to a large number so the loop starts.
Set the iteration counter to zero.

Repeat until the error is smaller than the tolerance or N iterations are reached:

>Store a copy of the current approximation vector to compare errors later.
>
>For each equation in the system:
>
>>Compute the summation of the terms before the diagonal element using the newest updated values.
>>
>>Compute the summation of the terms after the diagonal element using the values from the previous iteration.
>>
>>Calculate the new approximation for the current variable.
>>
>Compute the error as the norm or maximum absolute difference between the updated vector and the previous approximation.
>
>Increase the iteration counter by one.

Report the final approximation vector as the solution.

**END**

## Method 11 — Successive Over-Relaxation (SOR)

**Purpose:** This iterative method improves the Gauss-Seidel approach by introducing a relaxation factor that can accelerate convergence. Each new approximation is adjusted using both the previous value and the newly computed value.

**Inputs:**
A — coefficient matrix
b — independent terms vector
x0 — initial approximation vector
w — relaxation factor
tol — acceptable error
N — maximum number of iterations

**Output:**
Approximation of the solution vector

**BEGIN**

Set the current approximation vector to x0.
Set the initial error to a large number so the loop starts.
Set the iteration counter to zero.

Repeat until the error is smaller than the tolerance or N iterations are reached:

>Store a copy of the current approximation vector to compare errors later.
>
>For each equation in the system:
>
>>Compute the summation of the terms before the diagonal element using the newest updated values.
>>
>>Compute the summation of the terms after the diagonal element using the values from the previous iteration.
>>
>>Compute the Gauss-Seidel approximation for the current variable.
>>
>>Adjust the approximation using the relaxation factor w.
>
>Compute the error as the norm or maximum absolute difference between the updated vector and the previous approximation.
>
>Increase the iteration counter by one.

Report the final approximation vector as the solution.
