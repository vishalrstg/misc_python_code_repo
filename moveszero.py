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

#i=0, j=0, [1,0,2,3,0,9,0,5]
#i=2, j=2 ,[1,0,2,3,0,9,0,5],i=3, j=3 [1,2,0,3,0,9,0,5], [1,2,3,0,0,9,0,5]i=4, j=4, j=5, i=5, [1,2,3,0,9,0,0,5], j=6, i=6, [1,2,3,0,9,0,0,5], j=7, i=7

#[0,0,0,0,2,3,9,0,5] i=0, j=4, [2,0,0,0,0,3,9,0,5]
#i=1, j=2, i=1, j=5, [2,3,0,0,0,0,9,0,5]
#i=2, j=6
