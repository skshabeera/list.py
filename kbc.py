question_list = [
    "How many continents are there?",          
    "What is the capital of India?",           
    "in ng which course learning"    
]
options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal= ", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1] 
print("Well come to KBC Game!!")
print("Good morning to all audience")
print("now our quation showing on screen:")
i= 0
while i<len(question_list):
	print(i+1,question_list[i])
	a= 0
	while a<=len(options_list):
		print(a+1,options_list[i][a])
		a= a+1
	j= int(input('enter solution'))
	if j==solution_list[i]:
			print('congrats')
	else:
			print('quit')
			break
	i=i+1