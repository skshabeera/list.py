a=[2,3,1,45,15]
i=0
while i<len(a):
    j=i
    while j<len(a):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j+=1
    i+=1
print(a)