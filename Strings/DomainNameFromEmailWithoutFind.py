"""
User will give email id: ashishoozone55@gmail.com
We have to print user id and domain name separately
user id: ashishoozone55, domain name: gmail.com without using find method of the python.
"""

email = input("Enter the email: ")
count = 0

for i in email:  # Here I found the index of '@'
    count += 1
    if i == '@':
        break

user_id = email[0:count-1:1]  # Split string before '@' which is eventually the user_id
print(f"User ID: {user_id}")

domain_name = email[count::]  # Split string after '@' which is eventually the domain_name
print(f"Domain Name: {domain_name}")