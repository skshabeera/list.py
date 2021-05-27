list1=["A","B","C"]
list2=[[1,2],[2,3],[4,5]]
n=input("enter the number")
i=0
while i<len(list1):
    if n==list1[i]:
        list1[i]==list2[i]
        print(list2[i])
    i=i+1