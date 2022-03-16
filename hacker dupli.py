n=list(map(int,input("enter the number").rstrip().split()))
l=[]
i=0
while i<len(n):
    if n[i] not in l:
        l.append(n[i])
        l.sort()
    i=i+1
print(l)