# Program Code: DT-CT-02
# Title: Which Type Is Better?
# Cognitive Skill: Critical Thinking (Evaluating choices)
# Topic: Data Types in Python

# For each scenario, compare two approaches and decide which is better.
print("=== Which Type Is Better? ===\n")

# Scenario 1: Phone number
print("--- Scenario 1: Storing a Phone Number ---")
phone_as_int = 9876543210
phone_as_str = "9876543210"
print("As int:", phone_as_int)
print("As str:", phone_as_str)
print("Can you do maths on a phone number? No.")
print("Can phone numbers start with 0? Yes — but int drops leading zeros.")
print("Winner: str  — phone numbers are identifiers, not quantities.")
input("Press Enter to continue...")

# Scenario 2: Age
print("\n--- Scenario 2: Storing Age ---")
age_as_str = "13"
age_as_int = 13
print("As str:", age_as_str, "→ cannot calculate 'next year'")
print("As int:", age_as_int, "→", age_as_int + 1, "next year")
print("Winner: int — age is a quantity used in calculations.")
input("Press Enter to continue...")

# Scenario 3: Price
print("\n--- Scenario 3: Storing Price (Rs.49.50) ---")
price_as_int = 49
price_as_float = 49.50
print("As int:", price_as_int, "→ loses the 50 paise!")
print("As float:", price_as_float, "→ accurate")
print("Winner: float — prices have decimals.")
input("Press Enter to continue...")

# Scenario 4: Is present?
print("\n--- Scenario 4: Is the student present today? ---")
present_as_str = "yes"
present_as_bool = True
print("As str:", present_as_str, "→ requires exact matching ('Yes'? 'YES'?)")
print("As bool:", present_as_bool, "→ clean True/False, works in if/else directly")
print("Winner: bool — yes/no questions are naturally boolean.")

# Think:
# 1. You're building an app. User enters their PIN (e.g., 0042).
#    Should PIN be int or str? Why?
# 2. What type would you use for a percentage like 85.5%?
