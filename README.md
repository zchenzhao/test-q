# Fibonacci Number Calculator

This is a simple Fibonacci number calculator that provides functions to:
1. Calculate the nth Fibonacci number
2. Generate a sequence of Fibonacci numbers up to the nth position

## Usage

### Running the Calculator

```bash
python main.py
```

This will start an interactive prompt where you can enter a position (n) to calculate the corresponding Fibonacci number.

### Using the Functions in Your Code

```python
from main import frodo, gandalf

# Calculate the 10th Fibonacci number
fib_10 = frodo(10)  # Returns 55

# Generate Fibonacci sequence up to position 10
fib_sequence = gandalf(10)  # Returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

## Running Tests

```bash
python test_fibonacci.py
```

## Fibonacci Sequence

The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...