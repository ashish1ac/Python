import re

pattern = r"^abc"
text = "abcdef"

match = re.match(pattern, text)
print(match)

pattern = r"def$"
match = re.match(pattern, text)
print(match)

# pattern = r"^abc"
# text = "abcdef"
# match = re.match(pattern, text)
# print(match)  # Matches "abc" only if it's at the start

# pattern = r"def$"
# match = re.search(pattern, text)
# print(match)  # Matches "def" only if it's at the end

'''
In this case, if you will use re.search then it will give different result than using re.match.
'''
