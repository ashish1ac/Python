"""
we will get a list with duplicates elements in it,
we need to remove the duplicate elements and add them to a new list.
"""

uniqueList = []
L1 = [1, 2, 3, 4, 5, 6, 3, 4, 9, 9]

for x in L1:
    if x not in uniqueList:
        uniqueList.append(x)

print(uniqueList)