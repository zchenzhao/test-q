# This file is part of a test project set up by @cindyzh.
# Example usage of the Fibonacci calculator

from main import fibonacci_recursive, fibonacci_non_recursive, gandalf, aragorn

def legolas(n):
    """
    Compare the performance of recursive and non-recursive Fibonacci implementations.
    Named after Legolas from Lord of the Rings.
    
    Args:
        n (int): The position in the Fibonacci sequence to calculate
    """
    print(f"Calculating F({n}) using both methods:")
    
    # Using recursive method
    result_recursive = fibonacci_recursive(n)
    print(f"  Recursive result: {result_recursive}")
    
    # Using non-recursive method
    result_non_recursive = fibonacci_non_recursive(n)
    print(f"  Non-recursive result: {result_non_recursive}")
    
    # Verify they match
    print(f"  Results match: {result_recursive == result_non_recursive}")


def main():
    print("Fibonacci Calculator Examples\n")
    
    # Example 1: Calculate specific Fibonacci numbers
    print("Example 1: Calculate specific Fibonacci numbers")
    for i in range(10):
        print(f"F({i}) = {fibonacci_non_recursive(i)}")
    print()
    
    # Example 2: Negative indices
    print("Example 2: Negative indices")
    for i in range(-5, 0):
        print(f"F({i}) = {fibonacci_non_recursive(i)}")
    print()
    
    # Example 3: Generate a sequence
    print("Example 3: Generate a sequence of Fibonacci numbers")
    sequence = gandalf(10)
    print(f"First 10 Fibonacci numbers: {sequence}")
    print()
    
    # Example 4: Sum of every kth number
    print("Example 4: Sum of every kth Fibonacci number")
    sum_every_2nd = aragorn(10, 2)
    print(f"Sum of every 2nd Fibonacci number up to F(10): {sum_every_2nd}")
    print()
    
    # Example 5: Compare implementations
    print("Example 5: Compare implementations")
    legolas(15)
    print()
    
    # Note: For large values, the recursive implementation will be very slow
    print("Note: For n > 30, the recursive implementation becomes very slow")
    print("Try fibonacci_non_recursive(100) for large values")


if __name__ == "__main__":
    main()