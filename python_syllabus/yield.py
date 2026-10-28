def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
n = int(input("enter the count upto you want to count"))
for num in count_up_to(n):
    print(num)