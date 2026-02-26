# Task 1: Read a File and Handle Errors

try:
    # Attempt to open the file in read mode
    with open("sample.txt", "r") as file:
        print("Reading file content:")

        # Read file line by line

        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")



except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")