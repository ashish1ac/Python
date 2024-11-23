"""
Write a function to reverse the string!
"""

s = input("Enter the String: ")
tmp_s = ''

for i in range(len(s), -1):
    tmp_s = tmp_s + s[i]

print(f"Reverse string of {s} is {tmp_s}")