# This is a test file.
# Demo script for the Fibonacci calculator

from main import frodo, gandalf


def gimli():
    """
    Function to demonstrate the Fibonacci calculator with examples.
    """
    print("Fibonacci Calculator Demo")
    print("========================")
    
    # Example 1: Calculate specific Fibonacci numbers
    print("\nExample 1: Calculate specific Fibonacci numbers")
    for i in range(11):
        print(f"F({i}) = {frodo(i)}")
    
    # Example 2: Generate Fibonacci sequences
    print("\nExample 2: Generate Fibonacci sequences")
    print(f"Fibonacci sequence up to position 10: {gandalf(10)}")
    
    print("\nDemo completed!")



if __name__ == "__main__":
    gimli()