# Program Code: VAR-CT-02
# Title: Which Approach is Better?
# Cognitive Skill: Critical Thinking (Comparing approaches)
# Topic: Variables in Python

# Problem 1: Aarav earns Rs.500, spends Rs.200 on snacks, Rs.100 on books.

print("--- Problem 1 ---")
print("Approach A:")
print("  savings = 500 - 200 - 100")
print("Approach B:")
print("  pocket_money = 500")
print("  snacks = 200")
print("  books = 100")
print("  savings = pocket_money - snacks - books")

savings_a = 500 - 200 - 100

pocket_money = 500
snacks = 200
books = 100
savings_b = pocket_money - snacks - books

print("Approach A result:", savings_a)
print("Approach B result:", savings_b)

choice = input("Which is better? (A or B) ")
print("Both give the same answer.")
print("Approach B is clearer — you know what each number means.")
print("If Aarav adds a new expense, Approach B is easier to update.")

input("Press Enter for Problem 2...")

# Problem 2: Celsius to Fahrenheit
print("--- Problem 2 ---")
print("Approach A: fahrenheit = (37 * 9/5) + 32")
print("Approach B: celsius = 37")
print("            fahrenheit = (celsius * 9/5) + 32")

choice = input("Which is better? (A or B) ")
print("Approach B is better.")
print("If you change celsius, the formula updates automatically.")
print("In Approach A, the number 37 is hardcoded — easy to forget to update.")

input("Press Enter for Problem 3...")

# Problem 3: Printing student info
print("--- Problem 3 ---")
print("Approach A: separate print for each variable")
print("Approach B: one line combining all")

choice = input("Which is better? (A or B) ")
print("Both are valid — it depends on what output you want.")
print("Sometimes there is no single best answer.")
print("A good programmer chooses based on the situation.")

# Think:
# 1. Why is clear code often better than short code?
# 2. Once you store a value in a variable, should you use the variable
#    or the raw number in your calculations? Why?
