n=int(input("enter the  number"))
i=1
dict={}
while i<n:
    order=int(input("enter the number of order"))
    preparation_time=int(input("enter the number of preparation time"))
    delivery=order+preparation_time
    dict[i]=delivery
    b=sorted(dict.values())
    i=i+1
print(dict)
print(b)
k=0
list=[]
while k<len(b):
    for j in dict:
        if b[k]==dict[j]:
            list.append(j)
    k=k+1 
m=0
list3=[]
while m<len(list):
    if list[m] not in list3:
        list3.append(list[m])
    m=m+1
print(list3)
