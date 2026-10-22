# Count the frequency of each name using a dictionary
with open ("names.txt", "r") as f:
    nm = [name.strip() for name in f]
    frequency = {}
    for name in nm:
        if name in frequency:
            frequency[name] += 1
        else:
            frequency[name] = 1
print(frequency)