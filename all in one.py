ele= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
c=0
even=0
odd=0
even_sum=0
odd_sum=0
while i<len(ele):
	if ele[i]%2==0:
		even=even+1
		even_sum=even_sum+ele[i]
		
		print(ele[i])
	else:
		odd_sum=odd_sum+ele[i]
		odd=odd+1
		a=even_sum+odd_sum/len(ele)
		print(ele[i])
		c=c+1
	i=i+1
print('even numbers',even,'the even sum ',even_sum,)
print('odd numbers',odd,'the sum of odd',odd_sum,a)