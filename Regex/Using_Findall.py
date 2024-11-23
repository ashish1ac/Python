import re

pattern = r'a.c'
text = 'abc aac adc a/c axx'

matches = re.findall(pattern, text)
print(matches)

# It will return all the pattern which are matching in the given string.
# Here o/p: ['abc', 'aac', 'adc', 'a/c'] it leave axx because it's not matching the pattern.
