# Write a program that takes an integer N as input and calculates the sum of its digits.

n = int(input("Enter the number: "))
real_number = n
add = 0

while n > 0:
    digit = n % 10
    add = add + digit
    n = n // 10

print(f"Sum of these numbers {real_number} is:", add)