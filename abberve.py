from typing import Counter


a=[5, 6, 7]
b=[3, 6, 10]
# a=[17 ,28 ,30]
# b=[99 ,16, 8]

i=0
count_a=0
count_b=0
# Counter=0
l=[]
while i<len(a):
    if a[i]>b[i]:
        count_a+=1
    elif b[i]>a[i]:
        count_b+=1
    elif a[i]==b[i]:
        pass
    i=i+1
l.append(count_b)
l.append(count_a)
print(l)