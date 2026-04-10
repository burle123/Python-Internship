d = {} 

def addTodict(country): 
	if country in d: 
		d[country] += 1
	else: 
		d[country] = 1

addTodict('China') 
addTodict('Japan') 
addTodict('china') 

print (len(d))