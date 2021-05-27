m=int(input("enter the length:"))
i = 0
n=[]
while i<m:
	d=int(input("enter the no.b:"))
	n.append(d)
	i+=1
print(n)
c = int(input("enter the number:"))
n.remove(c)
print(n)