import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_base_cases(self):
        """Test the base cases of the Fibonacci function."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_small_values(self):
        """Test the Fibonacci function with small values."""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
    
    def test_fibonacci_larger_value(self):
        """Test the Fibonacci function with a larger value."""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)
    
    def test_fibonacci_negative_input(self):
        """Test that the Fibonacci function raises ValueError for negative input."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_fibonacci_non_integer_input(self):
        """Test that the Fibonacci function raises TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            fibonacci(1.5)
        with self.assertRaises(TypeError):
            fibonacci("1")

if __name__ == "__main__":
    unittest.main()