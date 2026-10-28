#create a list of 10 numbers and display the sum of last 4 elements
#remove the items from the list located at 2nd and 5th position 
#print the difference between the highest and smallest number of the list
#append a new element in the list which is half of the item located in the 3rd position


number = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1]
print("sum of last 4 elements is ", sum(number[-4:]))
out = (number.pop(2))

# del number[1]
# del number[4]
print(number)
print(max(number)-min(number))
number.append(2/2)
print(number)
