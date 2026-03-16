class student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	@staticmethod
	def hello():
		print("hi this is a static method")
	def welcome(self):
		print("welcome",self.name)
	def get_marks(self):
		print("marks",self.marks)
s1=student("rahul",45)
s1.welcome()
s1.get_marks()  
s1.hello()              
        	