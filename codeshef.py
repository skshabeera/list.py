w=[2, 3.5,4.3,"hello world", 5, 4.3]
x=[]
y=[]
z=[]
i = 0
while i<len(w):
    if w[i]==str(w[i]):
        x.append(w[i])
    elif w[i]==int(w[i]):
        y.append(w[i])
    elif w[i]==float(w[i]):
        z.append(w[i])
    else:
    	print(i)
    i+=1
print(x)
print(y)
print(z)