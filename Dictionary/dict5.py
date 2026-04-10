d1 = {'Google' : 1, 
			'Facebook' : 2, 
			'Microsoft' : 3
			} 
d2 = {'GFG' : 1, 
			'Microsoft' : 2, 
			'Youtube' : 3
			} 
d1.update(d2); 
for key, values in d1.items(): 
	print(key, values , end=" ")
	
# dictionary1.update(dictionary2) is used to update the entries of dictionary1 with entries of dictionary2. If there are same keys in two dictionaries, then the value in the second dictionary is used.