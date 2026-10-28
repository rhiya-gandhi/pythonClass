# Only **kwargs: accepts any number of keyword arguments
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Maya", age=25)
# The names args and kwargs are conventions; 
# the * and ** are what make them collect the arguments.

# So, * means “collect extra values given without names,” 
# while ** means “collect extra values given with names.”

