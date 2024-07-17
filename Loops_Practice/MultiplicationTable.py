# Write a program that takes an integer N as input and prints the multiplication table for N up to 10.

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print('', end='')
    for j in range(1, 11):
        print(i*j)
