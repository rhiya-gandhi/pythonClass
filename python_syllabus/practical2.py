#accept 2 values S and N. print square of first N numbers starting from S
S = int(input("enter S: ")) #starting from this number 
N = int(input("enter N: ")) #how many numbers after S
for i in range(S, S + N): #loop starting from S and goes till N
    print (i * i) #square of numbers