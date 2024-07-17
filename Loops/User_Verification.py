"""
If user is entering a positive number say, valid input,
else say invalid input. (For char or string also print it's invalid
"""

while True:
    user_input = input("Enter the positive number (or 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    if not user_input.isdigit() or int(user_input) <= 0:
        print("Invalid Input")
        continue

    print("Valid Input")
