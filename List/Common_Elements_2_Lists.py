list1 = [10, 15, 6, 9, 12, 8, 4]
list2 = [14, 6, 19, 4, 7, 10, 11]
commonList = []

'''
O(n^2)
for x in list1:
    for y in list2:
        if x == y:
            commonList.append(x)
'''
# O(n) Solution
for x in list1:
    if x in list2:
        commonList.append(x)

print(commonList)
