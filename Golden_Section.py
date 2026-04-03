import numpy as np
import matplotlib.pyplot as plt

# ── Define the objective function ──────────────────────────
def f(x):
    return (x - 2)**2 + 3

# ── Golden Section Search ───────────────────────────────────
def golden_section_search(f, a, b, tol=1e-6):
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi

    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1, f2 = f(x1), f(x2)

    history = [(a, b)]
    iteration = 0

    print(f"{'Iter':>4} {'a':>10} {'b':>10} {'x1':>10} {'x2':>10} {'f(x1)':>12} {'f(x2)':>12} {'Interval':>12}")
    print("-" * 90)

    while abs(b - a) > tol:
        iteration += 1
        print(f"{iteration:>4} {a:>10.6f} {b:>10.6f} {x1:>10.6f} {x2:>10.6f} {f1:>12.6f} {f2:>12.6f} {abs(b-a):>12.8f}")

        if f1 < f2:
            b = x2
            x2, f2 = x1, f1
            x1 = a + resphi * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1, f1 = x2, f2
            x2 = b - resphi * (b - a)
            f2 = f(x2)

        history.append((a, b))

    x_min = (a + b) / 2
    return x_min, f(x_min), history


# ── Function for main.py ─────────────────────────────────────
def run_golden(f_func, a, b):
    x_min, f_min, history = golden_section_search(f_func, a, b)
    return x_min, f_min


# ── Run (only when executed directly) ────────────────────────
if __name__ == "__main__":
    a, b = -5, 10

    print("=" * 90)
    print("  GOLDEN SECTION SEARCH METHOD")
    print(f"  Function : f(x) = (x - 2)² + 3")
    print(f"  Interval : [{a}, {b}]")
    print("=" * 90)

    x_min, f_min, history = golden_section_search(f, a, b)

    print("-" * 90)
    print(f"\n  ✔ Minimum found at  x = {x_min:.8f}")
    print(f"  ✔ Minimum value    f(x) = {f_min:.8f}")
    print(f"  ✔ True minimum at  x = 2.0,  f(2) = 3.0")
    print(f"  ✔ Total iterations: {len(history) - 1}")

    # ── Plot ─────────────────────────────────────────────────────
    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, 'b-', linewidth=2)
    plt.axvline(x=x_min, color='red', linestyle='--')
    plt.scatter([x_min], [f_min], color='red')

    final_a, final_b = history[-1]
    plt.axvspan(final_a, final_b, alpha=0.2, color='green')

    plt.title('Golden Section Search Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()