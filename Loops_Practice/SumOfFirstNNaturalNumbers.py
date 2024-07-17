# Write a program that takes an integer N as input and calculates the sum of the first N natural numbers.

n = int(input("Enter the number till where you want the sum: "))
su = 0
for i in range(1, n + 1):
    su = su + i

print(f"Sum of {n} numbers is:", su)
