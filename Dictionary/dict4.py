d = dict() 
d['key1'] = {'key1' : 44, 'key2' : 566} 
d['key2'] = [1, 2, 3, 4] 
for (key, values) in d.items(): 
	print(values, end = "") 

# O/P = {'key1': 44, 'key2': 566}[1, 2, 3, 4]