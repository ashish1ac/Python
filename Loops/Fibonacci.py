"""
Fibonacci series means the 3 number is the sum of 1 and 2
"""

n = int(input("Enter, how many numbers you want: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
