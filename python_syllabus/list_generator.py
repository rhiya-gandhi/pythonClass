list_demo = [x * x for x in range(6)]
print (list_demo)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))


# List: [ ]
# Makes all the results immediately and keeps them in memory.

# [0, 1, 4, 9, 16]

# Generator: ( )
# Produces results one at a time when requested, instead of storing the entire result list.

# 0 → 1 → 4 → 9 → 16
def even(limit):
    for n in range(0, limit+1 , 2):
        yield n
print(list(even(10)))

#countdown
def countdown(n):
    while n > 0:
        yield n
        n -= 1
print(list(countdown(5)))

#squares upto 
def squares(limit):
    n = 1 
    while n * n <= limit:
        yield n * n 
        n += 1
print(list(squares(50)))


