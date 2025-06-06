"""
Fibonacci Number Calculator

This module provides functions to calculate Fibonacci numbers.
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    This is the recommended function for calculating Fibonacci numbers
    as it is more efficient than the recursive approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
                 where F(0) = 0, F(1) = 1, F(2) = 1, etc.
    
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n <= 1:
        return n
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.
    
    Note: This implementation is not recommended for large values of n
    due to its exponential time complexity and potential for stack overflow.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
                 where F(0) = 0, F(1) = 1, F(2) = 1, etc.
    
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def test_fibonacci():
    """Test the fibonacci functions with known values."""
    # Test cases for the iterative implementation
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    
    # Test cases for the recursive implementation
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(6) == 8
    
    # Test error handling
    try:
        fibonacci(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
        
    try:
        fibonacci_recursive(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_fibonacci()
    
    # Example usage
    print("\nFibonacci Sequence (first 10 numbers):")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
    
    # Performance comparison example
    import time
    
    print("\nPerformance comparison:")
    n = 30
    
    # Measure time for iterative approach
    start = time.time()
    result_iterative = fibonacci(n)
    end = time.time()
    print(f"Iterative approach for F({n}): {result_iterative}, Time: {end - start:.6f} seconds")
    
    # Measure time for recursive approach (only for small n)
    if n <= 30:  # Limit to avoid long execution time
        start = time.time()
        result_recursive = fibonacci_recursive(n)
        end = time.time()
        print(f"Recursive approach for F({n}): {result_recursive}, Time: {end - start:.6f} seconds")
    else:
        print(f"Recursive approach for F({n}): skipped (too large for efficient recursive calculation)")
