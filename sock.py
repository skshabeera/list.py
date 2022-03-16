l=[10,10,11,20,20,10,50,30,10]
i=0
l1=[]
while i<len(l):
    if l[i] not in l1:
        l1.append(l[i])
    i=i+1
print(l1)
j=0
socks=0
while j<len(l1):
    c=0
    k=0
    while k<len(l):
        if l1[j]==l[k]:
           c=c+1
        k=k+1
    j=j+1
    socks+=c//2
print(socks)
    

        
