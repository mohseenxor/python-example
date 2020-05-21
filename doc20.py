class person:
	def __init__(self,name):
		self.name = name
		name = "john"
		print(name)
	def display(self):
		print("hello",self.name)

person1 = person("amul")
person1.display()
