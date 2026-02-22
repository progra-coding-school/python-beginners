# Program Code: DT-KN-04
# Title: Type Conversion
# Cognitive Skill: Knowledge
# Topic: Data Types in Python

# TYPE CONVERSION — changing a value from one type to another

# String → Integer
age_text = "15"
age_number = int(age_text)
print(age_number + 1)      # 16  (adding works now!)
print(type(age_number))    # <class 'int'>

# Integer → String
score = 98
score_text = str(score)
print("Score: " + score_text)   # can join with text now
print(type(score_text))

# String → Float
price_text = "49.99"
price = float(price_text)
print(price * 2)           # 99.98
print(type(price))

# Integer → Float
whole = 7
decimal = float(whole)
print(decimal)             # 7.0
print(type(decimal))

# Float → Integer (drops decimal, does NOT round)
gpa = 9.8
gpa_int = int(gpa)
print(gpa_int)             # 9 (NOT 10!)

# Boolean conversions
print(bool(1))     # True
print(bool(0))     # False
print(bool(""))    # False — empty string
print(bool("Hi"))  # True — non-empty string

# Think:
# 1. input() always returns a string. What must you do before using it in maths?
# 2. int(9.9) gives 9, not 10. When could this cause a real bug?
