# This is a test file.
# Test cases for the Fibonacci calculator

import unittest
from main import frodo, gandalf


def legolas(test_case):
    """
    Decorator function for test cases.
    """
    def wrapper(*args, **kwargs):
        print(f"Running test: {test_case.__name__}")
        result = test_case(*args, **kwargs)
        print(f"Test {test_case.__name__} completed")
        return result
    return wrapper



class TestFibonacci(unittest.TestCase):
    """
    Test class for Fibonacci calculator functions.
    """
    
    @legolas
    def test_frodo_base_cases(self):
        """Test the base cases for the frodo function."""
        self.assertEqual(frodo(0), 0)
        self.assertEqual(frodo(1), 1)



    @legolas
    def test_frodo_sequence(self):
        """Test the frodo function for known Fibonacci numbers."""
        self.assertEqual(frodo(2), 1)
        self.assertEqual(frodo(3), 2)
        self.assertEqual(frodo(4), 3)
        self.assertEqual(frodo(5), 5)
        self.assertEqual(frodo(6), 8)
        self.assertEqual(frodo(10), 55)



    @legolas
    def test_gandalf_base_cases(self):
        """Test the base cases for the gandalf function."""
        self.assertEqual(gandalf(-1), [])
        self.assertEqual(gandalf(0), [0])
        self.assertEqual(gandalf(1), [0, 1])



    @legolas
    def test_gandalf_sequence(self):
        """Test the gandalf function for generating Fibonacci sequences."""
        self.assertEqual(gandalf(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(gandalf(7), [0, 1, 1, 2, 3, 5, 8, 13])



if __name__ == "__main__":
    unittest.main()