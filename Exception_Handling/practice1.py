print("Hello, World!")
a =10
b =0
try:
    print(a/b)
# except ZeroDivisionError:
except Exception as e:
    # print("Error: Division by zero is not allowed.")
    print("Error: ", e)
    
print("This is the end of the program.")