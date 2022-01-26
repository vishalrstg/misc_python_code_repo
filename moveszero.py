def moveszero(n):
	counter=0
	i=0
	while i<len(n):
		if n[i]!=0:
			n[counter]=n[i]
			counter= counter+1
		i+=1
	for i in range(counter, len(n)):
		n[i]=0
	return n
		
		
n=[1,0,2,3,0,9,0,5,0]
print(moveszero(n))
