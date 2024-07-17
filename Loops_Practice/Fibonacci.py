# Write a program that takes an integer N as input and prints the first N terms of the Fibonacci sequence.
# 0 1 1 2 3 5 8

n = int(input("Enter the Nth number: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
