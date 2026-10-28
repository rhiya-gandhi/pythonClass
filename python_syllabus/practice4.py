# Fibonacci generator + next()
# Write a generator function that produces Fibonacci numbers.
# - Start with a = 0 and b = 1.
# - Use yield to return one number at a time.
# - Use next() inside a loop to print the first 8 Fibonacci numbers.
# - Do not use input().
def fibonacci():
    a,b = 0, 1
    while True:
        yield a
        a , b = b , a+b
gen = fibonacci() 
for _ in range (8):
    print(next(gen))
