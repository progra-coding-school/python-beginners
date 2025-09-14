#My First Program

#Using double quotes
#print("Hello World")

#Using single quotes
#print('Hello World')

#Passing 2 arguments to the print function
#print("Hello","World")
#print('Hello','World')

#Passing 6 arguments to the print function
# print("How","Are","You","I","am","fine")
# print('How','Are','You','I','am','fine')
# print('How',"Are",'You',"I",'am','fine')

# print('Hello'
#       ' World')


# print(" Today "
#       "We are "
#       "having Coding class ")

#Multiline Printing using triple double quotes
# print(""" Today
#  We are
#  having
#  Coding class """)

#Multiline Printing using triple single quote
# print(''' Today
#  We are
#  having
#  Coding
#  class ''')

#Python case sensitive-NameError will be thrown as there is no function PRINT
# PRINT("Hello World")
"""
Python case sensitive there is no builtin function called 'PRINT'.
so we will be getting NameError: name 'PRINT'
 is not defined
"""

#Python case sensitive-NameError will be thrown as there is no function print1
# print1("Hello World")
"""
There is no builtin function called 'print1'.
So 'NameError: name 'print1' is not defined' will be thrown
"""

#SyntaxError due to Missing parentheses in call to 'print'
# print "Hello World"
"""
We will be getting SyntaxError: Missing parentheses in call to 'print'.
parantheses are required from python 3.0
"""

#It will work as its a number and it does not require quotes
#print(100)

#Error will be thrown if we are not enclosing texts inside quotes
# print("Apple")

#It will perform addition
#print(5+5)

# print('5'+'5')
"""
single quote -> string
Two strings  are joined or concatenated
"""


# print("5"+"5")
"""
Single or double quotes will be considered as strings
5+5=55
"""

# print("Hello "+"World")
"""
Single or double quotes will be considered as strings
so here strings are joined
"""

# print(5+'5')
"""
5-> Int
'5'-> String
We cannot add a integer and a string. 
TypeError: unsupported operand type(s) - Error will be thrown
"""

# print(5-5)

# print(5*5)
"""
*-> Multiplication Operator
"""

print(5/5)
"""
/ -> Division Operator
1.0 -> Floating point number
"""

# print:
#------
# This is a built-in Python function used to display messages or output text
# to the console (the screen where your program runs).
#
# ("Hello World"):
#----------------
# The parentheses () are used to pass arguments (in this case, a string)
# into the print() function.
#
# "Hello World" is a string, which is a sequence of characters enclosed in
# quotes. This is the message that will be printed.