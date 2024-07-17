"""
User will tell how many number he will enter,
We have to return the sum of all the numbers he entered.
"""

number = int(input("Tell, how many numbers you want to enter: "))
total = 0

while number > 0:
    incoming_number = int(input("Enter the number: "))
    total = total + incoming_number
    number -= 1

print("Sum of all the numbers is:", total)
