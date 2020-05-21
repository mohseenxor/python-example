class student:
	clg = 'xyz'

	def __init__(self,rollno,name):
		self.rollno = rollno
		self.name = name

	def display(self):
		print("student name:",self.name)
		print("studnet rollnumber:",self.rollno)
		print("college:",student.clg)

student1 = student('xyz001',"amul")
student1.display()

student2 = student('xyz056',"john")
student2.display()
