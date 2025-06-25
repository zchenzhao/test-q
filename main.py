# This is a test file.
import unittest


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use helper function with memoization for efficiency
    memo = {}
    return gandalf(n, memo)


def gandalf(n, memo):
    """
    Helper function to calculate Fibonacci numbers recursively with memoization.
    Named after Gandalf from Lord of the Rings.
    
    Args:
        n (int): The position in the Fibonacci sequence
        memo (dict): Memoization dictionary to store already calculated values
        
    Returns:
        int: The nth Fibonacci number
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        result = n
    else:
        result = gandalf(n-1, memo) + gandalf(n-2, memo)
    
    memo[n] = result
    return result


def aragorn(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    Named after Aragorn from Lord of the Rings.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    
    return b


def legolas(n):
    """
    Generate a list of Fibonacci numbers up to the nth position.
    Named after Legolas from Lord of the Rings.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        list: A list of Fibonacci numbers from F(0) to F(n)
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return [0]
    
    result = [0, 1]
    
    for i in range(2, n + 1):
        result.append(result[i-1] + result[i-2])
    
    return result[:n+1]


class FibonacciTest(unittest.TestCase):
    """
    Unit tests for the Fibonacci calculator functions.
    """
    
    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
    
    def test_aragorn_function(self):
        self.assertEqual(aragorn(0), 0)
        self.assertEqual(aragorn(1), 1)
        self.assertEqual(aragorn(2), 1)
        self.assertEqual(aragorn(5), 5)
        self.assertEqual(aragorn(10), 55)
    
    def test_legolas_function(self):
        self.assertEqual(legolas(0), [0])
        self.assertEqual(legolas(1), [0, 1])
        self.assertEqual(legolas(5), [0, 1, 1, 2, 3, 5])
    
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            aragorn(-5)
        with self.assertRaises(ValueError):
            legolas(-3)


def main():
    """
    Main function to run the Fibonacci calculator from the command line.
    """
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <n> [--sequence]")
        print("  n: Calculate the nth Fibonacci number (0-indexed)")
        print("  --sequence: Generate the Fibonacci sequence up to n")
        return
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Please provide a non-negative integer")
            return
        
        if len(sys.argv) > 2 and sys.argv[2] == "--sequence":
            sequence = legolas(n)
            print(f"Fibonacci sequence up to {n}: {sequence}")
        else:
            result = fibonacci(n)
            print(f"Fibonacci({n}) = {result}")
    
    except ValueError:
        print("Please provide a valid integer")


if __name__ == "__main__":
    # Run tests if in test mode
    if len(import_module := __import__('sys').argv) > 1 and import_module.argv[1] == "--test":
        unittest.main(argv=['first-arg-is-ignored'])
    else:
        # Otherwise run the calculator
        main()
