# Naming Matters — Good Dictionary Names Make Code Self-Explanatory
# The name of a dictionary and its keys should tell you exactly what the data is.
# Bad names (d, d2, x, k) force you to read the WHOLE program to understand it.
# Good names (student_marks, fruit_prices) make code read like plain English.

# Version A: Poor naming — you must read every line to guess what this does
print("Version A: Poor naming (hard to read):")
d  = {"a": 13, "b": 7, "c": 85}   # what is d? what are "a", "b", "c"?
d2 = {}

for x in d:
    if d[x] > 10:
        d2[x] = d[x]   # what is being filtered? for what reason?

print(d2)

print()

# Version B: Good naming — the code explains itself without needing extra comments
print("Version B: Good naming (self-explanatory):")
student_ages     = {"Aarav": 13, "Diya": 7, "Karthik": 85}   # clearly: student name → age
secondary_school = {}   # clearly: students old enough for secondary school

for student_name, age in student_ages.items():
    if age > 10:
        secondary_school[student_name] = age   # readable: filter students over 10

print(secondary_school)

print()

# Naming rules for dictionaries — follow these every time
print("Naming Guidelines:")
guidelines = {
    "Use noun phrases"        : "student_marks, not d or data",
    "Key describes content"   : "'name', 'price', 'qty' — not 'k' or 'x'",
    "Plural for collections"  : "contacts = {}, not contact = {}",
    "Avoid abbreviations"     : "total_price not tp",
    "Singular for one record" : "student = {'name': 'Aarav'} not students",
}

for rule, example in guidelines.items():
    print("  " + rule.ljust(28) + " → " + example)

print()

# Practice: rename these poorly named variables
# The rule: ask "what does this dict hold?" and use plural noun + context word
print("Practice: What better names would you use?")

# Poor: d3 = {"r": 120, "g": 45, "b": 85}
# "r", "g", "b" are cryptic. Better: full fruit names and a descriptive variable name
print("Rename d3:")
fruit_prices = {"mango": 120, "banana": 45, "apple": 85}
print("  fruit_prices =", fruit_prices)

# Poor: x2 = {"p": "9876543210", "q": "9123456780"}
# "p" and "q" are meaningless. Better: clear labels and a meaningful dict name
print("Rename x2:")
emergency_contacts = {"hospital": "9876543210", "police": "9123456780"}
print("  emergency_contacts =", emergency_contacts)
