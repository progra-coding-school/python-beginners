# Demo of continue statement

count = 0
while count < 10:
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1
print("Loop finished!")

# ---- Explanation----:
# The loop runs while count is less than 10.
# When count reaches 5, continue is used to skip print(count).
# It still increments count so the loop doesn't get stuck.
# So 5 is not printed, and the rest of the numbers are.