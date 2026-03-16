class votererror(base exception):
	def __init__(self,name):
		super().__init__()
print("enter a age")
age=int(input())
if age>=18:
	print("eligibal")
else:
	try:
		raise votererror("agge not allow")
	except:
		print("not allow")
print("main end")