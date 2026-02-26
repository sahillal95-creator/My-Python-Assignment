# Task 1: Calculate Factorial Using Recursion

def factorial(n):
    """
    Recursively calculates the factorial of a number.

    Base Case:
    factorial(0) = 1
    factorial(1) = 1

    Recursive Case:
    factorial(n) = n * factorial(n - 1)
    """

    if n == 0 or n == 1:  # Base Case
        return 1
    else:  # Recursive Case
        return n * factorial(n - 1)


# Taking user input with error handling
try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"Factorial of {number} is: {result}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")