
#Create a function `add()` to add two numbers

def add(a,b):
    ans=a+b
    return ans

#Create a function `subtract()` to subtract two numbers.

def subtract(a,b):
    ans=a-b
    return ans

#Create a function `multiply()` to multiply two numbers.

def multiply(a,b):
    ans=a*b
    return ans


#Create a function `divide()` to divide two numbers.

def divide(a,b):
    ans=a/b
    return ans


#Create the `calculator()` function

def calculator():
    number1=int(input("Please enter your first number : "))
    number2 = int(input("Please enter your second number : "))
    operation = input("Please enter what operation you want to perform +.-,*,/ : ")
    if (operation=='+'):
        result=add(number1,number2)
        print("The addition operation result is : ",result)
    elif (operation=='-'):
        result = subtract(number1, number2)
        print("The subtract operation result is : ", result)
    elif (operation=='*'):
        result = multiply(number1, number2)
        print("The multiplication operation result is : ", result)
    elif (operation=='/'):
        result = divide(number1, number2)
        print("The division operation result is : ", result)
    else:
        print("The operation is not supported")

calculator()