"""
User will give some number like 1234,
We have give the sum by adding all the digits of the number
"""

number = int(input("Enter the number: "))
count = 0

while number > 0:
    digit = number % 10
    count = count + digit  # count += number
    number = number // 10

print("Sum of the number is:", count)


