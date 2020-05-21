var = 10
def func1():
	global var
	var = var+1
	print("variable value is func1 is ",var)
	return

#main

func1()
