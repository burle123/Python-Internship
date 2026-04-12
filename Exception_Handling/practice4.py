#Why we dont use if else for error handling
# --> We use try except block for error handling because it allows us to handle exceptions gracefully without crashing.

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if y == 0:
    print("Error: Division by zero is not allowed.")
else:
    print(x/y)

# n no of time the code will run through else block but if we use try except block then it will only run when there is an error and it will not run when there is no error.    

