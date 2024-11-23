""" 
Need to find the occurrence of each item in the given list.
"""

lst = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']
traversedLst = []

for x in lst:
    if x not in traversedLst:
        traversedLst.append(x)
        count = 0
        for y in lst:
            if x == y:
               count += 1
        print(f"{x}: {count}")
