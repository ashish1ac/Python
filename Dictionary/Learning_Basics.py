dict1 = {'name': 'Ashish', 'age': 26, 'occupation': 'Software Developer', 'company': 'Nokia', 'city': 'Noida'}

list1 = ['A', 'B', 'C', 'D']
list2 = ['Apple', 'Ball', 'Cat']
dict2 = dict(zip(list1, list2))
print("DICT2:", dict2)

# Above thing using Comprehension
dict8 = dict((x,y) for x,y in zip(list1, list2))
print("DICT8: ", dict8)

# Enumerate using Comprehension
listEnu = [100, 200, 300]
dictEnu = {x:y for x,y in enumerate(listEnu)}
print("DICTENU: ", dictEnu)

'''
Dict using enumerate function
dict3 = dict(enumerate(list1))
print("DICT3:", dict3)
'''

'''
Traversing a list!
for i in dict1:
    print(i, ':',  dict1[i])
'''
