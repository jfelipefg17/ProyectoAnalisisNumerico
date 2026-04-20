"""
Shared print utilities for all test files.
==========================================
Formatting standards applied everywhere:
  - x values          : 10 decimal places  (%.10f)
  - f(x), g(x) values : scientific notation, 4 decimal places  (%.4e)
  - Error E           : scientific notation, 4 decimal places  (%.4e)
  - iter              : integer
  - First-row E       : blank (no error on initial guess)

Do not modify — imported by every test script.
"""

import pandas as pd


# ── Column format registry ─────────────────────────────────────────────────
# Any column whose name matches a key is formatted with that spec.
# Matching is case-sensitive and checked by exact name or prefix.

_SCI_COLS  = {"f(xi)", "f(xm)", "f(xi+1)", "f(x)", "f(xi)", "g(xi)",
              "f(xi)", "E", "f(xm)"}   # scientific notation
_FLOAT_COLS = {"xi", "xm", "a", "b", "xi+1", "g(xi)"}  # 10 decimal places


def _fmt(col: str, val) -> str:
    """Format a single cell value according to column name."""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return ""
    if col == "iter":
        return f"{int(val)}"
    # Scientific notation columns
    if col in ("f(xi)", "f(xm)", "f(xi+1)", "E", "f(xi)"):
        return f"{val:.4e}"
    # 10-decimal float columns
    if col in ("xi", "xm", "a", "b", "xi+1", "g(xi)"):
        return f"{val:.10f}"
    # fallback
    try:
        return f"{val:.10f}"
    except (TypeError, ValueError):
        return str(val)


def _print_table(df: pd.DataFrame) -> None:
    """Print a DataFrame with unified column formatting."""
    cols = list(df.columns)

    # Build formatted rows
    formatted = []
    for _, row in df.iterrows():
        formatted.append([_fmt(c, row[c]) for c in cols])

    # Compute column widths
    widths = [len(c) for c in cols]
    for frow in formatted:
        for j, cell in enumerate(frow):
            widths[j] = max(widths[j], len(cell))

    # Header
    header = "  ".join(c.rjust(widths[j]) for j, c in enumerate(cols))
    sep    = "  ".join("-" * w for w in widths)
    print(header)
    print(sep)
    for frow in formatted:
        print("  ".join(cell.rjust(widths[j]) for j, cell in enumerate(frow)))


# ── Public helpers ─────────────────────────────────────────────────────────

def print_search_result(label: str, result: dict) -> None:
    """
    Print table and summary for incremental_search.
    Reports every interval found.
    """
    print(f"\n{'='*65}")
    print(f"  {label}")
    print(f"{'='*65}\n")
    _print_table(result["table"])
    print(f"\n  Steps performed : {result['iters']}")
    if result["found"]:
        print(f"  Intervals found : {len(result['intervals'])}")
        for a, b in result["intervals"]:
            print(f"    f has a root in [{a:.10f}, {b:.10f}]")
    else:
        print("  No sign change found — try smaller h or a different x0.")
    print()


def print_root_result(label: str, result: dict) -> None:
    """
    Print table and summary for bisection, false_position, newton,
    fixed_point, secant, and multiple_roots.
    """
    print(f"\n{'='*65}")
    print(f"  {label}")
    print(f"{'='*65}\n")
    _print_table(result["table"])
    print(f"\n  Iterations : {result['iters']}")
    print(f"  Root       : {result['root']:.10f}")
    print(f"  Error      : {result['error']:.4e}")
    print(f"  Status     : {'Converged ✓' if result['converged'] else 'Max iterations reached'}")
    print()


def print_system_result(label: str, x, stages) -> None:
    """
    Print elimination stages and solution vector for linear system methods.
    """
    print(f"\n{'='*65}")
    print(f"  {label}")
    print(f"{'='*65}")
    for i, stage in enumerate(stages):
        print(f"\n  Stage {i}:")
        for row in stage:
            print("  " + "  ".join(f"{v:12.6f}" for v in row))
    print(f"\n  Solution x:")
    for i, xi in enumerate(x):
        print(f"    x[{i}] = {xi:.10f}")
    print()
