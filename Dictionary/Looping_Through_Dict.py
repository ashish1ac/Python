dict = {
    1: 'Nokia',
    2: 'Target',
    3: 'Amazon',
    4: 'Adobe',
    5: 'Google'
}

print(dict[5])
print(dict.get(5))
print()

# print(dict[6])  # key 6 doesn't exist, it will throw KeyError
print(dict.get(6)) # I won't throw error infact it will say None
print(dict.get(6, 'Apple'))
print()

print("DICT KEYS", dict.keys()) # Return all the keys
print("DICT VALUES", dict.values()) # Return all the values
print("DICT ITEMS:", dict.items()) # Return (K, V) tuple in a list
print()

# Famous way of printing dictionary
for x,y in dict.items():
    print(x, y)

