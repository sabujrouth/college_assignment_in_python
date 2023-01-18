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