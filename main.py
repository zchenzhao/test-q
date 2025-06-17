def print_foobar():
    """
    Function that prints the string 'foobar'
    """
    print("foobar")

def display_foobar():
    """
    Another function that prints the string 'foobar'
    """
    print("foobar")

def test_foobar_functions():
    """
    Test function to verify that both foobar functions work correctly
    """
    import io
    import sys
    
    # Capture stdout to verify output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test print_foobar
    print_foobar()
    assert captured_output.getvalue().strip() == "foobar"
    
    # Reset captured output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test display_foobar
    display_foobar()
    assert captured_output.getvalue().strip() == "foobar"
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    print("All tests passed!")

if __name__ == "__main__":
    # Demonstrate the functions
    print("Calling print_foobar():")
    print_foobar()
    
    print("\nCalling display_foobar():")
    display_foobar()
    
    # Run tests
    print("\nRunning tests:")
    test_foobar_functions()
