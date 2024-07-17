"""
Learning, how "break" keyword works in python 
"""

while True:
    n = int(input("Enter the number: "))

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Going to break this loop")
        break
