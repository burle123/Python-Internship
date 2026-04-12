# Real Implementation of Exception Handling

# Example

# Read the file

try:
    with open("Exception_Handling/abc.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
else:
    print("File read successfully.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")    
