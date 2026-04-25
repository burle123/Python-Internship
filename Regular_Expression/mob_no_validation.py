import re 

mob_no = input("Enter a mobile number: ")

if re.fullmatch(r"\d{10}",mob_no):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")