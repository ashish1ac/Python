"""
User will give the number,
We have to return number of digits in it.
"""

number = int(input("Enter the number: "))
count = 0

if number == 0:
    count = 1

else:
    while number > 0:
        number = number // 10
        count += 1

print("Total number of digits are:", count)
