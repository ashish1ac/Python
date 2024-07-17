"""
User will give any number n,
we need to tell the factors of the number.

Logic will be,
Number divided by any number if it's completely divisible that number is its factor,
1 and that number itself are the factor of that number
"""

n = int(input("Enter the number: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)
