#  Accept the principal, rate, and time to calculate and display simple interest.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: {simple_interest}")
