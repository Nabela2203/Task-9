# 4. Write a python function to validate the Regular Expression for the following:
# b. Mobile numbers of Bangaladesh

import re

mobile_number = input("Enter Mobile Number:")

"""\s - Matches any whitespace
eg: 880 1050 694200"""

pattern = "^880\s[1][0-9]{3}\s[0-9]{6}$"

if re.search(pattern,mobile_number):
    print("It's a valid Mobile Number")
else:
    print("Invalid Mobile Number")