# Program Code: DT-KN-02
# Title: Integers and Floats
# Cognitive Skill: Knowledge
# Topic: Data Types in Python

# INTEGERS — whole numbers (no decimal point)
runs = 42
wickets = 3
year = 2025
temperature = -5     # negative integers are valid too!

print("Runs:", runs)
print("Wickets:", wickets)
print("Year:", year)
print("Temperature:", temperature)

# FLOATS — numbers with a decimal point
price = 29.99
average_marks = 87.5
distance_km = 1.5

print("Price:", price)
print("Average marks:", average_marks)
print("Distance:", distance_km)

# Arithmetic with ints stays int (usually)
total_runs = runs + 8
print("Total runs:", total_runs, type(total_runs))

# Arithmetic with a float makes the result a float
price_with_gst = price * 1.18
print("Price with GST:", price_with_gst, type(price_with_gst))

# Division ALWAYS gives a float
ratio = 10 / 4
print("10 / 4 =", ratio, type(ratio))  # 2.5, not 2

# Floor division gives an int
ratio_floor = 10 // 4
print("10 // 4 =", ratio_floor, type(ratio_floor))  # 2

# Think:
# 1. Why does Python make 10/4 = 2.5 and not 2?
# 2. If you want to split 10 cookies equally among 4 friends with no halves,
#    which operator would you use?
