# Program Code: VAR-KN-03
# Title: Naming Rules
# Cognitive Skill: Knowledge
# Topic: Variables in Python

# Rules: only letters, digits, underscore. Cannot start with digit.
# No spaces, no hyphens, no keywords (if, for, while...)
# Case-sensitive: age and Age are different.

student_name = "Aarav"
marks2024 = 92
_score = 100

print(student_name)
print(marks2024)
print(_score)

# Case matters — these are 3 different variables
age = 13
Age = 25
print(age)
print(Age)

# Multiple assignment — one line, multiple variables
tamil, english, maths = 88, 91, 95
print(tamil, english, maths)

# Same value to many variables
science = social = computer = 0
print(science, social, computer)

# Invalid names — these cause SyntaxError (shown as comments):
# 2name  = "Aarav"   starts with digit
# my age = 13        has a space
# my-age = 13        hyphen not allowed
# for    = 5         'for' is a keyword

# Convention: use snake_case — student_name, total_marks, is_present
