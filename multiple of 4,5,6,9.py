i = 1
b=[]
while i<101:
	if i%4==0:
		b.append(i)
	elif i%6==0:
		b.append(i)
	elif i%8==0:
		b.appenda(i)
	elif i%10==0:
		b.append(i)
	elif i%3==1:
		b.append(i)
	elif i%5==1:
		b.append(i)
	elif i%7==1:
		b.append(i)
	elif i%9==1:
		b.append(i)
	else:
		pass
	i+=1
print(b)