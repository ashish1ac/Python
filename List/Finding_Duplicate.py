"""
Finding the duplicates in an array
Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3]
Explanation: 2 and 3 occur more than once in the given array.

Input: arr[] = [0, 3, 1, 2]
Output: []
Explanation: There is no repeating element in the array, so the output is empty.

Input: arr[] = [2]
Output: []
Explanation: There is single element in the array. Therefore output is empty.
"""

lst = [2]
duplicateLst = []

for x in lst:
    count = 0
    for i in range(len(lst)):
        if x == lst[i]:
            count += 1
    if count > 1 and x not in duplicateLst:
        duplicateLst.append(x)

print(duplicateLst)
