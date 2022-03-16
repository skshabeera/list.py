n=int(input("enter the number"))
i=0
list=[]
odd_count=0
even_count=0
while i<n:
    num=int(input("enter the number"))
    list.append(num)
    if list[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i=i+1
print(list)
if even_count>odd_count:
    print("your ready to do battle")
elif even_count==odd_count:
    print("your not ready")
else:
    print("your not ready")
