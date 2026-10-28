# Write a program to:
# 1. Print the student's name using .get().
# 2. Print the student's grade using .get("grade", "Not assigned").
# 3. Loop through the dictionary and print each key and value.

student = {
    "name": "Riya",
    "age": 21,
    "marks": 78
}
print(student.get("name"))
print(student.get("grade", "not assigned"))
for key, value in student.items():
    print(key , value)
