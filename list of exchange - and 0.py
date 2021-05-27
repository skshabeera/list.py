a=[-3, 1,3,2,-1,-1, 4]
i=0
while i<len(a):
	if a[i]<0:
		a[i]=0
	i=i+1
print(a)