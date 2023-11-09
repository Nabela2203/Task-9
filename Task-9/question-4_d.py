# 4. Write a python function to validate the Regular Expression for the following:
# d . 16 character Alpha-numeric password composed of alphabets of Upper case, Lower case, special characters and numbers.

"""
Lookbehind assertion: (?<=...), (?<!...)

Lookahead assertion: (?=...), (?!...)

pswd - positive lookahead - (?=...)
*    - Match or more repetitions
.    - Match any character except newline
"""

import re

password = input("Enter Password:")

pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{16}$"

if re.search(pattern,password):
    print("It's a valid password")
else:
    print("Invalid password")