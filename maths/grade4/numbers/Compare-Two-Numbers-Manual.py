# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 1: Count digits
digits1 = len(str(num1))
digits2 = len(str(num2))

# Step 2: Compare number of digits
if digits1 > digits2:
    print(num1, "is greater than", num2)
elif digits1 < digits2:
    print(num1, "is smaller than", num2)
else:
    print("Both numbers have the same number of digits")

    # Step 3: Compare each place value
    str1 = str(num1)
    str2 = str(num2)

    i = 0
    while i < digits1:
        if str1[i] > str2[i]:
            print(num1, "is greater than", num2)
            break
        elif str1[i] < str2[i]:
            print(num1, "is smaller than", num2)
            break
        i += 1
    else:
        print("Both numbers are equal")
