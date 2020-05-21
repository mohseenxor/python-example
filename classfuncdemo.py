class Myclass:
	name = "Mosin"
	def sum(self,a,b):
		print(a+b)
	def __init__(self, name, age):
		self.name = name
		self.age = age

x = Myclass("John", 40)
print(x.name)
print(x.age)
x.sum(4,5)
