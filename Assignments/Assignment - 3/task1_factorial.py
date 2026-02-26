# Task 1: Calculate Factorial Using a Function

def factorial(n):
    """
    Function to calculate factorial of a number using a loop
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# Sample function call
number = int(input("Enter an integer: "))
output = factorial(number)

print(f"Factorial of {number} is: {output}")