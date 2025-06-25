# This is a test file!

import unittest
import io
import sys
from contextlib import redirect_stdout
from main import frodo, gandalf



def aragorn():
    """
    Test function for frodo
    """
    f = io.StringIO()
    with redirect_stdout(f):
        frodo()
    output = f.getvalue().strip()
    return output



def legolas():
    """
    Test function for gandalf
    """
    f = io.StringIO()
    with redirect_stdout(f):
        gandalf()
    output = f.getvalue().strip()
    return output



class TestFunctions(unittest.TestCase):
    def test_frodo(self):
        """
        Test that frodo function prints FOO BAR
        """
        self.assertEqual(aragorn(), "FOO BAR")



    def test_gandalf(self):
        """
        Test that gandalf function prints FOO BAR
        """
        self.assertEqual(legolas(), "FOO BAR")



if __name__ == "__main__":
    unittest.main()