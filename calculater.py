number1=int(input("enter the first number:"))
operation=input("enter the operation:")
number2=int(input("enter the second number:"))
if operation=="+":
    answer=number1+number2
    print(f"answer is {answer}")
elif operation=="-":
    answer = number1-number2
    print(f"answer is {answer}")
elif operation=="*":
    answer = number1*number2
    print(f"answer is {answer}")
elif  operation=="/":
    answer = number1/number2
    print(f"answer is {answer}")
else:
    print("sorry... this operation is not supported..")