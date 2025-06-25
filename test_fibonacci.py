# This is a test file! :D
import unittest
from main import gandalf, aragorn


class TestFibonacci(unittest.TestCase):
    """Test cases for the Fibonacci calculator functions."""
    
    def test_gimli_recursive(self):
        """Test the recursive Fibonacci implementation with known values."""
        self.assertEqual(gandalf(0), 0)
        self.assertEqual(gandalf(1), 1)
        self.assertEqual(gandalf(2), 1)
        self.assertEqual(gandalf(3), 2)
        self.assertEqual(gandalf(5), 5)
        self.assertEqual(gandalf(10), 55)



    def test_boromir_iterative(self):
        """Test the iterative Fibonacci implementation with known values."""
        self.assertEqual(aragorn(0), 0)
        self.assertEqual(aragorn(1), 1)
        self.assertEqual(aragorn(2), 1)
        self.assertEqual(aragorn(3), 2)
        self.assertEqual(aragorn(5), 5)
        self.assertEqual(aragorn(10), 55)
        self.assertEqual(aragorn(20), 6765)



    def test_samwise_edge_cases(self):
        """Test edge cases for both implementations."""
        # Negative input
        self.assertEqual(gandalf(-1), 0)
        self.assertEqual(aragorn(-5), 0)
        
        # Large number (only testing iterative to avoid long test time)
        self.assertEqual(aragorn(30), 832040)



if __name__ == "__main__":
    unittest.main()