def counter(c):
	if c<=0:
		return c
	else:
		return c+counter(c-1)

counter(5)
