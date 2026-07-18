number1 = int(input("Enter an input number greater than 10"))
number2 = int(input("Enter an input number less than 20"))
print(number1 + number2)
subtraction = number1 - number2
print(number1 - number2)
multiplication = number1 * number2
print(number1 * number2)
division = number1 / number2
print(number1 / number2)

choice  = input("1.Addition , 2.Subtraction , 3.multiplication , 4.Division")
if choice == "Addition":
    addition = number1+number2
elif choice  == "Subtraction":
     subtraction = number1 - number2
elif choice == "multiplication":
      multiplication = number1 * number2
elif choice == "Division":
      Division = number1 / number2