c = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i = 0
a = []
count= 0
while i<len(c):
	j = 0
	b = []
	count1= 0
	while j<len(c):
		if c[i]==c[j]:
			count1= count1+1
		j+=1
	b.append(c[i])
	b.append(count1)
	if b not in a:
		a.append(b)
 
	i+=1
print(a)
print(count1)
	