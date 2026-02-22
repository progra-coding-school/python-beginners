# Program Code: VAR-KN-02
# Title: Variable Types
# Cognitive Skill: Knowledge
# Topic: Variables in Python

# 4 main types: int, float, str, bool

age = 13          # int   — whole number
marks = 92.5      # float — decimal number
name = "Diya"     # str   — text in quotes
is_present = True # bool  — True or False

print(age)
print(marks)
print(name)
print(is_present)

# type() tells you what type a variable is
print(type(age))
print(type(marks))
print(type(name))
print(type(is_present))

# 27, 27.0, and "27" are all different
print(type(27))     # int
print(type(27.0))   # float — decimal point makes it float
print(type("27"))   # str  — quotes make it text

# Think: What type would you use for a student's marks? name? attendance?
