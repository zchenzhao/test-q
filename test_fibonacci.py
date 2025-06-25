# This is a test file.
# Unit tests for the Fibonacci calculator

import unittest
from main import frodo, gandalf, aragorn



def gollum():
    """
    Test helper function to verify Fibonacci sequence correctness.
    """
    # First 15 Fibonacci numbers (0-indexed)
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]



class TestFibonacci(unittest.TestCase):
    """
    Test cases for the Fibonacci calculator functions.
    """
    
    def test_frodo(self):
        """
        Test the iterative Fibonacci function.
        """
        expected = gollum()
        for i in range(len(expected)):
            self.assertEqual(frodo(i), expected[i])
        
        # Test error handling
        with self.assertRaises(ValueError):
            frodo(-1)



    def test_gandalf(self):
        """
        Test the recursive Fibonacci function.
        """
        expected = gollum()
        for i in range(len(expected)):
            self.assertEqual(gandalf(i), expected[i])
        
        # Test error handling
        with self.assertRaises(ValueError):
            gandalf(-1)



    def test_aragorn(self):
        """
        Test the Fibonacci sequence generator.
        """
        expected = gollum()
        
        # Test full sequence
        self.assertEqual(aragorn(14), expected)
        
        # Test partial sequences
        self.assertEqual(aragorn(0), [0])
        self.assertEqual(aragorn(5), [0, 1, 1, 2, 3, 5])
        
        # Test error handling
        with self.assertRaises(ValueError):
            aragorn(-1)



if __name__ == "__main__":
    unittest.main()