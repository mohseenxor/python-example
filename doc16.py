import math
num = int(input("please enter the number to cal factorial of:"))
try:
	result=math.factorial(num)
	print(result)
except:
	print("cannot compute the factorial of -ve number")
