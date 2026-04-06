class student:
	def __init__(self,marks1,marks2,marks3):
		self.mark1=marks1
		self.mark2=marks2
		self.mark3=marks3
	def avarage(self):
		print((self.mark1+self.mark2+self.mark3)/3)
s1=student(45,34,89)
s1.avarage()