# Task 2: Using the Math Module

import math

# Taking user input
number = float(input("Enter a number: "))

if number <= 0:
    print("Natural logarithm and square root are only defined for positive numbers.")
else:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print(f"Square Root of {number} = {square_root}")
    print(f"Natural Log of {number} = {natural_log}")
    print(f"Sine of {number} = {sine_value}")