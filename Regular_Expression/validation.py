import re

# ---------------- EMAIL VALIDATION ----------------
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    
    if re.fullmatch(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"


# ---------------- MOBILE NUMBER VALIDATION ----------------
def validate_mobile(mobile):
    # Indian mobile number: starts with 6/7/8/9 and total 10 digits
    pattern = r'^[6-9]\d{9}$'
    
    if re.fullmatch(pattern, mobile):
        return "Valid Mobile Number"
    else:
        return "Invalid Mobile Number"


# ---------------- PASSWORD VALIDATION ----------------
def validate_password(password):
    # Rules:
    # At least 8 chars
    # 1 uppercase
    # 1 lowercase
    # 1 digit
    # 1 special char

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.fullmatch(pattern, password):
        return "Valid Password"
    else:
        return "Invalid Password"


# ---------------- MAIN PROGRAM ----------------
email = input("Enter Email: ")
mobile = input("Enter Mobile Number: ")
password = input("Enter Password: ")

print(validate_email(email))
print(validate_mobile(mobile))
print(validate_password(password))