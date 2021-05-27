a=[1,2,3,4,5,6]
i=0
even=0
odd=0
b=[]
c=0
r=0

while i<len(a):
	if a[i]%2==0:
		even=even+1
		c =a[i]*100
		b.append(c)
	else:
		odd=odd+1
		r=a[i]*-1
		b.append(r)
	i=i+1
print(b)