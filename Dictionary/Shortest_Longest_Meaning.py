dct = {
    'A': 'aaaaaaaaaaaaa',
    'B': 'bbbbbbbbbbb',
    'C': 'ccccccccc',
    'D': 'ddddddd',
    'E': 'eeeee'
}

keysList = list(dct.keys())
valuesList = list(dct.values())

valueSize = [len(x) for x in dct.values()]

max = max(valueSize)
min = min(valueSize)

max_index = valueSize.index(max)
min_index = valueSize.index(min)

print(f"Max meaning is of letter {keysList[max_index]} and the meaning is {valuesList[max_index]}")
print(f"Min meaning is of letter {keysList[min_index]} and the meaning is {valuesList[min_index]}")
