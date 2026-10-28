# Write a program that:
# 1. Uses a for loop to go through the numbers from 0 to 9.
# 2. Skips index 2 using continue.
# 3. Stops the loop when the index reaches 8 using break.
# 4. Prints the character at each remaining index.
# 5. Prints the reverse of the full string using slicing.

word = "abcdefghij"

for i in range (10):
    if i == 2:
        continue
    if i == 8:
        break
    print(word[i])
print(word[::-1])
