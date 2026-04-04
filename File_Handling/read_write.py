# with open('File_Handling/example3.txt.txt', 'r+') as f:  
#     data = f.write(" Students arwe learning how to read and write files in Python.")
#     content = f.read()                          # error : File is not present in the directory
#     print ("Data written to this file:", data)
#     print("Data read from this file :", content)



with open('File_Handling/example3.txt', 'w+') as f:  
    data = f.write(" Students arwe learning how to read and write files in Python.")
    content = f.read()                          # error : File is not present in the directory
    print ("Data written to this file:", data)
    print ("Data read from this file :", content)  