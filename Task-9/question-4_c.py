# 4. Write a python function to validate the Regular Expression for the following:
# c. Telephone numbers of USA

import re

phone_number = input("Enter Phone Number:")

"""\s - Matches any whitespace
eg: +1 202 555 0118
First is a 1: the “country code” covering the US.
Second is a 3-digit area code.
Finally, there’s a 7-digit local number."""

pattern = ("^1\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}$")

if re.search(pattern,phone_number):
    print("It's a valid Phone Number")
else:
    print("Invalid Phone Number")