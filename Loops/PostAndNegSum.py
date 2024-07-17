"""
User will give some positive numbers and some negative,
We have to return the sum of the numbers separately and show.
"""

numOfTimes = int(input("Tell, how many numbers you want to add: "))
posSum = 0
negSum = 0

while numOfTimes > 0:
    incoming_number = int(input("Enter the number: "))

    if incoming_number > 0:
        posSum = posSum + incoming_number
    else:
        negSum = negSum + incoming_number

    numOfTimes -= 1

print("Positive numbers sum is:", posSum)
print("Negative numbers sum is:", negSum)

