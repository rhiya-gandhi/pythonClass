# Print names containing the letter "a"
with open ("names.txt","r") as f:
    nm = [name.strip() for name in f]
    for name in nm:
        if "a" in name.lower():
            print(name)