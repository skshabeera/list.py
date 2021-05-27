num=int(input("enter any num for 1st loop="))
i=1
list=[]
s=1
while i<=num:
    j=1
    list1=[]
    num1=int(input("enter nay num for 2nd loop="))
    while j<=num1:
        list1.append(s)
        j+=1
        s+=1
    list.append(list1)
    i+=1
print(list)
#create nested list and out is in pair
#If user will give 2 o/p should be like this
# [[1,2],[3,4]]