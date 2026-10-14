#accept sentence from the user and count the vowels 
vowels = input("enter a sentence: ")

count = 0
for i in vowels:
    if i.lower() in 'aeiou':
        count += 1
print(count)

# print(vowels.count("a") + vowels.count("e") + vowels.count("i") + vowels.count("o") + vowels.count("u"))
# print(vowels.count("A") + vowels.count("E") + vowels.count("I") + vowels.count("O") + vowels.count("U"))
