"""
Write a program of zero division error and explaining the nested try except
"""

try:
    a = int(input("Enter the numerator: "))
    try:
        b = int(input("Enter the denominator: "))
        try:
            c = a // b
            print(c)
        except ZeroDivisionError as msg:
            print("Zero Division Error: ", msg)
    except ValueError as msg:
        print("Value error in denominator: ", msg)
except ValueError as msg:
    print("Value error in numerator: ", msg)

print('1' == 1)
