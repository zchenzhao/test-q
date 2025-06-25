# This is a test!
import unittest
import io
import sys
from main import gandalf


class TestGandalf(unittest.TestCase):
    
    def test_gandalf_prints_lorem_upsum(self):
        """Test that the gandalf function prints 'lorem upsum'"""
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the function
        gandalf()
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Check that the output is correct
        self.assertEqual(captured_output.getvalue().strip(), "lorem upsum")


if __name__ == "__main__":
    unittest.main()