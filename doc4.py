l=[6,1,3,5,6,3,1]
i=0
l1=[]
mul=1
while i<len(l):
    if l[i] not in l1:
        l1.append(l[i])
        mul=mul*l1[i]
    i=i+1
print(mul)