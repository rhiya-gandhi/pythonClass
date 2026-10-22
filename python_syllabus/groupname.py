with open ("names.txt", "r") as f:
    nm = f.read().splitlines()
groups = {}
for name in nm:
    if name:
        letter = name[0].upper()
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(name)
for letter in groups:
    with open (letter + "_names.txt", "w") as f:
        for name in groups[letter]:
            f.write(name + "\n")
print(groups)
