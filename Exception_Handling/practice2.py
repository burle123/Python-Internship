print("Hello, World!")
a =10
b ="two"
try:
    print(a/b)
except TypeError as e:    
# except BaseException as e:            # Use BaseException or Exception if we dontt know the type of error
    print("Error: ", e)
    
print("This is the end of the program.")