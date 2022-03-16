user=int(input("enter the number"))
l=[]
for i in range(0,user):
    l.append(list(map(int,input("enter the number").strip().split())))
print(l)
i=0
sum=0
j=2
add=0
while i<len(l):
    sum=sum+l[i][i]
    add=add+l[i][j]
    i=i+1
    j=j-1
    b=sum-add
print(abs(b))
# 11 2 4
# 4 5 6
# 10 8 -12

        