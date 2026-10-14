#read a file and count vowels in file 
with open ("myfile.txt", "r") as f:
    content = f.read()
    vowels = 'aeiou'
    count = 0
    for i in content:
        if i in vowels:
            count+=1
    print(content)
    print("vowels: ",count)