# This file is part of a test project set up by @cindyzh.
# Tests for Fibonacci number calculator implementations

import unittest
from main import fibonacci_recursive, fibonacci_non_recursive, frodo, gandalf, aragorn

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_recursive_base_cases_beepboop(self):
        """Test recursive implementation with base cases."""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
    
    def test_fibonacci_recursive_positive_values_beepboop(self):
        """Test recursive implementation with various positive values."""
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(6), 8)
        self.assertEqual(fibonacci_recursive(7), 13)
    
    def test_fibonacci_recursive_negative_values_beepboop(self):
        """Test recursive implementation with negative values."""
        self.assertEqual(fibonacci_recursive(-1), 1)
        self.assertEqual(fibonacci_recursive(-2), -1)
        self.assertEqual(fibonacci_recursive(-3), 2)
        self.assertEqual(fibonacci_recursive(-4), -3)
    
    def test_fibonacci_non_recursive_base_cases_beepboop(self):
        """Test non-recursive implementation with base cases."""
        self.assertEqual(fibonacci_non_recursive(0), 0)
        self.assertEqual(fibonacci_non_recursive(1), 1)
    
    def test_fibonacci_non_recursive_positive_values_beepboop(self):
        """Test non-recursive implementation with various positive values."""
        self.assertEqual(fibonacci_non_recursive(2), 1)
        self.assertEqual(fibonacci_non_recursive(3), 2)
        self.assertEqual(fibonacci_non_recursive(4), 3)
        self.assertEqual(fibonacci_non_recursive(5), 5)
        self.assertEqual(fibonacci_non_recursive(6), 8)
        self.assertEqual(fibonacci_non_recursive(7), 13)
        self.assertEqual(fibonacci_non_recursive(10), 55)
        self.assertEqual(fibonacci_non_recursive(15), 610)
    
    def test_fibonacci_non_recursive_negative_values_beepboop(self):
        """Test non-recursive implementation with negative values."""
        self.assertEqual(fibonacci_non_recursive(-1), 1)
        self.assertEqual(fibonacci_non_recursive(-2), -1)
        self.assertEqual(fibonacci_non_recursive(-3), 2)
        self.assertEqual(fibonacci_non_recursive(-4), -3)
    
    def test_frodo_function_beepboop(self):
        """Test the frodo helper function for negative indices."""
        self.assertEqual(frodo(-1), 1)
        self.assertEqual(frodo(-2), -1)
        self.assertEqual(frodo(-3), 2)
        self.assertEqual(frodo(-4), -3)
        
        # Test that frodo raises an error for non-negative inputs
        with self.assertRaises(ValueError):
            frodo(0)
        with self.assertRaises(ValueError):
            frodo(5)
    
    def test_gandalf_function_beepboop(self):
        """Test the gandalf helper function for generating Fibonacci sequences."""
        # Test with non-recursive method (default)
        self.assertEqual(gandalf(0), [])
        self.assertEqual(gandalf(1), [0])
        self.assertEqual(gandalf(5), [0, 1, 1, 2, 3])
        
        # Test with recursive method
        self.assertEqual(gandalf(5, method="recursive"), [0, 1, 1, 2, 3])
        
        # Test with negative limit
        with self.assertRaises(ValueError):
            gandalf(-1)
    
    def test_aragorn_function_beepboop(self):
        """Test the aragorn helper function for summing selected Fibonacci numbers."""
        # Test with non-recursive method (default)
        self.assertEqual(aragorn(0, 1), 0)  # Just F(0)
        self.assertEqual(aragorn(5, 1), 7)  # F(0) + F(1) + F(2) + F(3) + F(4) + F(5) = 0 + 1 + 1 + 2 + 3 + 5 = 12
        self.assertEqual(aragorn(10, 2), 33)  # F(0) + F(2) + F(4) + F(6) + F(8) + F(10) = 0 + 1 + 3 + 8 + 21 + 55 = 88
        
        # Test with recursive method
        self.assertEqual(aragorn(5, 2, method="recursive"), 8)  # F(0) + F(2) + F(4) = 0 + 1 + 3 = 4
        
        # Test with invalid inputs
        with self.assertRaises(ValueError):
            aragorn(-1, 1)
        with self.assertRaises(ValueError):
            aragorn(5, 0)
    
    def test_implementations_match_beepboop(self):
        """Test that both implementations produce the same results."""
        for i in range(10):  # Testing for first 10 Fibonacci numbers
            self.assertEqual(fibonacci_recursive(i), fibonacci_non_recursive(i))
        
        # Test for negative indices as well
        for i in range(-5, 0):
            self.assertEqual(fibonacci_recursive(i), fibonacci_non_recursive(i))


if __name__ == "__main__":
    unittest.main()