d = {1 : 1, 2 : '2', '1' : 1, '2' : 3} 
d['1'] = 2
print(d[d[d[str(d[1])]]])

# The program evaluates keys step by step: d[1] → 1 → str(1) = '1' → d['1'] = 2 → d[2] = '2' → d['2'] = 3, so the final output is 3.

# O/P = 3