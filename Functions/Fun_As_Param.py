def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def fun(f, x, y):
    f(x, y)


def display():
    print("Hello")


def meth(d):
    d()


print(meth(display))
print(fun(add, 100, 500))
print(fun(sub, 1000, 500))
