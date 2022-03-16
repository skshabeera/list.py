list=[["a","b","c"],["d","e","f"],["g","h","i"]]
for i in list:
    for j in i:
        print(j,end="")
list=[["a","b","c"],["d","e","f"],["g","h","i"]]
i=0
str=" "
while i<len(list):
    j=0
    while j<len(list[i]):
        str+=list[i][j]
        j=j+1
    i=i+1
print(str)
