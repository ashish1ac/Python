"""
User will enter the pass and confirm pass, and then we have to verify whether both the pass and verify pass are 
correct or not, if both the pass are same but only difference is in their caps then tell user, please verify your caps.
"""

pwd = input("Enter the Password: ")
verpwd = input("Re-enter your Password: ")

if pwd == verpwd:
    print("You have entered the correct password!")

elif pwd.casefold() == verpwd.casefold():  # Here, we are checking the mis-capping of Passwords
    print("Please check your caps!")

else:
    print("You have entered incorrect password!")

