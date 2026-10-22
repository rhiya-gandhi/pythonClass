#Sort names alphabetically in ascending order
# Read names from the file
with open ("names.txt", "r") as f:
    nm = [name.strip() for name in f]
# Sort names alphabetically
nm.sort()
# Print the sorted names
for name in nm:
    print(name)