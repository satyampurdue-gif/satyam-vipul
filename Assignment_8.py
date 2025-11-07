# Task 1

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}
name = input("Enter the student's name: ")


if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")


# Task 2
numbers = list(range(1, 11))
print("Original list:", numbers)

first_five = numbers[:5]
print("Extracted first five elements:", first_five)

reversed_list = first_five[::-1]
print("Reversed extracted elements:", reversed_list)