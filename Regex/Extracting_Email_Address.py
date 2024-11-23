"""
Extracting the Email Addresses from the given string.
"""
import re

string = "Contact us at support@example.com or sales@example.org."
email = re.findall("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", string)
print(email)

