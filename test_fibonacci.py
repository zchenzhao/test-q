"""
Test module for the Fibonacci calculator functions.
"""

import unittest
from main import fibonacci, fibonacci_recursive

class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci functions."""
    
    def test_fibonacci_base_cases(self):
        """Test the base cases for the iterative Fibonacci function."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_sequence(self):
        """Test several values in the Fibonacci sequence."""
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, expected in enumerate(expected_values):
            self.assertEqual(fibonacci(n), expected)
    
    def test_fibonacci_recursive_base_cases(self):
        """Test the base cases for the recursive Fibonacci function."""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
    
    def test_fibonacci_recursive_sequence(self):
        """Test several values in the Fibonacci sequence using recursive function."""
        # We'll use a smaller range for the recursive function to avoid long test times
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        for n, expected in enumerate(expected_values):
            self.assertEqual(fibonacci_recursive(n), expected)
    
    def test_negative_input(self):
        """Test that negative inputs raise ValueError."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
    
    def test_large_input(self):
        """Test the iterative function with a larger input."""
        # F(50) = 12586269025
        self.assertEqual(fibonacci(50), 12586269025)


if __name__ == "__main__":
    unittest.main()