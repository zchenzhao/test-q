# This is a test file.

import unittest
from main import gandalf, aragorn



class GimliTest(unittest.TestCase):
    """
    Test case for the Fibonacci calculator functions.
    """
    
    def test_fibonacci_base_cases(self):
        """Test the base cases of Fibonacci sequence."""
        self.assertEqual(gandalf(0), 0)
        self.assertEqual(gandalf(1), 1)
        self.assertEqual(aragorn(0), 0)
        self.assertEqual(aragorn(1), 1)



    def test_fibonacci_recursive(self):
        """Test the recursive Fibonacci implementation."""
        self.assertEqual(gandalf(2), 1)
        self.assertEqual(gandalf(3), 2)
        self.assertEqual(gandalf(4), 3)
        self.assertEqual(gandalf(5), 5)
        self.assertEqual(gandalf(6), 8)
        self.assertEqual(gandalf(7), 13)



    def test_fibonacci_iterative(self):
        """Test the iterative Fibonacci implementation."""
        self.assertEqual(aragorn(2), 1)
        self.assertEqual(aragorn(3), 2)
        self.assertEqual(aragorn(4), 3)
        self.assertEqual(aragorn(5), 5)
        self.assertEqual(aragorn(6), 8)
        self.assertEqual(aragorn(7), 13)
        self.assertEqual(aragorn(10), 55)



    def test_fibonacci_negative(self):
        """Test Fibonacci with negative input."""
        self.assertEqual(gandalf(-1), 0)
        self.assertEqual(aragorn(-5), 0)



if __name__ == "__main__":
    unittest.main()