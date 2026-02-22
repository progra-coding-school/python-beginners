# Program Code: OUT-UN-04
# Title: Formatting Output — Making It Readable
# Cognitive Skill: Understanding
# Topic: Output in Python

# Good output isn't just correct — it's READABLE and PRESENTABLE.
# Let's explore ways to format output beautifully.

print("=== 1. Alignment with f-strings ===")
# :10  → left-align in a field of 10 characters
# :>10 → right-align
# :^10 → centre-align
print(f"{'Name':<12} {'Marks':>6} {'Grade':^8}")
print("-" * 28)
print(f"{'Aarav':<12} {85:>6} {'A':^8}")
print(f"{'Diya':<12} {72:>6} {'B':^8}")
print(f"{'Karthik':<12} {91:>6} {'A+':^8}")

print()

print("=== 2. Decimal precision ===")
pi = 3.14159265
print(f"Pi (full):      {pi}")
print(f"Pi (2 decimal): {pi:.2f}")
print(f"Pi (4 decimal): {pi:.4f}")

average = 253 / 3
print(f"Average (raw):  {average}")
print(f"Average (1dp):  {average:.1f}")

print()

print("=== 3. Separators and borders ===")
def print_header(title):
    width = 35
    print("=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_row(label, value):
    print(f"  {label:<15} : {value}")

print_header("Progra School Report")
print_row("Student", "Aarav")
print_row("Class", "Grade 7")
print_row("Total Marks", "253 / 300")
print_row("Average", "84.3")
print_row("Grade", "A")
print("=" * 35)

print()

print("=== 4. Multiline output for readability ===")
# Bad — all on one line
print("Name: Aarav Age: 13 School: Progra Marks: 85 90 78")

# Good — structured
print()
print("Name   : Aarav")
print("Age    : 13")
print("School : Progra Kids Coding School")
print("Marks  : Maths=85, Science=90, English=78")

print()

print("=== 5. Using blank lines to group output ===")
print("Section 1: Personal Info")
print("  Name: Aarav")
print("  Age: 13")
print()    # blank line separates sections
print("Section 2: Academic Info")
print("  Total: 253")
print("  Grade: A")

# Think:
# 1. How would you print a rupee amount always showing 2 decimal places?
#    e.g., Rs.50 should show as Rs.50.00
# 2. What does {:^20} do? Try it with your name.
