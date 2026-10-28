
# Print sum of first 10 even numbers

numbers = []

for i in range(2, 21, 2): #start from 2 and end at 21 index skipping 1 to get even number
    numbers.append(i)

print("Even numbers:", numbers)
print("Sum of first 10 even numbers:", sum(numbers))
