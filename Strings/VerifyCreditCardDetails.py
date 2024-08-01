"""
Take the credit card number from the user,
Verify it is 16 digits,
Display the credit card number like this: **** **** **** 4321
"""

credit_number = input("Enter the credit card number: ")

last_four_numbers = credit_number[15::]  # Got the last 4 credit card numbers

stars = (4 * "*") + ' '  # create this pattern "**** "

secure_credit_number = (stars * 3) + last_four_numbers  # Concatenate the pattern with last 4 numbers

print(secure_credit_number)
