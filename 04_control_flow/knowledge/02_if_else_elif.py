# Program Code: CF-KN-02
# Title: if, if-else, if-elif-else
# Cognitive Skill: Knowledge
# Topic: Control Flow in Python

# ── IF ─────────────────────────────────────────────────────────────────────
# Run code ONLY when the condition is True.

day = "Saturday"
if day == "Saturday":
    print("We will be having coding class today.")

print("Program control reaches here regardless.")

# When condition is False — nothing happens, Python just moves on
day = "Monday"
if day == "Saturday":
    print("We will be having coding class today.")
# (no output — condition is False, code inside is skipped)

# IF with a boolean variable
feeling_sleepy = True
if feeling_sleepy:
    print("Go and sleep.")

is_tank_full = True
if is_tank_full:
    print("Turn off the motor.")

# IF with a comparison
current_time = 7
if current_time > 6:
    print("Turn on the lights.")

ratings = 4
if ratings >= 3:
    print("That's a good product!")

# ── IF-ELSE ────────────────────────────────────────────────────────────────
# One of the two paths ALWAYS runs.

day = "Sunday"
if day == "Saturday":
    print("Coding class today!")
else:
    print("No coding class today.")

age = 16
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# ── IF-ELIF-ELSE ───────────────────────────────────────────────────────────
# Pick exactly ONE path from many options.

day = "saturday"
if day == "saturday":
    print("We will be having coding class.")
elif day == "monday":
    print("We will be having badminton class.")
elif day == "wednesday":
    print("We will be having guitar class.")
else:
    print("We don't have any classes today.")

# Grade calculator
score = 85
if score >= 90:
    print("Grade: A+ — Excellent!")
elif score >= 80:
    print("Grade: A — Very Good!")
elif score >= 70:
    print("Grade: B — Good.")
elif score >= 60:
    print("Grade: C — Pass.")
else:
    print("Grade: F — Fail.")
print("Grading complete.")

# Comparison operators quick reference:
# ==  equal to        !=  not equal to
# >   greater than    <   less than
# >=  greater or equal    <=  less or equal

# Think:
# 1. What is the difference between = and == ?
# 2. In the day-class example, what happens if you replace 'elif' with 'if'?
# 3. Can you add Friday → "We will be having music class"?
