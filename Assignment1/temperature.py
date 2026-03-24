#formula for ferenite = (celsius * 9/5 )+ 32
#formula for celcius = (ferenite - 32) * 5/9

temp1 = int(input("Enter temp in celcius :"))
fr = (temp1 * 9/5) + 32
print("Temp in ferenite is :", fr)
temp2 = float(input("Enter temp in ferenite :"))
cl = (temp2  - 32) * 5/9
print("Temp in celcius is :", cl)
