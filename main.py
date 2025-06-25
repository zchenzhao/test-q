# This is a test file! :D
import time


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
        return gandalf(n - 1) + gandalf(n - 2)



def aragorn(n):
    """
    Calculate the nth Fibonacci number using iteration.
    
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
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def legolas(n, method="iterative"):
    """
    Calculate and display the nth Fibonacci number using the specified method.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        method (str): The calculation method - "recursive" or "iterative"
        
    Returns:
        int: The nth Fibonacci number
    """
    start_time = time.time()
    
    if method == "recursive":
        result = gandalf(n)
        method_name = "Recursive (Gandalf)"
    else:
        result = aragorn(n)
        method_name = "Iterative (Aragorn)"
    
    end_time = time.time()
    print(f"Fibonacci number at position {n}: {result}")
    print(f"Method: {method_name}")
    print(f"Calculation time: {end_time - start_time:.6f} seconds")
    
    return result



def frodo():
    """
    Main function to demonstrate the Fibonacci calculator.
    """
    print("Fibonacci Number Calculator")
    print("==========================")
    
    while True:
        try:
            n = int(input("\nEnter the position (n) in the Fibonacci sequence (or -1 to quit): "))
            if n == -1:
                print("Goodbye!")
                break
            
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            
            method = input("Choose calculation method (r for recursive, i for iterative): ").lower()
            
            if method == 'r':
                if n > 35:
                    print("Warning: Recursive calculation may be very slow for n > 35.")
                    confirm = input("Continue anyway? (y/n): ").lower()
                    if confirm != 'y':
                        continue
                legolas(n, "recursive")
            else:
                legolas(n, "iterative")
                
        except ValueError:
            print("Please enter a valid integer.")



if __name__ == "__main__":
    frodo()
