a="my name is sindhu"
n=[]
i=0
temp =' '
while i<len(a):
	if a[i]==' ':
		n.append(temp)
		temp=' '
	else:
		temp=temp+a[i]
	i+=1
n.append(temp)
print(n)

#make a list without using split function
