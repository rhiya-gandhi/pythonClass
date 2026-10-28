# Only *args: accepts any number of positional arguments
def add_all(*args):
    return sum(args)

print(add_all(2, 3, 5))  # 10