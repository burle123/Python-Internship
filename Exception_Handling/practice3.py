# Multiple Exceptions in a single try block

try:
    x= int(input("Enter a number: "))
    y= int(input("Enter another number: "))
    print("Hello, World!")
    print(x/y)
except (ZeroDivisionError, TypeError, BaseException) as e:
    print("Error: ", e)
