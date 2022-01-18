def stockspan(n):
	span=[1]
	stack=[0]
	for i in range(1, len(n)):
		while len(stack)>0 and n[i] > n[stack[-1]] :
			stack.pop()
		if len(stack)==0:
			span.append(i+1)
		else:
			span.append(i-stack[-1])
		stack.append(i)
			#if n[i] < n[stack[len(stack)-1]]:
			#	span.append(i-stack[len(stack)-1])
			#stack.append(i)
	return span
	
	

	
	
n=[100,60,70,65,120,85,110,20,95]
print(stockspan(n))
[1, 1, 2, 1, 5, 1, 2, 1, 2]
#answer 1,1,2,1,4,5,1,2,8]

