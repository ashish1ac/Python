#  Here we want only positive result like 20 - 5 = 15 not 5 - 20 = -15

number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
difference = number1 - number2

if difference > 0:
    print("Difference is:", difference)
else:
    print("Difference is:", -difference)

