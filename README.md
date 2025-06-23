# This file is part of a test project set up by @cindyzh.

# Fibonacci Number Calculator

This repository contains implementations of a Fibonacci number calculator with both recursive and non-recursive (iterative) approaches.

## Features

- Calculate Fibonacci numbers using recursive or non-recursive methods
- Support for negative indices using the formula: F(-n) = (-1)^(n+1) * F(n)
- Helper functions for generating sequences and calculating sums

## Functions

### Main Functions

- `fibonacci_recursive(n)`: Calculate the nth Fibonacci number using recursion
- `fibonacci_non_recursive(n)`: Calculate the nth Fibonacci number using iteration

### Helper Functions

- `frodo(n)`: Handle negative indices for Fibonacci calculations
- `gandalf(limit, method)`: Generate a list of Fibonacci numbers up to a limit
- `aragorn(n, k, method)`: Calculate the sum of every kth Fibonacci number up to the nth number

## Usage Examples

```python
from main import fibonacci_recursive, fibonacci_non_recursive, gandalf, aragorn

# Calculate the 10th Fibonacci number (0-indexed)
print(fibonacci_recursive(10))  # Output: 55
print(fibonacci_non_recursive(10))  # Output: 55

# Generate the first 10 Fibonacci numbers
print(gandalf(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Sum every 2nd Fibonacci number up to the 10th
print(aragorn(10, 2))  # Output: 88 (0 + 1 + 3 + 8 + 21 + 55)
```

## Testing

Run the tests using:

```bash
python -m unittest test_fibonacci.py
```

## Performance Considerations

The recursive implementation is simple but inefficient for large values of n due to repeated calculations. For large values, the non-recursive implementation is recommended.