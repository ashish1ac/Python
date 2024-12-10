import math
a = 0.2 + 0.1
b = 0.3

print(a == b)  # This supposed to be return true, but it's false because a = 0.3000....4 not exactly 0.3

print(math.isclose(a, b))  # This will return true

