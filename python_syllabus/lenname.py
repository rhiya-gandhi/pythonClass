with open ("names.txt", "r") as f:
    nm = f.readlines()
    nm = [name.strip() for name in nm]
    for name in nm:
        if len(name) > 5:
            print("names longer than 5 ch", name)