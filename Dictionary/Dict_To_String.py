"""
dict = {
    'A': 5,
    'B': 3,
    'C': 1,
    'D': 6
}

o/p: A5B3C1D6
"""
dct = {
    'A': 5,
    'B': 3,
    'C': 1,
    'D': 6
}

for i in dct:
    print(str(i) + str(dct[i]), end='')


