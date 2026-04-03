# Optimization Methods Project

## Overview

This project implements four optimization techniques:

* Bisection Method
* Golden Section Method
* Fibonacci Method
* Steepest Ascent Method

The system allows the user to input custom mathematical functions and automatically computes derivatives and gradients using numerical differentiation. It also provides graphical visualization and saves outputs.

---

## Project Structure

The project folder contains:

* `main.py` → Python script version (terminal-based)
* `optimization_methods.ipynb` → Jupyter Notebook version (preferred for submission)
* `Bisection_method.py`
* `Golden_Section.py`
* `Fiibonacci_method.py`
* `Steepest_Ascent.py`
* `outputs/` → folder where graphs are saved

---

## How to Run

### ▶️ Option 1: Run using Python script

```id="run1"
python main.py
```

---

### ▶️ Option 2: Run using Jupyter Notebook (Recommended)

```id="run2"
jupyter notebook
```

Then:

* Open `optimization_methods.ipynb`
* Click **Run All Cells**

---

## Features

* User-defined functions
* Automatic derivative computation (numerical differentiation)
* Automatic gradient computation for 2D optimization
* Menu-driven interface
* Input validation and error handling
* Graphical visualization using matplotlib
* Automatic saving of graphs in `outputs/` folder
* Modular and reusable code

---

## Graph Output

For each method:

* A graph is displayed
* The graph is automatically saved in the `outputs/` folder

### Example saved files:

* `outputs/Bisection_Method.png`
* `outputs/Golden_Section_Method.png`
* `outputs/Fibonacci_Method.png`
* `outputs/Steepest_Ascent_Result.png`

---

## Methods Implemented

### 1. Bisection Method

Finds stationary points by solving f'(x) = 0 using interval halving.

### 2. Golden Section Method

Minimizes a function using the golden ratio for efficient interval reduction.

### 3. Fibonacci Method

Uses Fibonacci numbers to iteratively narrow down the search interval.

### 4. Steepest Ascent Method

Maximizes a function using gradient-based optimization.

---

## Example Runs (Recommended Test Cases)

### Example 1: Bisection Method

Input:

```id="ex1"
Choice: 1
Enter function f(x): x**3 - 6*x**2 + 9*x + 1
Enter a: 2
Enter b: 4
```

Expected Output:

```id="out1"
Stationary point → x ≈ 3.000000
```

---

### Example 2: Golden Section

Input:

```id="ex2"
Choice: 2
Enter function f(x): (x-2)**2 + 3
Enter a: -5
Enter b: 10
```

---

### Example 3: Fibonacci Method

Input:

```id="ex3"
Choice: 3
Enter function f(x): x**2 + 10*sin(x)
Enter a: 0
Enter b: 6
Enter number of iterations: 15
```

---

### Example 4: Exponential Optimization

Input:

```id="ex4"
Choice: 2
Enter function f(x): exp(x) - 4*x
Enter a: 0
Enter b: 3
```

---

### Example 5: Steepest Ascent (Basic)

Input:

```id="ex5"
Choice: 4
Enter function f(x,y): -(x**2 + y**2)
Enter x0: 2
Enter y0: -3
Enter learning rate: 0.1
```

---

### Example 6: Steepest Ascent (Shifted)

Input:

```id="ex6"
Choice: 4
Enter function f(x,y): -(x-2)**2 - (y-3)**2 + 5
Enter x0: 0
Enter y0: 0
Enter learning rate: 0.1
```

---

### Example 7: Run All Methods

Input:

```id="ex7"
Choice: 5
Enter function f(x): (x-2)**2
Enter a: 0
Enter b: 5
Enter number of iterations: 15
Enter function f(x,y): -(x**2 + y**2)
Enter x0: 1
Enter y0: 1
Enter learning rate: 0.1
```

---

## Input Format

* Use Python syntax
* Use `**` for powers

Correct:

```id="fmt1"
(x-2)**2
sin(x) + x**2
```

Incorrect:

```id="fmt2"
x^2
```

---

## Limitations

* Numerical differentiation introduces small approximation errors
* Requires valid mathematical expressions as input
* Works best for unimodal functions in 1D optimization

---

## Author

LOKESH PATIL, 
AKSHAT GUPTA, 
P. S. KASHYAP. 

