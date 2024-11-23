"""
If matrix is given as this
m = [1, 2, 3, 4]
    [1, 2, 3, 4]
    [1, 2, 3, 4]

TRANSPOSE OF A MATRIX WILL BE LIKE THIS
m = [1, 1, 1]
    [2, 2, 2]
    [3, 3, 3]
    [4, 4, 4]

Row become columns and vice-versa
"""

mtx = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
lst = []
for i in range(len(mtx)):
    localLst = []
    for j in range(0, len(mtx[0]) - 1):
        localLst.append(mtx[j][i])
    lst.append(localLst)

print(lst)




