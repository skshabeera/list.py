i = 1
n=[]
while i<=140:
	j=12
	while j<=14:
		if i%j==0:
			n.append(i)
		j+=2
	i+=1
print(n)