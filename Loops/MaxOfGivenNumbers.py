"""
First, will ask user how many numbers you want to give
Take, all the numbers,
Out of those numbers, we have to return the Max one
"""

numOfTimes = int(input("Tell, how many numbers you want to give: "))
max_number = None  # if it's 0 then it won't work for negative numbers because 0 is larger than negative numbers

while numOfTimes > 0:
    incoming_number = int(input("Enter the number: "))

    if max_number is None or incoming_number > max_number:
        max_number = incoming_number

    numOfTimes -= 1

print("Maximum number is: ", max_number)
