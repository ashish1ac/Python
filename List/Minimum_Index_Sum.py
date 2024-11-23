"""
fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

find out the item which both like based on their priority.
"""

fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

indexList = []
for i in range(len(fav1)):
    for j in range(len(fav2)):
        if fav1[i] == fav2[j]:
            indexList.append(i+j)

print(indexList)
item = min(indexList)
print(fav1[item -1])