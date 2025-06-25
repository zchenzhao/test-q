# This is a test file! :D

import unittest
from main import gandalf, frodo, aragorn



def gollum():
    """
    Helper function to verify Fibonacci sequence correctness.
    First few Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]



class TestFibonacci(unittest.TestCase):
    
    def test_gandalf_recursive(self):
        """Test the recursive Fibonacci implementation."""
        fib_sequence = gollum()
        for i in range(10):  # Testing up to the 10th Fibonacci number
            self.assertEqual(gandalf(i), fib_sequence[i])



    def test_frodo_iterative(self):
        """Test the iterative Fibonacci implementation."""
        fib_sequence = gollum()
        for i in range(13):  # Testing up to the 13th Fibonacci number
            self.assertEqual(frodo(i), fib_sequence[i])



    def test_aragorn_sequence(self):
        """Test the Fibonacci sequence generator."""
        # Test with limit 50 (should include 0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
        sequence = aragorn(50)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(sequence, expected)
        
        # Test with limit 100 (should include numbers up to 89)
        sequence = aragorn(100)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(sequence, expected)



    def test_edge_cases(self):
        """Test edge cases for Fibonacci functions."""
        # Test negative input
        self.assertEqual(gandalf(-1), 0)
        self.assertEqual(frodo(-5), 0)
        
        # Test zero
        self.assertEqual(gandalf(0), 0)
        self.assertEqual(frodo(0), 0)
        
        # Test first Fibonacci number
        self.assertEqual(gandalf(1), 1)
        self.assertEqual(frodo(1), 1)



if __name__ == "__main__":
    unittest.main()