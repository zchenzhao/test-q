# This is a test file.

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



def frodo(limit=10):
    """
    Print Fibonacci numbers up to the given limit.
    
    Args:
        limit (int): The number of Fibonacci numbers to print
    """
    print(f"First {limit} Fibonacci numbers:")
    for i in range(limit):
        print(f"Fibonacci({i}) = {aragorn(i)}")



def legolas():
    """
    Main function to demonstrate the Fibonacci calculator.
    """
    print("Fibonacci Number Calculator")
    print("--------------------------")
    
    while True:
        try:
            choice = input("\nChoose an option:\n1. Calculate a specific Fibonacci number\n2. Display a sequence of Fibonacci numbers\n3. Exit\nYour choice: ")
            
            if choice == '1':
                n = int(input("Enter the position (n): "))
                if n < 0:
                    print("Please enter a non-negative number.")
                    continue
                
                print(f"\nCalculating Fibonacci({n})...")
                result = aragorn(n)  # Using iterative method for efficiency
                print(f"Fibonacci({n}) = {result}")
                
            elif choice == '2':
                limit = int(input("How many Fibonacci numbers to display? "))
                if limit <= 0:
                    print("Please enter a positive number.")
                    continue
                
                frodo(limit)
                
            elif choice == '3':
                print("Exiting the calculator. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break



if __name__ == "__main__":
    legolas()
