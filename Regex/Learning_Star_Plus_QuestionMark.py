"""
* matches 0 or more repetitions.
+ matches 1 or more repetitions.
? matches 0 or 1 repetition.
"""

import re

pattern = 'ab*c'
text = 'ac abc abbc abbbc'

match = re.findall(pattern, text)
print("If we use '*' =", match)  # It will return this ['ac', 'abc', 'abbc', 'abbbc']

pattern = 'ab+c'
match = re.findall(pattern, text)
print("If we use '+' =", match)  # It will return this ['abc', 'abbc', 'abbbc']

pattern = 'ab?c'
match = re.findall(pattern, text)
print("If we use '+' =", match)  # It will return this ['ac', 'abc']
