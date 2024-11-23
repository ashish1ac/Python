dict1 = {
    1: 'Nokia',
    2: 'Target',
    3: 'Adobe',
    4: 'Amazon',
    5: 'Google'
}

dict2 = dict1.copy()
print("COPY Method, DICT2:", dict2)
print()

dict2.update({6: 'Apple', 7: 'Tesla'})
print("UPDATE Method, DICT2:", dict2)
print()

print("GET Method:", dict2.get(10, 'Oppo'))  # It won't add this key-value of it's not there
print("SetDefault Method:", dict2.setdefault(9, 'Samsung'))  # It will add this key-value if it's not there.
print(dict2)
print()

# Remove Methods
print("POP Method:", dict1.pop(1))
print("POP Method:", dict1.pop(1, 'None'))
print()

print("POP ITEM:", dict2.popitem())
print("POP ITEM:", dict2.popitem())

for x in enumerate(range(2)):
    print("ENUMERATE:", x)

z = {
    2: 6,
    3: 9,
    5: 10
}
z.pop(2)
print(z)

