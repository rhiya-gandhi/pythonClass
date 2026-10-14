#read all lines into a list , print tot of lines , display 2nd and 4th line
with open ("myfile.txt","r") as f:
    content = f.readlines()
    print("total number of line: ", len(content))
    if len(content)<=5:
        print("2nd line is : ", content[1].strip())
        print("4th line is : ", content[3].strip())
