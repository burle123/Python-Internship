f1 = open('File_Handling/arnold.jpg', 'rb')  # open the file in binary mode
content = f1.read()  # read the content of the file
print("Data read Successfully.")
f1.close()