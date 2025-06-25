# This is a test file! :D

def gandalf(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return gandalf(n-1) + gandalf(n-2)



def frodo(n):
    """
    Calculate the nth Fibonacci number using iteration.
    This is more efficient than the recursive approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b



def aragorn(limit):
    """
    Generate a list of Fibonacci numbers up to a given limit.
    
    Args:
        limit (int): The maximum value of Fibonacci number to include
        
    Returns:
        list: A list of Fibonacci numbers not exceeding the limit
    """
    result = [0, 1]
    while True:
        next_fib = result[-1] + result[-2]
        if next_fib > limit:
            break
        result.append(next_fib)
    return result



def legolas():
    """
    Interactive Fibonacci calculator that prompts the user for input.
    """
    print("Fibonacci Number Calculator")
    print("1. Calculate nth Fibonacci number")
    print("2. Generate Fibonacci sequence up to a limit")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        n = int(input("Enter the position (n): "))
        print(f"The {n}th Fibonacci number is: {frodo(n)}")
    elif choice == '2':
        limit = int(input("Enter the limit: "))
        sequence = aragorn(limit)
        print(f"Fibonacci sequence up to {limit}: {sequence}")
    else:
        print("Invalid choice!")



if __name__ == "__main__":
    legolas()
