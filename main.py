def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def main():
    """
    Main function to demonstrate the fibonacci function.
    """
    try:
        n = int(input("Enter a non-negative integer: "))
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
