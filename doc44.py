lower = int(input("enter the lower number"))
upper = int(input("enter the upper number"))

for num in range(lower,upper+1):
	result = 0
	for i in range(1,num):
		if (num%i)==0:
			result=result+i
	if num==result:
		print(num)
