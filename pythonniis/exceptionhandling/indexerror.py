print("main start")
l=[10,20,30]
try:
	print(l[2])
except IndexError as e:
	print(e)
print("main end")		
