number = int(input("Enter a number : "))

# Method - 1
if number % 2 == 0 :
    print (number, "is an even number.")
else :
    print (number, "is an odd number.")

# Method - 2

print (number, "is an even number.") if number % 2 == 0 else print (number, "is an odd number.")
