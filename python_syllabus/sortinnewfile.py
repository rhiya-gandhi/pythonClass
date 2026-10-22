with open ("names.txt", "r") as f:
    nm = f.read().splitlines()
unique = list((set(nm)))
unique.sort(key = len)

with open ("processed.txt", "w") as f:
    for name in unique:
        f.write(name + "\n")
    print("completed")