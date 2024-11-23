def add():
    print("I am running!")


def addDefaultArgs(a, b=0, c=0):
    return a + b + c


def variableArgs(*args):
    print(args)


def variableMandatoryArgs(a, b, *args):
    print(a, b, args)


"""
This is wrong because: non-default parameter follows default parameter, default parameter should always be on the right!
def addDefaultOnRight(a = 10, b, c):
    return a + b + c
"""

print(add())  # Even though we didn't add the return in the function, but it will return None for sure while calling.
print(addDefaultArgs(1.5, 2, 10))  # c values is taken 0 as its default value.
# print(addDefaultArgs(b= 10, c = 20, 10))  This will throw an error because positional args should be in the starting.
print(variableMandatoryArgs(a=10, b=20))
