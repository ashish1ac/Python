"""
User will give email id: ashishoozone55@gmail.com
We have to print user id and domain name separately
user id: ashishoozone55, domain name: gmail.com
"""

gmail = input("Enter your Gmail: ")

i = gmail.find('@')  # Finding the index of the @

user_id = gmail[0:i:1]  # Split before @
domain_name = gmail[i+1::]  # Split after @

print(f"User id of the gmail is: {user_id} and domain name is: {domain_name}")
