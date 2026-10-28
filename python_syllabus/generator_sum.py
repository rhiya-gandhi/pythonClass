# Calculate sum of squares without creating a list

total = sum(x * x for x in range (3))
print (total)

numbers = range (1, 10)
print(list(numbers))

print("i in steps of 3")
for i in range (2,10,2):
    print(i)

#print sum of 1st n numbers 
n = int(input("enter the n"))
total = 0
for i in range (1 ,n+1):
    total += i
print(total)
