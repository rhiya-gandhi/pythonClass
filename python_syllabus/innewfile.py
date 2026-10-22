with open ("names.txt", "r") as f:
    nm = f.readlines()
    nm = [name.strip() for name in nm]
filtered = []
for name in nm:
    if len(name) > 5:
        filtered.append(name)

with open ("longname.txt","w") as f:
    for name in filtered:
        f.write(name + "\n")
            
print("filtered name saved")