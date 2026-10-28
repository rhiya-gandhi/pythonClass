# for i in range(1, 8):
#     if i == 3:
#         continue
#     if i == 6:
#         break
#     print(i)

# Pass the string "programming" directly into a variable.

# Write a program to print:
# 1. The first four characters.
# 2. Every alternate character starting from index 1.
# 3. The string in reverse using reversed() and .join().

s = "programming"
print(s[:4])
print(s[1::2])
print("".join(reversed(s)))