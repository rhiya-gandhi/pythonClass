#read a file split contents in words and store in list
#1- print total no. of words
#2- print unique words

with open("myfile.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Total number of words:", len(words))


    unique_words = set(words)
    print("Unique words:", unique_words)
