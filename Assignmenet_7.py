# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        print("Reading file content:\n")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")


except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

# Task 2: Write and Append Data to a File


text_to_write = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")


text_to_append = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.\n")


print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())