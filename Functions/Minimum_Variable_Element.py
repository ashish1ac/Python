"""
There can be any number of args
argument = (1, 5, -5, 10) -> min = -5
argument = (1, 5, 2, -5, 10, low_limit = 2 -> min = 5
"""


def minimum(*num, low_limit=None):
    if low_limit is None:
        numList = list(num)  # First list of num with low_limit
        minm = numList[0]
        for i in numList:
            if i < minm:
                minm = i
    else:
        numList = [x for x in num if x > low_limit]  # Second list of num who are greater than low_limit
        minm = numList[0]
        for i in numList:
            if i < minm:
                minm = i

    return minm


def optimisedMinimum(*num, low_limit = None):
    minm = None

    for x in num:
        if low_limit is not None and x <= low_limit:  # Ignoring all the values that are lesser than low_limit
            continue
        if minm is None or x < minm:  # Whatever is less than minm It will come and get stores in minm
            minm = x

        return minm


print(minimum(1, 5, 2, -5, 10, low_limit=0))
print(optimisedMinimum(1,2,3))

