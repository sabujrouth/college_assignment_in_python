# A website requires the users to input username and password to register. Write a program
# to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check
# them according to the above criteria.
import re

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return "Password must be at least 6 characters long"
    elif re.search("[a-z]", password) is None:
        return "Password must contain at least one lowercase letter"
    elif re.search("[A-Z]", password) is None:
        return "Password must contain at least one uppercase letter"
    elif re.search("[0-9]", password) is None:
        return "Password must contain at least one number"
    elif re.search("[!@#\$%^&*()]", password) is None:
        return "Password must contain at least one special character"
    else:
        return "Password is valid"

password = input("Enter your password: ")
print(check_password(password))