# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compare the numbers
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is smaller than", num2)
else:
    print("Both numbers are equal")
