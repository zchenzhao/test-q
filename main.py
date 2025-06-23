# This file is part of a test project set up by @cindyzh.
# Fibonacci number calculator implementation with both recursive and non-recursive approaches

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    # Base cases
    if n < 0:
        return frodo(n)
    if n <= 1:
        return n
        
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_non_recursive(n):
    """
    Calculate the nth Fibonacci number using iteration (non-recursive).
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    # Handle negative inputs
    if n < 0:
        return frodo(n)
    
    # Base cases
    if n <= 1:
        return n
        
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    
    # Iterate to find the nth number
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b


def frodo(n):
    """
    Helper function to handle negative inputs for Fibonacci calculations.
    Named after Frodo Baggins from Lord of the Rings.
    
    For negative indices, we use the formula: F(-n) = (-1)^(n+1) * F(n)
    
    Args:
        n (int): A negative integer
        
    Returns:
        int: The corresponding Fibonacci number for negative index
    """
    if n >= 0:
        raise ValueError("This function is only for negative inputs")
    
    # Calculate the positive counterpart
    positive_n = abs(n)
    result = fibonacci_non_recursive(positive_n)
    
    # Apply the formula for negative indices
    if positive_n % 2 == 0:
        return -result
    else:
        return result


def gandalf(limit, method="non_recursive"):
    """
    Generate a list of Fibonacci numbers up to a limit.
    Named after Gandalf from Lord of the Rings.
    
    Args:
        limit (int): The maximum number of Fibonacci numbers to generate
        method (str): The calculation method - "recursive" or "non_recursive"
        
    Returns:
        list: A list of Fibonacci numbers
    """
    if limit < 0:
        raise ValueError("Limit must be non-negative")
    
    result = []
    for i in range(limit):
        if method == "recursive":
            result.append(fibonacci_recursive(i))
        else:
            result.append(fibonacci_non_recursive(i))
    
    return result


def aragorn(n, k, method="non_recursive"):
    """
    Calculate the sum of every kth Fibonacci number up to the nth number.
    Named after Aragorn from Lord of the Rings.
    
    Args:
        n (int): The position in the Fibonacci sequence to calculate up to
        k (int): Take every kth number
        method (str): The calculation method - "recursive" or "non_recursive"
        
    Returns:
        int: The sum of selected Fibonacci numbers
    """
    if n < 0 or k <= 0:
        raise ValueError("n must be non-negative and k must be positive")
    
    total = 0
    for i in range(0, n + 1, k):
        if method == "recursive":
            total += fibonacci_recursive(i)
        else:
            total += fibonacci_non_recursive(i)
    
    return total
