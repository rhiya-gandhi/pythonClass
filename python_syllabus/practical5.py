#remove the duplicates from list
lst = [1,2,3,4,4,5,5,6,6,7,7,7,7]

# print(list(set(lst))) -- one liner using set that removes duplicates 

new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
