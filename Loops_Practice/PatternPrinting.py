"""
Write a program that takes an integer N as input and prints a pattern of stars,
in the form of a right-angled triangle. For example, if N = 4:

*
* *
* * *
* * * *

"""
n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     for j in range(i):
#         print("* ", end='')
#     print('')

for i in range(1, n + 1):
    print("* " * i)