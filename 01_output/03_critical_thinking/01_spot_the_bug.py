# Program Code: OUT-CT-01
# Title: Spot the Bug — Output
# Cognitive Skill: Critical Thinking (Bug Spotting)
# Topic: Output in Python

# Each snippet has a bug. Find it, explain why it's wrong, and fix it.

print("=== Bug 1 ===")
print("""
  PRINT("Hello World")
""")
answer = input("What is the bug? ")
print("Bug: PRINT is not valid — Python is case-sensitive.")
print("     print() must be lowercase.")
print("Fix: print('Hello World')")
print()

print("=== Bug 2 ===")
print("""
  print("It's a sunny day!)
""")
answer = input("What is the bug? ")
print("Bug: Missing closing double quote — SyntaxError.")
print('Fix: print("It\'s a sunny day!")')
print("  OR: print(\"It's a sunny day!\")")
print()

print("=== Bug 3 ===")
print("""
  print("My name is" + Aarav)
""")
answer = input("What is the bug? ")
print("Bug: Aarav has no quotes — Python thinks it's a variable name.")
print('     If Aarav is not defined, NameError! If it should be text, it needs quotes.')
print('Fix: print("My name is" + "Aarav")')
print('  OR: print("My name is Aarav")')
print()

print("=== Bug 4 ===")
print("""
  print("Hello, Diya you are " + 13 + " years old.")
""")
answer = input("What is the bug? ")
print("Bug: Cannot concatenate str and int with +.")
print("     13 is an integer, not a string → TypeError!")
print('Fix: print("Hello, Diya you are " + str(13) + " years old.")')
print()

print("=== Bug 5 ===")
print("""
  print1("Hello World")
""")
answer = input("What is the bug? ")
print("Bug: print1 does not exist — NameError.")
print("     The function is called print, not print1.")
print("Fix: print('Hello World')")
print()

print("=== Bug 6 ===")
print("""
  print "Hello World"
""")
answer = input("What is the bug? ")
print("Bug: Missing parentheses — SyntaxError.")
print("     In Python 3, print is a function and MUST have ().")
print('Fix: print("Hello World")')
print()

print("Most common output bugs:")
print("  1. PRINT instead of print (case-sensitive)")
print("  2. Missing opening or closing quote")
print("  3. Mixing strings and integers with +")
print("  4. Missing parentheses ()")
