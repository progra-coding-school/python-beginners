# Program Code: DT-UN-02
# Title: How Python Stores Data
# Cognitive Skill: Understanding
# Topic: Data Types in Python

# Python automatically picks a type when you create a variable.
# This is called "dynamic typing".

# Python sees 13 → int
age = 13
print(type(age))           # <class 'int'>

# Python sees 13.5 → float
weight = 13.5
print(type(weight))        # <class 'float'>

# Python sees "hello" → str
city = "Chennai"
print(type(city))          # <class 'str'>

# Python sees True/False → bool
is_member = True
print(type(is_member))     # <class 'bool'>

# The type is stored WITH the value (Python tracks it for you)

# You can CHANGE the type of a variable (Python is flexible!)
score = 95            # int
print(type(score))    # <class 'int'>
score = 95.5          # now float
print(type(score))    # <class 'float'>
score = "Excellent"   # now str
print(type(score))    # <class 'str'>

# Each type allows different OPERATIONS
marks = 95
print(marks + 5)      # math: 100   (works for int/float)
word = "hello"
print(word + "!")     # join: hello!  (works for str)
print(word * 3)       # repeat: hellohellohello  (str only)

# Think:
# 1. Python lets you do score = 95 and then score = "Excellent".
#    Is this a good idea? What problems might it cause?
# 2. What does word * 3 produce? How is this different from int * 3?
