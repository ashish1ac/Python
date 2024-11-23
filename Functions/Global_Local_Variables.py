"""Learning global and local variables"""
g = 100


def fun(a, b):
    g = 1000
    c = a + b
    print("LOCAL VAR:", c)
    print("GLOBAL VAR:", g)
    print("GLOBAL VAR:", x)


x = 200
fun(10, 20)
print(g)

# If we define a variable below the calling of function then the function won't be able to access it and throws error.
# If we want a function to modify the value of global variable then use global keyword inside the function for global variable.
print(globals())
print(locals())
