A=["A","B"]
b=[]
i=1
n=int(input("enter a num:"))
while i<=n:
	j=0
	while j<len(A):
		b=b+[A[j]+str(i)]
		j=j+1
	i=i+1
print(b)