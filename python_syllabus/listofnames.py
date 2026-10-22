with open ("names.txt" , "r") as f:
    nm = f.readlines()
    nm = [i.strip() for i in nm]
    print ("list of names: ", nm)