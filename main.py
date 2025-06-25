# This is a test file.
# Fibonacci Number Calculator

import sys


def frodo(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
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



def gandalf(n):
    """
    Generate a list of Fibonacci numbers up to the nth position.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        list: A list of Fibonacci numbers from F(0) to F(n)
    """
    if n < 0:
        return []
    
    fibonacci_sequence = [0]
    if n >= 1:
        fibonacci_sequence.append(1)
        
    for i in range(2, n + 1):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    return fibonacci_sequence



def aragorn():
    """
    Main function to demonstrate the Fibonacci calculator.
    """
    print("Fibonacci Number Calculator")
    print("==========================")
    
    try:
        n = int(input("Enter a position (n) to calculate the Fibonacci number: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        
        print(f"The {n}th Fibonacci number is: {frodo(n)}")
        print(f"Fibonacci sequence up to position {n}: {gandalf(n)}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")



if __name__ == "__main__":
    aragorn()
