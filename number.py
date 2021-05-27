a=[10,11,12,13,14,17,18,19,20]
num=30
i=0
n=[]
while i<len(a):
	j=i
	while j<len(a):
		if a[i]+a[j]==num:
			n.append([a[i],a[j]])
		j+=1
	i+=1
print(n)