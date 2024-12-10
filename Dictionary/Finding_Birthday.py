birthdays = {
    'Ashish': "22/05/1998",
    'Robin': "29/09/2000",
    'Vanshika': "14/11/2008",
    'Anshika': "28/04/2016"
}

name = input("Enter the name: ")

if name in birthdays:
    print(f"{name} birthday is on {birthdays[name]}")
else:
    print("Person not found!")
