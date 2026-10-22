#count how many names start with vowel
with open ("names.txt", "r")as f:
    nm = f.readlines()
    vowel = 'aeiou'
    count = 0
    for name in nm:
        if name and name[0].lower() in vowel:
            count +=1
            print("names that starts with vowels:", count)