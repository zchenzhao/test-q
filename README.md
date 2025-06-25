# This is a test file.

# Fibonacci Number Calculator

A simple Python application that calculates Fibonacci numbers using both recursive and iterative approaches.

## Features

- Calculate a specific Fibonacci number
- Display a sequence of Fibonacci numbers
- Interactive command-line interface

## Usage

Run the main script:

```bash
python main.py
```

This will start the interactive calculator where you can:
1. Calculate a specific Fibonacci number
2. Display a sequence of Fibonacci numbers
3. Exit the program

## Implementation Details

The calculator provides two different implementations:

1. **Recursive Implementation** (`gandalf` function)
   - Elegant but inefficient for large numbers due to repeated calculations
   - Time complexity: O(2^n)

2. **Iterative Implementation** (`aragorn` function)
   - More efficient approach
   - Time complexity: O(n)
   - Used as the default method for the calculator

## Testing

Run the test suite:

```bash
python test_fibonacci.py
```

The tests verify both implementations against known Fibonacci values.

## Note

For large Fibonacci numbers (n > 35), the recursive implementation may be very slow due to its exponential time complexity. The iterative implementation is recommended for practical use.