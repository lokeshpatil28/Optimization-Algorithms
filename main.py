import numpy as np
import math
import matplotlib.pyplot as plt
import os

from Bisection_method import run_bisection
from Golden_Section import run_golden
from Fiibonacci_method import run_fibonacci
from Steepest_Ascent import run_steepest

# ── Safe evaluation dictionary ──────────────────────────────
safe_dict = {
    "x": 0,
    "y": 0,
    "np": np,
    "math": math,
    "sin": math.sin,
    "cos": math.cos,
    "exp": math.exp,
    "log": math.log,
    "sqrt": math.sqrt
}

# ── Plotting Functions ───────────────────────────────
def plot_1d_function(f, x_opt, title):
    x_vals = np.linspace(x_opt - 5, x_opt + 5, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axvline(x=x_opt, color='red', linestyle='--', label=f'x = {x_opt:.3f}')
    plt.scatter([x_opt], [f(x_opt)], color='red')

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)

    # 📁 Create outputs folder if not exists
    os.makedirs("outputs", exist_ok=True)

    filename = title.replace(" ", "_") + ".png"
    filepath = os.path.join("outputs", filename)

    plt.savefig(filepath)
    print(f"Graph saved in 'outputs/' folder as: {filename}")

    plt.show()

def plot_2d_function(f, x_opt, y_opt):
    x = np.linspace(x_opt - 5, x_opt + 5, 100)
    y = np.linspace(y_opt - 5, y_opt + 5, 100)
    X, Y = np.meshgrid(x, y)

    Z = np.vectorize(f)(X, Y)

    plt.figure(figsize=(6, 5))
    plt.contourf(X, Y, Z, levels=30, cmap='viridis')
    plt.colorbar()

    plt.scatter(x_opt, y_opt, color='red', label="Optimum")
    plt.title("Steepest Ascent Result")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    # 📁 Create outputs folder if not exists
    os.makedirs("outputs", exist_ok=True)

    filename = "Steepest_Ascent_Result.png"
    filepath = os.path.join("outputs", filename)

    plt.savefig(filepath)
    print(f"Graph saved in 'outputs/' folder as: {filename}")

    plt.show()

# ── Numerical Derivative (1D) ───────────────────────────────
def numerical_derivative(f, h=1e-5):
    def df(x):
        return (f(x + h) - f(x - h)) / (2*h)
    return df

# ── Numerical Gradient (2D) ─────────────────────────────────
def numerical_gradient(f, h=1e-5):
    def grad(x, y):
        dfdx = (f(x + h, y) - f(x - h, y)) / (2*h)
        dfdy = (f(x, y + h) - f(x, y - h)) / (2*h)
        return np.array([dfdx, dfdy])
    return grad

# ── Utility Functions ───────────────────────────────────────
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input. Please enter a number.")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input. Please enter an integer.")

# ── Function Inputs ─────────────────────────────────────────
def get_function_1d():
    while True:
        expr = input("Enter function f(x): ")
        try:
            safe_dict["x"] = 1
            eval(expr, {"__builtins__": None}, safe_dict)
        except:
            print("Invalid function. Try again (use ** for powers).")
            continue

        def f(x):
            safe_dict["x"] = x
            return eval(expr, {"__builtins__": None}, safe_dict)

        return f

def get_function_2d():
    while True:
        expr = input("Enter function f(x,y): ")
        try:
            safe_dict["x"], safe_dict["y"] = 1, 1
            eval(expr, {"__builtins__": None}, safe_dict)
        except:
            print("Invalid function. Try again.")
            continue

        def f(x, y):
            safe_dict["x"] = x
            safe_dict["y"] = y
            return eval(expr, {"__builtins__": None}, safe_dict)

        return f

# ── Menu ────────────────────────────────────────────────────
def menu():
    print("\n========== MENU ==========")
    print("1. Bisection Method")
    print("2. Golden Section Method")
    print("3. Fibonacci Method")
    print("4. Steepest Ascent Method")
    print("5. Run All Methods")
    print("==========================")

    while True:
        choice = get_valid_int("Enter choice (1-5): ")
        if 1 <= choice <= 5:
            return choice
        print("Invalid choice. Try again.")

# ── MAIN ────────────────────────────────────────────────────
def main():
    choice = menu()

    # COMMON INPUT (for Run All)
    if choice == 5:
        print("\n===== COMMON INPUT (1D) =====")
        f_common = get_function_1d()

    # ── Bisection ──
    if choice in [1, 5]:
        print("\n===== BISECTION INPUT =====")
        f = f_common if choice == 5 else get_function_1d()
        df = numerical_derivative(f)

        print("Using numerical differentiation for derivative")

        a = get_valid_float("Enter a: ")
        b = get_valid_float("Enter b: ")

        try:
            root, val = run_bisection(df, a, b)
            print(f"Stationary point → x = {root:.6f}")
            plot_1d_function(f, root, "Bisection Method")
        except Exception as e:
            print("Error:", e)

    # ── Golden Section ──
    if choice in [2, 5]:
        print("\n===== GOLDEN SECTION INPUT =====")
        f = f_common if choice == 5 else get_function_1d()

        a = get_valid_float("Enter a: ")
        b = get_valid_float("Enter b: ")

        try:
            x, val = run_golden(f, a, b)
            print(f"Minimum → x = {x:.6f}, f(x) = {val:.6f}")
            plot_1d_function(f, x, "Golden Section Method")
        except Exception as e:
            print("Error:", e)

    # ── Fibonacci ──
    if choice in [3, 5]:
        print("\n===== FIBONACCI INPUT =====")
        f = f_common if choice == 5 else get_function_1d()

        a = get_valid_float("Enter a: ")
        b = get_valid_float("Enter b: ")
        n = get_valid_int("Enter number of iterations: ")

        try:
            x, val = run_fibonacci(f, a, b, n)
            print(f"Minimum → x = {x:.6f}, f(x) = {val:.6f}")
            plot_1d_function(f, x, "Fibonacci Method")
        except Exception as e:
            print("Error:", e)

    # ── Steepest Ascent ──
    if choice in [4, 5]:
        print("\n===== STEEPEST ASCENT INPUT =====")
        f2d = get_function_2d()
        grad = numerical_gradient(f2d)

        print("Using numerical gradient for optimization")

        x0 = get_valid_float("Enter x0: ")
        y0 = get_valid_float("Enter y0: ")
        alpha = get_valid_float("Enter learning rate: ")

        try:
            x, y, val = run_steepest(f2d, grad, x0, y0, alpha)
            print(f"Maximum → ({x:.6f}, {y:.6f}), f = {val:.6f}")
            plot_2d_function(f2d, x, y)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()