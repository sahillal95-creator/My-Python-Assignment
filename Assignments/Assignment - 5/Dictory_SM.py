# Task 1 - Dictionary of Student Marks

# creating a dictionary of students and their marks
students = {"Rahul": 85,"Amit": 90,"Sneha": 78,"Priya": 92}

# asking user to enter student name
name = input("Enter the student name: ")

# checking if name is in dictionary
if name in students:
    print("Marks of", name, "is", students[name])
else:
    print("Student not found in the record.")