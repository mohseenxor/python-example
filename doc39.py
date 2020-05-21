n = int(input("enter the number"))
result = 1
for i in range(n,0,-1):
	print(i)
	result = result*i

print("factorial of",n,"is",result) 
