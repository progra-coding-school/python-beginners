
def calculator():
    number1=int(input("Please enter the first number : "))
    number2 = int(input("Please enter the second number: "))
    operator = input("Please enter the operation : addition , substraction, multiplication, division :")
    if (operator=="addition"):
        answer=addition(number1,number2)
        print("The sum is ",answer)
    elif (operator=="substraction"):
        answer = substraction(number1, number2)
        print("The diff is ", answer)
    elif (operator=="multiplication"):
        answer = multiplication(number1, number2)
        print("The product is ", answer)
    elif (operator=="division"):
        answer = division(number1, number2)
        print("The answer is ", answer)

def addition(a,b):
    result=a+b
    return result

def substraction(a,b):
    result=a-b
    return result

def multiplication(a,b):
    result=a*b
    return result

def division(a,b):
    result=a/b
    return result


calculator()