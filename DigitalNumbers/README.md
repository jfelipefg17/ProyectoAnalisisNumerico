# DigitalNumbers — Numerical Analysis Project
**EAFIT University · Department of Computer Science and Systems**
Course: Numerical Analysis · Instructor: Edwar Samir Posada
Team: Juan Felipe Florez · Jerónimo Mesa · Juan Guillermo Isaza · Luciana Pineda
Repository: https://github.com/jfelipefg17/ProyectoAnalisisNumerico

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Project Structure](#2-project-structure)
3. [Setup — Step by Step](#3-setup--step-by-step)
4. [How to Run Every Test](#4-how-to-run-every-test)
5. [Methods and Test Inputs](#5-methods-and-test-inputs)
6. [How to Add Your Methods](#6-how-to-add-your-methods)
7. [Coding Standards](#7-coding-standards)

---

## 1. Project Overview

DigitalNumbers is a web application that implements the numerical methods studied in class.
The Python code is organized by chapter so each team member works independently without conflicts.

| Chapter | Topic                         | Owner                                                   |
|---------|-------------------------------|---------------------------------------------------------|
| 1       | Single Variable Equations     | Juan Guillermo Isaza · Juan Felipe Florez · Luciana Pineda |
| 2       | Linear Systems                | Jerónimo Mesa Alzate                                    |
| 3       | Open Methods                  | Juan Felipe Florez · Luciana Pineda                     |

---

## 2. Project Structure

```
DigitalNumbers/
│
├── methods/
│   ├── __init__.py
│   ├── chapter1_single_variable/
│   │   ├── __init__.py
│   │   ├── incremental_search.py
│   │   ├── bisection.py
│   │   ├── false_position.py
│   │   ├── newton.py
│   │   ├── fixed_point.py
│   │   ├── secant.py
│   │   └── multiple_roots.py
│   ├── chapter2_linear_systems/
│   │   ├── __init__.py
│   │   ├── naive_gaussian_elimination.py
│   │   ├── gaussian_elimination_PP.py
│   │   └── gaussian_elimination_TP.py
│   └── chapter3_open_methods/
│       └── __init__.py
│
├── tests/
│   ├── print_helpers.py                    ← shared print utilities
│   ├── chapter1_single_variable/
│   │   ├── test_incremental_search.py
│   │   ├── test_bisection.py
│   │   ├── test_false_position.py
│   │   ├── test_newton.py
│   │   ├── test_fixed_point.py
│   │   ├── test_secant.py
│   │   └── test_multiple_roots.py
│   ├── chapter2_linear_systems/
│   │   ├── test_naive_gaussian_elimination.py
│   │   ├── test_gaussian_elimination_PP.py
│   │   └── test_gaussian_elimination_TP.py
│   └── chapter3_open_methods/
│       ├── test_newton.py
│       └── test_fixed_point.py
│
├── pseudocode/
│   └── pseudocode_all_methods.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 3. Setup — Step by Step

### Step 1 — Clone the repository
```bash
git clone https://github.com/jfelipefg17/ProyectoAnalisisNumerico.git
```

### Step 2 — Enter the project folder
```bash
cd ProyectoAnalisisNumerico/DigitalNumbers
```

> ⚠️ **All commands must be run from inside this `DigitalNumbers/` folder.**
> If you run them from another folder, Python will not find the `methods/` package and tests will fail.

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

That installs `numpy` and `pandas`, which are the only libraries needed.

---

## 4. How to Run Every Test

Run each command from inside the `DigitalNumbers/` folder.

### Chapter 1 — Single Variable Equations

```bash
python tests/chapter1_single_variable/test_incremental_search.py
python tests/chapter1_single_variable/test_bisection.py
python tests/chapter1_single_variable/test_false_position.py
python tests/chapter1_single_variable/test_newton.py
python tests/chapter1_single_variable/test_fixed_point.py
python tests/chapter1_single_variable/test_secant.py
python tests/chapter1_single_variable/test_multiple_roots.py
```

### Chapter 2 — Linear Systems

```bash
python tests/chapter2_linear_systems/test_naive_gaussian_elimination.py
python tests/chapter2_linear_systems/test_gaussian_elimination_PP.py
python tests/chapter2_linear_systems/test_gaussian_elimination_TP.py
```

### Chapter 3 — Open Methods

```bash
python tests/chapter3_open_methods/test_newton.py
python tests/chapter3_open_methods/test_fixed_point.py
```

### Run everything at once (Mac/Linux)

```bash
for f in tests/chapter1_single_variable/test_*.py \
          tests/chapter2_linear_systems/test_*.py \
          tests/chapter3_open_methods/test_*.py; do
  echo "--- $f ---"
  python "$f"
done
```

---

## 5. Methods and Test Inputs

All tests use the **exact inputs given by the professor** in *Prueba_métodos_1.pdf*.
`Tol = 1e-7`, `N = 100`, absolute error `Eₙ = |xₙ − xₙ₋₁|`.

### Functions used

```
f(x)   = ln(sin²(x) + 1) − 1/2
f'(x)  = 2·sin(x)·cos(x) / (sin²(x) + 1)
g(x)   = ln(sin²(x) + 1) − 1/2          ← used as x = g(x) for Fixed Point
h(x)   = eˣ − x − 1
h'(x)  = eˣ − 1
h''(x) = eˣ
A = [[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]],  b = [1,1,1,1]
```

### Inputs per method

| Method                  | Inputs                                  | Expected result          |
|-------------------------|-----------------------------------------|--------------------------|
| Incremental Search      | `f`, `x0=-3`, `h=0.5`, `N=100`         | 32 sign-change intervals |
| Bisection               | `f`, `a=0`, `b=1`, `tol=1e-7`, `N=100` | root ≈ 0.9364045262      |
| False Position          | `f`, `a=0`, `b=1`, `tol=1e-7`, `N=100` | root ≈ 0.9364045809      |
| Newton-Raphson          | `f`, `f'`, `x0=0.5`, `tol=1e-7`, `N=100` | root ≈ 0.9364045809   |
| Fixed Point             | `g`, `x0=-0.5`, `tol=1e-7`, `N=100`    | root ≈ −0.3744450530     |
| Secant                  | `f`, `x0=0.5`, `x1=1`, `tol=1e-7`, `N=100` | root ≈ 0.9364045809 |
| Multiple Roots          | `h`, `h'`, `h''`, `x0=1`, `tol=1e-7`, `N=100` | root ≈ 0.0        |
| Naive Gaussian          | `A`, `b`                                | x ≈ [0.038495, −0.180227, −0.309711, 0.247594] |
| Gaussian PP             | `A`, `b`                                | x ≈ [0.038495, −0.180227, −0.309711, 0.247594] |
| Gaussian TP             | `A`, `b`                                | x ≈ [0.038495, −0.180227, −0.309711, 0.247594] |

---

## 6. How to Add Your Methods

### Step 1 — Create your method file

Use this template in `methods/chapterX_your_topic/your_method.py`:

```python
"""
Method Name
===========
One paragraph explaining what the method does.

Author: Your Name
Last updated: April 2026
"""

import pandas as pd


def your_method(param1, param2, tol: float, n_max: int) -> dict:
    """
    Parameters
    ----------
    param1 : type — description
    tol    : float — error tolerance
    n_max  : int   — maximum iterations

    Returns
    -------
    dict with keys:
        'root'      : float
        'iters'     : int
        'error'     : float
        'table'     : pd.DataFrame
        'converged' : bool
    """
    rows = []

    for i in range(1, n_max + 1):
        # ... your computation ...
        rows.append({
            "Iteration": i,
            "x":         round(x, 10),
            "f(x)":      round(fx, 10),
            "error":     round(error, 10),
        })
        if error < tol:
            return {"root": x, "iters": i, "error": error,
                    "table": pd.DataFrame(rows), "converged": True}

    return {"root": x, "iters": n_max, "error": error,
            "table": pd.DataFrame(rows), "converged": False}
```

### Step 2 — Register in `__init__.py`

In `methods/chapterX_your_topic/__init__.py`:
```python
from .your_method import your_method
```

In `methods/__init__.py`:
```python
from .chapterX_your_topic import your_method
```

### Step 3 — Create your test file

```python
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from methods.chapterX_your_topic.your_method import your_method
from tests.print_helpers import print_root_result

f = lambda x: ...
result = your_method(f=f, ...)
print_root_result("Test: f(x) = ...  |  params", result)
```

---

## 7. Coding Standards

- **Language:** English only — comments, docstrings, variable names, print output.
- **One function per file**, same name as the file (`bisection.py` → `def bisection(...)`).
- **Always return a `dict`** — never return plain floats or tuples.
- **No `print()` inside method files** — printing only in test files.
- **No global variables** — everything inside the function.
- **Build the table** with `rows = []` → `pd.DataFrame(rows)`.
- **Round table values** with `round(value, 10)`.
- **Raise `ValueError`** with a clear message for invalid inputs.
- **Use `print_root_result()` or `print_system_result()`** from `tests/print_helpers.py`.
- **Never commit** `venv/`, `__pycache__/`, or `.DS_Store` — they are in `.gitignore`.
