a=[2,3,4,5,5,4,6,7]
i=0
b=[]
c=[]
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
	else:
		c.append(a[i])
	i+=1
print(b)
print(c)