"""
Program will guess one number randomly in between 0 and 10 using random method,
Now, we have to guess that number, by telling user that if random number is more
than what you entered, increase your number and vice-versa.
"""

import random

guess_n = random.randint(1, 10)
user_n = 0

while guess_n != user_n:
    user_n = int(input("Enter the number: "))
    if user_n > guess_n:
        print("Guess number is lesser!, decrease your number")
    elif user_n < guess_n:
        print("Guess number is higher!, increase your number")
    else:
        print("You have guessed the number: ", "Guess No:", guess_n, "Your No:", user_n)

