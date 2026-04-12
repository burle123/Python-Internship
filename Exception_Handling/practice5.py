# try , except , else and finally

try:
    x= int(input("Enter a number: "))
    y= int(input("Enter another number: ")) # If we enter 0
    print("Hello, World!")
    print(x/y)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    
else:
    print("No error occurred.")    # This block will execute only if there is no error in the try block.
finally:
    print("This will always execute.")