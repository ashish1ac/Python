# Return the digits of the number

number = int(input("Enter the number: "))

while number > 0:
    digit = number % 10  # Modulus gives the last part of the number
    print(digit)  # Divide gives the first part of the number
    number = number // 10





