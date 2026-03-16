class votererror(BaseException):
	def __init__(self,name):
		super().__init__()
age=int(input("enter age"))
if age>18:
	print("eligible")
else:
	try:
		raise votererror("age not allow")
	except:
		print("not allow")
print("main end")					