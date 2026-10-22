# Question 8: String analysis
# For each name, print its length, first character, last character, and whether it is a palindrome.
with open ("names.txt", "r") as f:
    nm = [name.strip() for name in f]
    for name in nm:
        print("name- ", name)
        print("length ",len(name), "1st letter-",name[0], "lastletter - ", name[-1])
        if name.lower() == name[::-1].lower():
            print("yes it is palindrom")
        else:
            print("no not a palindrom")