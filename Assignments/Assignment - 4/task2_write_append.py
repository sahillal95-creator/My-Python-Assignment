# Task 2: Write and Append Data to a File

try:
    # Step 1: Take first input
    first_text = input("Enter text to write to the file: ")

    # Step 2: Write to file (overwrite mode)
    with open("output.txt", "w") as file:
        file.write(first_text + "\n")

    print("Data successfully written to output.txt.\n")

    # Step 3: Take additional input
    additional_text = input("Enter additional text to append: ")

    # Step 4: Append to file
    with open("output.txt", "a") as file:
        file.write(additional_text + "\n")

    print("Data successfully appended.\n")

    # Step 5: Read and display final content
    print("Final content of output.txt:")
    with open("output.txt", "r") as file:
        print(file.read())

except Exception as e:
    print(f"An error occurred: {e}")