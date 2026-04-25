import re 
# email = "burleshantanu@gmail.com"
email = input("Enter an email address: ")

if re.fullmatch(r"\w+@\w+\.\w+", email):
    print("Valid email address.")
else:
    print("Invalid email address.")
