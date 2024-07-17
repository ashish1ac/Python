"""
Any number who has only 2 factors that is 1 and that number itself.
"""

n = int(input("Enter the number: "))
count = 0

for i in range(1, int((n + 1) * 0.5)):
    if n % i == 0:
        count += 1

if count > 2:
    print(f"{n} is not a prime number!")
else:
    print(f"{n} is a prime number!")