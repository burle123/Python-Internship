import re
text = "Hello World"

# match the word "Hello"
match = re.match(r"Hello", text)
if match:
    print("Match found:", match.group())  #group() returns the matched string
else:
    print("No match found.")   

# search for the word "World"
search = re.search(r"World", text)
if search:
    print("Search found:", search.group())
else:
    print("No search found.")

# find digits in the text
text1 = "Shantanu12345"
# find_all = re.findall(r"\d", text1)  # \d matches a single digit
find_all = re.findall(r"\d+", text1)  # \d+ matches one or more digits
print("Digits found:", find_all)

# finditer - Returns match objects with positions.

find_iter = re.finditer(r"\d+", text1)
for match in find_iter:
    print(match.group(),match.start(), match.end())  # group() returns the matched string, start() and end() return the positions of the match

# split the text by whitespace
split_text = re.split(r"\s", text)
print("Split text:", split_text)

# replace/substitute "World" with "Universe"
replaced_text = re.sub(r"World", "Universe", text)
print("Replaced text:", replaced_text)

