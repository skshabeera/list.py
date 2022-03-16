# 1222311
n=input("enter the number")
s=" "
for i in (0,len(n)):
    if i!=0:
        if n[i]==n[i-1]:
            continue
    c=0
    for j in(i,len(n)):
        if n[i]==n[j]:
            c=c+1
        else:
            break
    s='strip('
print(c,n[i])




