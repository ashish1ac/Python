import re

pattern = r'abc'
text = 'abcdef'

matches = re.search(pattern, text)
print(matches)

# If pattern matches the text then it will return "match' else None
# o/p will be like this: <re.Match object; span=(0, 3), match='abc'>

pattern = '[a-zA-Z]'
text = 'abc 123 XYX'

matches = re.findall(pattern, text)
print(matches)  #  ['a', 'b', 'c', 'X', 'Y', 'X']  we will get everything in btw a-z and A-Z.

pattern = '[^0-9]'
text = 'abc 12345 ABCD @/}{'

matches = re.findall(pattern, text)
print(matches)
# ['a', 'b', 'c', ' ', ' ', 'A', 'B', 'C', 'D', ' ', '@', '/', '}', '{'] we'll get everything except 0-9 including
# space.
