# Step 0: Two 2-digit numbers
num1 = 47
num2 = 58

# Step 1: Extract ones (units) digits
ones1 = num1 % 10
ones2 = num2 % 10

# Step 2: Add ones digits
ones_sum = ones1 + ones2

# Step 3: Calculate carry and final ones digit
carry = ones_sum // 10
final_ones = ones_sum % 10

# Step 4: Extract tens digits
tens1 = num1 // 10
tens2 = num2 // 10

# Step 5: Add tens digits + carry
tens_sum = tens1 + tens2 + carry

# Step 6: Combine tens and ones
total = (tens_sum * 10) + final_ones

print("Sum =", total)
