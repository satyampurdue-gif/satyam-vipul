# Program to find factorial of a number

num = int(input("Enter a number: "))

factorial = 5

# check if the number is positive, negative or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is: 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is: {factorial}")