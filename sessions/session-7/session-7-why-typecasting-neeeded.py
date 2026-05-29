number1=input("Please enter the first number: ")
number2=input("Please enter the second number: ")
print(type(number1))
print(type(number2))
sum=number1+number2

print("Before typecasting the sum is :",sum)

number1=int(number1)
number2=int(number2)

print(type(number1))
print(type(number2))

sum=number1+number2
print("After typecasting the sum is :",sum)
