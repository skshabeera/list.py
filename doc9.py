l=[10,30,29,90,56,78,100]
i=0
max=0
max1=0
max2=0
while i<len(l):
    if l[i]>max:
        max1=max
        max=l[i]
    elif max>l[i] and max1<l[i]:
        max2=max1
        max1=l[i]
    elif max1<l[i] and max> l[i]:
        max2=l[i]
    i=i+1
print(max,max1,max2)