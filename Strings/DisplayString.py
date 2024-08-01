"""
User will give name of the item and the price of it.
We have to display the string in this format: (item_name.....price) make sure this whole length is equal to the 25.
"""

item = input("Enter the item name: ")
price = input("Enter the price for the item: ")

total_length = len(item) + len(price)  # Get the total length of both the strings
dot_length = 25 - total_length  # Get how many dots we need to add

print(item + '.' * dot_length + price)
