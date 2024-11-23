"""
we will get a list with duplicates elements in it,
we need to remove the duplicate elements in the same list.
"""

nList = [0, 0, 1, 1, 1, 2, 3, 3, 5, 7]
l = 1

for r in range(1, len(nList)):
    if nList[r] != nList[r - 1]:
        nList[l] = nList[r]
        l += 1
print(l)
