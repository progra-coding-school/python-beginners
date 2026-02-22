# Program Code: VAR-UN-02
# Title: How Variables Work
# Cognitive Skill: Understanding
# Topic: Variables in Python

# A variable is like a labelled box in memory.
# The name is the label. The value is what's inside.

score = 0
name = "Rohit"
price = 49.99

print(score)
print(name)
print(price)

# Reassignment — same box, new value (old value is gone)
name = "Dhoni"
print(name)     # Rohit is gone

# Python detects type automatically
age = 14          # int
height = 5.4      # float
city = "Chennai"  # str
passed = True     # bool

print(type(age))
print(type(height))
print(type(city))
print(type(passed))

# Updating using the variable's own value
score = 20
score = score + 10    # now 30
score = score * 2     # now 60
print(score)

# Shorthand
score += 5     # same as score = score + 5
score -= 10    # same as score = score - 10
score *= 2     # same as score = score * 2
print(score)

# Think:
# 1. What is score after: score = 10, score += 5, score *= 2 ?
# 2. What happens if you print a variable before creating it?
