"""
i/p: dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
o/p: newDict = {10: 'a', 20: 'b', 30: 'c', 40: 'd'}
"""

"""
This is the shortest way of doing it actually.
newDct =dict(zip(dct.values(), dct.keys()))
print("Inverted Dict", newDct)
"""


def invertDct(d):
    newDict = {}
    for i in d:
        newDict[d[i]] = i

    return newDict


d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(f"The inverted dict of {d} is {invertDct(d)}")
