'''📘 Assignment -7
1️⃣ String to Integer
Create a program to convert a number stored as a string into an integer
and print the type before and after conversion.

2️⃣ Float to Integer
Create a program to convert a float value into an integer and observe
what happens to the decimal part.

3️⃣ Text to Integer
Try converting a text value (example: a name) into an integer and
observe the error generated.

4️⃣ Boolean to Integer
Convert boolean values (True / False) into integers and observe the output.

🎯 Expected Learning
Students will understand:
Different Python data types
Type conversion using int()
Valid and invalid conversions
How Python handles boolean values

'''

#Typecasting string number  to int

age="10"
print(type(age))
age=int(age)
print(type(age))
print(age)

#Typecasting float  to int

age=100.45
print(type(age))
age=int(age)
print(type(age))
print(age)

#Typecasting str text to int
name="Daniel"
print(type(name))
name=int(name)
print(type(name))
print(name)

#Typecasting bool to int
is_raining=False
print(type(is_raining))
is_raining=int(is_raining)
print(type(is_raining))
print(is_raining)