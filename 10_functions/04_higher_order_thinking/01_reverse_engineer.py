# Program Code: FN-HOT-01
# Title: Reverse Engineer — Design the Function
# Cognitive Skill: Higher Order Thinking (Reverse Engineering)
# Topic: Functions in Python

# Given the FUNCTION CALL and the OUTPUT — design the function!
# Work backwards from what you know.

score = 0

print("=== Reverse Engineer ===")
print("Given the call and output — write what the function body must be.")
print()

# --- Challenge 1 ---
print("Challenge 1:")
print("  Call:   make_greeting('Aarav')")
print("  Output: 'Hello, Aarav! Welcome to Progra.'")
print("What must be inside the function?")
answer = input("> ")
print("Answer: return 'Hello, ' + name + '! Welcome to Progra.'")
print("  OR:   return f'Hello, {name}! Welcome to Progra.'")
# Verify:
def make_greeting(name):
    return f"Hello, {name}! Welcome to Progra."
print("  Verified:", make_greeting("Aarav"))
print()

# --- Challenge 2 ---
print("Challenge 2:")
print("  Call:   percent_score(45, 60)")
print("  Output: 75.0")
print("What calculation is inside?")
answer = input("> ")
print("Answer: return (marks / total) * 100")
def percent_score(marks, total):
    return (marks / total) * 100
print("  Verified:", percent_score(45, 60))
print()

# --- Challenge 3 ---
print("Challenge 3:")
print("  Call:   is_eligible(16, True)")
print("  Output: False")
print("  Call:   is_eligible(18, True)")
print("  Output: True")
print("What condition does the function check?")
answer = input("> ")
print("Answer: return age >= 18 and has_id")
def is_eligible(age, has_id):
    return age >= 18 and has_id
print("  Verified:", is_eligible(16, True), is_eligible(18, True))
print()

# --- Challenge 4 ---
print("Challenge 4:")
print("  Call:   describe_number(9)")
print("  Output: '9 is odd and not divisible by 3'")
print("  Call:   describe_number(12)")
print("  Output: '12 is even and divisible by 3'")
answer = input("What must the function do? ")
def describe_number(n):
    even_odd = "even" if n % 2 == 0 else "odd"
    div3 = "divisible by 3" if n % 3 == 0 else "not divisible by 3"
    return f"{n} is {even_odd} and {div3}"
print("  Verified:", describe_number(9))
print("  Verified:", describe_number(12))
print()

# --- Challenge 5 ---
print("Challenge 5:")
print("  Call:   apply_discount(500, 10)")
print("  Output: 450.0")
print("  Call:   apply_discount(200, 25)")
print("  Output: 150.0")
answer = input("What formula is inside? ")
print("Answer: discount = price * percent / 100; return price - discount")
def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount
print("  Verified:", apply_discount(500, 10), apply_discount(200, 25))
print()

print("Reverse engineering builds deep understanding. Great thinking!")
