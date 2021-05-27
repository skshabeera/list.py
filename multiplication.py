list = [[1,2,3],[2,3]]
i=0
while i<len(list):
	mul=1
	j=0
	while j<len(list[i]):
		mul=mul*list[i][j]
		j=j+1
	i=i+1
	print(mul)