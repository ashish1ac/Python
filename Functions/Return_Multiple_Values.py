def fun(a, b, c):
    return a+1, b+1, c+1


"We can take the values in 3 different variables"
x, y, z = fun(10,20, 30)
print(x, y, z)

"We can take it in a single variable but that will be of tuple type"
t = fun(11, 22, 33)
print(t, type(t))

