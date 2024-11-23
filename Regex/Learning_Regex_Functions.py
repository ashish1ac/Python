"""
In this, we are going to learn the basic function that we need while working with the Regex in Python.
"""
import re

'''------------------------------------------------------------------------------------------------'''
#  re.search(): Search for the first occurrence of the pattern in the string.
matches = re.search("\d+", 'abc123def456')
print("Search function: ", matches)  # <re.Match object; span=(3, 6), match='123'> // this is without group()

matches = re.search("\d+", 'abc123def456')
print("Search function with group: ", matches.group())  # 123 // with using group()

'''------------------------------------------------------------------------------------------------'''
# re.findall(): Return all matches in the string.
matches = re.findall("\d+", 'abc123def456')
print("Findall function: ", matches)  # ['123', '456']

'''------------------------------------------------------------------------------------------------'''
# re.sub(): Substitute all matches with a replacement string.
result = re.sub("\d+", '#', "abc123DEF456")
print("Sub function: ", result)  # abc#DEF#

'''------------------------------------------------------------------------------------------------'''
# re.split(): Split the string by the occurrences of the pattern.
parts = re.split("\d+", 'abc123DEF456')
print("Split function: ", parts)  # ['abc', 'DEF', '']

'''------------------------------------------------------------------------------------------------'''
# re.match(): Determine if the pattern matches at the beginning of the string.
match = re.match("\d+", 'abc123DEF456')
print("Match function: ", match)  # None

match = re.match("\d+", '123DEF456')
print("Match function: ", match.group())  # 123
