# Write a program that takes a string as input and counts the number of vowels in the string.

string = input("Enter the string: ")
VOWELS = 'aeiouAEIOU'
count = 0

for ch in string:
    if ch in VOWELS:
        count += 1

print(count)