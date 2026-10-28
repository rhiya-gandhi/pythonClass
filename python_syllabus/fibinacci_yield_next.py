#A Fibonacci series is a sequence of numbers 
# where each new number is the sum of the previous two numbers.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a , b = b , a + b   
# yield returns one value at a time and pauses the function.
gen = fibonacci() #This creates a generator object.
for _ in range(10): #_ is a variable used when you don't need the loop counter.
    #_ you want to repeat something n times
    print(next(gen)) #asks the generator for its next value.
