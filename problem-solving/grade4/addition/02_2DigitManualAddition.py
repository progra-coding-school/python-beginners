# Input two 2-digit numbers
num1 = 34
num2 = 58

# Step 1: Extract ones digit
ones1 = num1 % 10
ones2 = num2 % 10

# Step 2: Add ones digits
ones_sum = ones1 + ones2

# Step 3: Extract tens digit
tens1 = num1 // 10
tens2 = num2 // 10

# Step 4: Add tens digits
tens_sum = tens1 + tens2

# Step 5: Combine tens and ones
total = (tens_sum * 10) + ones_sum

print("Sum =", total)
