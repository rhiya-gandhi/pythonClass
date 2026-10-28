#empty list
my_list =[]
print(my_list)
#with items
fruits=["banana", "apple","cherry"]
print(fruits)
#to acces the list
numbers=[10,20,40,60]
print(numbers[0]) #first item
print(numbers[-1]) #last item
#append item in the last
list=["red","green","blue"]
list.append("yellow")
print(list)
#insert item at a specific index
list.insert(2,"black")
print("after inserting ",list)
#pop the item 
last_item=list.pop() #pop removes the last item from the list
print("after poping ",list)
#pop item at a specific index
list.pop(2)
print("after poping at index 2 ",list)

#length of the list
number = [11,22,33,4,55,66,67]
print("length of the list is ",len(number))

#ascending order
numberr = [1,2,3,9,8,7,6]
print("ascendig order ", sorted(numberr))

#descending order
print("descending number: ",sorted(numbers,reverse=True))