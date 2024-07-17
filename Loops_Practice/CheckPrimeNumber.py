# Write a program that takes an integer N as input and checks whether N is a prime number.

n = int(input("Enter the number: "))
count = 0

if n == 1:
    print(f"{n} is not a prime number")

if n == 2:
    print(f"{n} is a prime number")
    exit()

if n % 2 == 0:
    print(f"{n} is not a prime number")
    exit()

for i in range(1, n+1):
    if n % i == 0:
        count += 1

    if count == 2:
        print(f"{n} is a prime number")