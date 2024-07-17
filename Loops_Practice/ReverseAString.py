# Write a program that takes a string as input and prints the string in reverse order.

seq = input("Enter the string: ")
reversed_str = ''

for c in seq:
    reversed_str = c + reversed_str

print(reversed_str)
