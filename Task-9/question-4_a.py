# 4. Write a python function to validate the Regular Expression for the following:
# a. Email Address

import re

email = input("Enter Email address:")

"""
^        Match the start of a string
.            Match any character except newline
$            Match the end of a string
+            Match 1 or more repetitions
2            max. character"""

pattern = "^[a-zA-Z0-9.@#$%^&*_-]+@[a-zA-Z]+.[a-zA-Z]{2,}$"

if re.search(pattern,email):
    print("It's a valid email")
else:
    print("It's not a valid email")