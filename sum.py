n=int(input("enter the number"))
i=0
l=[]
sum=0
while i<n:
    number=int(input("enter the number"))
    l.append(number)
    sum=sum+l[i]
    i=i+1
print(sum)
