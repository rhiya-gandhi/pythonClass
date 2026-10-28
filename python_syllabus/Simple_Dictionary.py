# ## Simple Dictionary 
# my_dict = { "name": "Jay", "age": 25, "city": "Pune"} 
# print("Name ", my_dict["name"]  )     
# print(my_dict.get("age") )
# for key in my_dict: 
#     print(key, my_dict[key]) 
# for key, value in my_dict.items():     
#     print(key, value)
# for value in my_dict.values(): #  
#     print(value)

students = {
    101: {"name":"Rhiya", "age": 21,"score":[20,30,40]},
    102: {"name":"jiya", "age": 20,"score":[40,60,40]}
}
for sid, details in students.items():
    avg = sum(details["score"]) / len(details["score"]) 
    passed = avg > 20
    print(details["name"],"average" , avg,"passed" if passed else "fail")