d = {} 
d[(1,2,4)] = 8
d[(4,2,1)] = 10
d[(1,2)] = 12

sum = 0
for k in d: 
	sum += d[k] 

print (len(d) + sum)