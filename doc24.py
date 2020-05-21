class person:
	def display(self):
		print("hello,this is class person")

class employee(person):
	def printing(self):
		print("hello,this is derived class emp")

class programmer(employee):
	def show(self):
		print("hello,another derived class programmer")

p1 = programmer()
p1.display()
p1.printing()
p1.show()
