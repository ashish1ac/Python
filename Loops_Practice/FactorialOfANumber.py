# Write a program that takes an integer N as input and calculates the factorial of N.

n = int(input("Enter the number: "))
fact = 1

if n == 0:
    print('Factorial of 0 is 1')
for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of a number {n} is: ", fact)

