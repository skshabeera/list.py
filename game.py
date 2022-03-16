#  Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
n=int(input("enter the number"))
l=[]
s_list=[]
main_list=[]
min_list=[]
max_list=[]
for i in range(0,n):
    number=int(input("enter the number"))
    l.append(number)
    s=0
    m=0
    for value in l:
        if s==0:
            s=value
            m=value
        elif value<s:
            s=value
        elif l[i]>m: 
            m=value
        elif l[i]<m:
            m=value
    s_list.append(s)
    main_list.append(m)
print(s_list,main_list)
a=min(s_list)
b=max(main_list)
k=0
while k<len(s_list):
    if a==s_list[k]:
        min_list.append(1)
    else:
        min_list.append(0)
    k=k+1
print(min_list)
h=0
while h<len(main_list):
    if b==main_list[h]:
        max_list.append(1)
    else:
        max_list.append(0)
    h=h+1
print(max_list)

    # print(min_list)

