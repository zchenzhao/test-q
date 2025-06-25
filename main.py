# This is a test file.
# Fibonacci Number Calculator

def frodo(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def gandalf(n, memo=None):
    """
    Calculate the nth Fibonacci number using a recursive approach with memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        memo (dict, optional): Memoization dictionary to store previously calculated values
        
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
        
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
        
    if n <= 1:
        return n
        
    memo[n] = gandalf(n-1, memo) + gandalf(n-2, memo)
    return memo[n]



def aragorn(n):
    """
    Generate a list of Fibonacci numbers up to the nth position.
    
    Args:
        n (int): The position in the Fibonacci sequence to generate up to (0-indexed)
        
    Returns:
        list: A list of Fibonacci numbers from F(0) to F(n)
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
        
    result = []
    for i in range(n + 1):
        result.append(frodo(i))
    return result



def legolas():
    """
    Main function to demonstrate the Fibonacci calculator.
    """
    print("Fibonacci Number Calculator")
    print("--------------------------")
    
    # Calculate individual Fibonacci numbers
    print(f"The 10th Fibonacci number (iterative): {frodo(10)}")
    print(f"The 10th Fibonacci number (recursive): {gandalf(10)}")
    
    # Generate Fibonacci sequence
    print("\nFibonacci sequence up to the 10th number:")
    sequence = aragorn(10)
    print(sequence)
    
    # Interactive mode
    try:
        n = int(input("\nEnter a position to calculate its Fibonacci number (0-indexed): "))
        print(f"The {n}th Fibonacci number is: {frodo(n)}")
        
        m = int(input("Enter a position to generate the Fibonacci sequence up to (0-indexed): "))
        print(f"Fibonacci sequence up to position {m}:")
        print(aragorn(m))
    except ValueError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    legolas()
