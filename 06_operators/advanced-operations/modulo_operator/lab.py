number=input("Please enter the number:")
number=int(number)

remainder_value=number % 2
print(remainder_value)
if remainder_value==0:
    print('Its a Even number')
else:
    print('Its a Odd number')