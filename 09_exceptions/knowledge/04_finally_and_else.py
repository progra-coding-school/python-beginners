# Program Code: EX-KN-04
# Title: finally and else Clauses
# Cognitive Skill: Knowledge
# Topic: Exceptions in Python

# try/except has two optional extra blocks:
#   else    → runs ONLY if NO exception occurred
#   finally → runs ALWAYS, whether or not an exception occurred

# --- else: code for the "success" path ---
print("=== else — runs only on success ===")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Cannot divide by zero!")
    else:
        print(f"  Success! {a} / {b} = {result:.2f}")

divide(10, 2)   # else runs
divide(10, 0)   # except runs, else is SKIPPED

print()

# --- finally: cleanup code that always runs ---
print("=== finally — always runs ===")

def read_score(value):
    try:
        score = int(value)
        print(f"  Score parsed: {score}")
    except ValueError:
        print(f"  '{value}' is not a valid score.")
    finally:
        print("  [finally] Done processing this value.\n")

read_score("85")
read_score("abc")
read_score("0")

# --- Real-world analogy ---
print("=== Real-world analogy ===")
print("try    → Open a shop")
print("except → Handle problems (power cut, no stock)")
print("else   → Serve happy customers (only if no problems)")
print("finally→ Lock up the shop at the end (happens no matter what)")

print()

# --- All four together ---
print("=== All four blocks together ===")

def safe_convert(text):
    print(f"Processing '{text}':")
    try:
        number = int(text)
    except ValueError as e:
        print(f"  except: {e}")
    else:
        print(f"  else: converted successfully → {number}")
    finally:
        print(f"  finally: always runs")
    print()

safe_convert("42")
safe_convert("hello")

# Think:
# 1. If an exception occurs, does the `else` block run?
# 2. Name a real situation where `finally` is critical — think about files or databases.
