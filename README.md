# This is a test file! :D

# Fibonacci Number Calculator

A simple Python implementation of a Fibonacci number calculator with multiple approaches.

## Features

- Calculate the nth Fibonacci number using recursion
- Calculate the nth Fibonacci number using iteration (more efficient)
- Generate a Fibonacci sequence up to a specified limit
- Interactive command-line interface

## Usage

Run the main script to use the interactive calculator:

```bash
python main.py
```

### As a Module

You can also import the functions in your own code:

```python
from main import gandalf, frodo, aragorn

# Calculate the 10th Fibonacci number using recursion
fib_10_recursive = gandalf(10)  # 55

# Calculate the 10th Fibonacci number using iteration (more efficient)
fib_10_iterative = frodo(10)  # 55

# Generate Fibonacci sequence up to 100
fib_sequence = aragorn(100)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

## Testing

Run the tests to verify the implementation:

```bash
python test_fibonacci.py
```

## Implementation Details

The calculator provides three main functions:

1. `gandalf(n)`: Recursive implementation (educational, but inefficient for large n)
2. `frodo(n)`: Iterative implementation (efficient for any reasonable n)
3. `aragorn(limit)`: Generates a sequence of Fibonacci numbers up to a limit

The interactive interface is provided by the `legolas()` function.