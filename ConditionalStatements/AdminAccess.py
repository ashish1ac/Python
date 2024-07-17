# Only two people, that is john and smith have admin access, rest are not authorised!

username = input("Enter the name of the person: ")

if username == 'john' or username == 'smith':
    print("You have the admin access!")
else:
    print("You don't have admin access!")
