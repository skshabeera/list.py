a = int(input("enter the number :"))
i = 0
n=[]
m=[]
while i<a:
	p= int(input("enter the num :"))
	if p%2==0:
		n.append(p)
	else:
		m.append(p)
	i+=1
print(n)
print(m)