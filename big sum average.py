n=(list(map(int,input("enter the number").rstrip().split())))
i=0
sum=0
while i<len(n):
    sum=sum+n[i]
    i=i+1
print(sum)