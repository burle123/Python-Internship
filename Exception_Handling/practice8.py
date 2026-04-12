#User define exception define class and raise exception
# Example - Matrimony Eligibility

class MatrimonyEligibilityError(Exception):
    def __init__(self, message="You are not eligible for matrimony."):
        self.message = message
        super().__init__(self.message)

# def check_matrimony_eligibility(age):
#     if age < 20:
#         raise MatrimonyEligibilityError(f"Age {age} is below the legal age for matrimony. {MatrimonyEligibilityError().message}")
#     else:
#         print("You are eligible for matrimony.")

class TooOld(MatrimonyEligibilityError):
    def __init__(self, message="You are too old for matrimony."):
        self.message = message
        super().__init__(self.message)

class TooYoung(MatrimonyEligibilityError):
    def __init__(self, message="You are too young for matrimony."):
        self.message = message
        super().__init__(self.message)

age = int(input("Enter your age: "))

if age < 20:
    raise TooYoung(f"Age {age} is below the legal age for matrimony. {TooYoung().message}")
elif age > 60:
    raise TooOld(f"Age {age} is above the legal age for matrimony. {TooOld().message}")
else:
    print("You are eligible for matrimony.")
