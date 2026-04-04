#Theory -Notes

# File Extensions: eg .txt, .csv, .json, .xml, .html, .py, .java, .cpp, .docx, .xlsx, .pdf, etc

# Structured vs Semi-Structured vs Unstructured Data:
# 1. Structured Data: This type of data is organized in a predefined manner, often in rows and columns, making it easy to search and analyze. Examples include data stored in relational databases, spreadsheets, and CSV files.
# 2. Semi-Structured Data: This type of data does not have a strict structure but still contains some organizational properties that make it easier to analyze than unstructured data. Examples include JSON, XML, and HTML files.
# 3. Unstructured Data: This type of data does not have a predefined format or structure, making it more challenging to analyze. Examples include text documents, images, videos, and audio files.


# File handling is a crucial aspect of programming that allows us to read from and write to files on our computer. In Python, we can use the built-in `open()` function to work with files.
# The `open()` function takes two arguments: the name of the file and the mode in which we want to open it. The mode can be 'r' for reading, 'w' for writing (which will overwrite the file if it already exists), 'a' for appending (which will add to the end of the file), and 'x' for creating a new file (which will raise an error if the file already exists).


# Here are some common file handling operations in Python:
# 1. Opening a file 
# 2. Reading from a file
# 3. Writing to a file 
# 4. Closing a file

# Operations: read, write, append, create, delete, rename, move, copy, etc

# modes: 'r' (read), 'w' (write), 'a' (append), 'x' (create), 'b' (binary), 't' (text), r+ (read and write), w+ (write and read), a+ (append and read)

# Syntax for opening a file:
# file = open('filename', 'mode')

# Example:

# with open('example.txt', 'w') as f:
#     f.read()
#     f.write('Hello, World!')
#     f.close()