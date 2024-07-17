# String can be multiplied just like they can be added
name = 'Hello '
name *= 2
print(name)

name *= True  # Here True means 1
print(name)

name *= False  # Here False means 0, so it won't return 0 but an empty string
print(type(name))
