class car:
	def __init__(self):
		self.brk=False
		self.acc=False
		self.clu=False
	def start(self):
		self.acc=True
		self.clu=True
		print("car started")
	def stop(self):
		self.brk=True
		print("car stopped")	
car1=car()
car1.start()
car1.stop()			