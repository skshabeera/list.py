mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
c = mainstr.split(' ')
a = ' '
i = 0
while i<len(c):
	if  c[i]=="over":
		a=a+'on'+' '
	else:
		a=a+c[i]+' '
	i=i+1
print(a)