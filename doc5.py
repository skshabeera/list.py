l=[1,2,2,5,8,4,4,8]
c=0
i=0
l1=[] 
while i<len(l):
    if l[i] not in l1:
        l1.append(l[i])
        c=c+1
    i=i+1
print(c)
    
