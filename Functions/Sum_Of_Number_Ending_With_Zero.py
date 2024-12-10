"""
I will get a list of numbers and I need to find the sum of those numbers who are ending with 0s.
"""


def sumOfZeroNum(numberlist):
    sum = 0
    for i in numberlist:
        if i % 10 == 0:
            sum = sum + i

    return sum


print(sumOfZeroNum([0, 0, 0, -10, 200, 211]))

