# Task 1: Check if a Number is Even or Odd

# Taking integer input from user
number = int(input("Enter an integer: "))

# Checking whether the number is even or odd
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")