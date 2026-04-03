import numpy as np
import matplotlib.pyplot as plt

# ── Define the objective function and its derivative ────────
def f(x):
    return x**3 - 6*x**2 + 9*x + 1

def df(x):
    return 3*x**2 - 12*x + 9

# ── Bisection Method ─────────────────────────────────────────
def bisection_method(df, a, b, tol=1e-6):
    if df(a) * df(b) > 0:
        raise ValueError("df(a) and df(b) must have opposite signs!")

    history = []
    iteration = 0

    print(f"{'Iter':>4} {'a':>10} {'b':>10} {'midpoint':>12} {'f(mid)':>12} {'df(mid)':>12} {'|b-a|':>12}")
    print("-" * 82)

    while abs(b - a) > tol:
        iteration += 1
        mid = (a + b) / 2
        f_mid = f(mid)
        df_mid = df(mid)
        history.append(mid)

        print(f"{iteration:>4} {a:>10.6f} {b:>10.6f} {mid:>12.8f} {f_mid:>12.6f} {df_mid:>12.8f} {abs(b-a):>12.8f}")

        if df_mid == 0:
            break
        elif df(a) * df_mid < 0:
            b = mid
        else:
            a = mid

    root = (a + b) / 2
    return root, f(root), history


# ── Function for main.py ─────────────────────────────────────
def run_bisection(df_func, a, b):
    root, f_root, history = bisection_method(df_func, a, b)
    return root, f_root


# ── Run (only when executed directly) ────────────────────────
if __name__ == "__main__":
    a, b = 2.0, 4.0

    print("=" * 82)
    print("  BISECTION METHOD")
    print(f"  Function   : f(x) = x³ - 6x² + 9x + 1")
    print(f"  Derivative : f'(x) = 3x² - 12x + 9")
    print(f"  Interval   : [{a}, {b}]  (searching for root of f')")
    print("=" * 82)

    root, f_root, history = bisection_method(df, a, b)

    print("-" * 82)
    print(f"\n  ✔ Root of f'(x) found at  x = {root:.8f}")
    print(f"  ✔ f(x) at minimum        = {f_root:.8f}")
    print(f"  ✔ True minimum at        x = 3.0,  f(3) = 1.0")
    print(f"  ✔ Total iterations: {len(history)}")

    # ── Plot ─────────────────────────────────────────
    x_vals = np.linspace(0, 5, 400)
    y_vals = f(x_vals)
    dy_vals = df(x_vals)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(x_vals, y_vals, 'b-', linewidth=2)
    axes[0].axvline(x=root, color='red', linestyle='--')
    axes[0].scatter([root], [f_root], color='red')

    axes[1].plot(x_vals, dy_vals, 'g-', linewidth=2)
    axes[1].axhline(y=0, color='black')

    plt.suptitle('Bisection Method')
    plt.tight_layout()
    plt.show()