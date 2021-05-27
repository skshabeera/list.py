a = [[1,2,3],[4,5,6],[7,8,9]]
sym = True
i=0
while i<len(a):
  j=0
  while j<len(a[i]):
      if a[i][j]!=a[j][i]:
      	sym = False
      j+=1
  i+=1
print (sym)