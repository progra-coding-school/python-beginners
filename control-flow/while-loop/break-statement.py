# Demo of break statement

count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1  # Increment count in each iteration
print("Loop finished!")

# ---- Explanation----:
# The loop runs as long as count < 10.
# It prints the current value of count.
# When count becomes 5, the if count == 5: condition is true,
# so break exits the loop.
# The loop ends and "Loop finished!" is printed.